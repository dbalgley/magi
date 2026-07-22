"""Provider protocol and expected provider failures."""

from typing import Protocol

from magi.domain.models import GenerationRequest, GenerationResult


class ProviderError(Exception):
    """Base class for expected model-provider failures."""


class ProviderAuthenticationError(ProviderError):
    """Raised when provider credentials are missing or rejected."""


class ProviderRateLimitError(ProviderError):
    """Raised when a provider rejects a request due to rate limits."""


class ProviderTimeoutError(ProviderError):
    """Raised when a provider request exceeds its deadline."""


class ProviderUnavailableError(ProviderError):
    """Raised when a provider is temporarily unavailable."""


class InvalidProviderResponseError(ProviderError):
    """Raised when a provider response cannot be normalized."""


class ModelProvider(Protocol):
    """Interface implemented by all model-provider adapters."""

    @property
    def provider_name(self) -> str:
        """Return the stable provider identifier."""
        ...

    @property
    def model_name(self) -> str:
        """Return the configured model identifier."""
        ...

    async def generate(self, request: GenerationRequest) -> GenerationResult:
        """Generate one normalized model response."""
        ...
