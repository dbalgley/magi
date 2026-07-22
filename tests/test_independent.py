"""Tests for the independent-response round."""

import pytest

from magi.domain.models import GenerationRequest
from magi.orchestration.independent import gather_independent_responses
from magi.providers.fake import FakeProvider


@pytest.mark.asyncio
async def test_gather_independent_responses_preserves_provider_order() -> None:
    """Return results in configured participant order."""
    providers = [
        FakeProvider("alpha", "model-a", "answer-a"),
        FakeProvider("beta", "model-b", "answer-b"),
        FakeProvider("gamma", "model-c", "answer-c"),
    ]

    results = await gather_independent_responses(
        providers,
        GenerationRequest(prompt="What is 2 + 2?"),
    )

    assert [result.provider for result in results] == ["alpha", "beta", "gamma"]
    assert all("What is 2 + 2?" in result.content for result in results)


@pytest.mark.asyncio
async def test_gather_independent_responses_requires_a_provider() -> None:
    """Reject an empty participant configuration."""
    with pytest.raises(ValueError, match="At least one provider"):
        await gather_independent_responses([], GenerationRequest(prompt="Question"))
