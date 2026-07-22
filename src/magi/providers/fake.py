"""Deterministic fake provider used by tests and local development."""

from dataclasses import dataclass

from magi.domain.models import GenerationRequest, GenerationResult


@dataclass(frozen=True)
class FakeProvider:
    """Return a configured response without external network access."""

    provider_name: str
    model_name: str
    response: str

    async def generate(self, request: GenerationRequest) -> GenerationResult:
        """Return the configured response."""
        return GenerationResult(
            provider=self.provider_name,
            model=self.model_name,
            content=f"{self.response}: {request.prompt}",
            latency_ms=0,
            finish_reason="stop",
        )
