"""Core provider-neutral request and response models."""

from pydantic import BaseModel, ConfigDict, Field


class GenerationRequest(BaseModel):
    """A normalized request sent to a model provider."""

    model_config = ConfigDict(frozen=True)

    prompt: str = Field(min_length=1)
    system_prompt: str | None = None
    temperature: float = Field(default=0.2, ge=0.0, le=2.0)


class GenerationResult(BaseModel):
    """A normalized result returned by a model provider."""

    model_config = ConfigDict(frozen=True)

    provider: str
    model: str
    content: str
    input_tokens: int | None = Field(default=None, ge=0)
    output_tokens: int | None = Field(default=None, ge=0)
    latency_ms: int = Field(ge=0)
    finish_reason: str | None = None
