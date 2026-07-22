"""Independent participant-response round."""

import asyncio
from collections.abc import Sequence

from magi.domain.models import GenerationRequest, GenerationResult
from magi.providers.base import ModelProvider


async def gather_independent_responses(
    providers: Sequence[ModelProvider],
    request: GenerationRequest,
) -> list[GenerationResult]:
    """Ask all participants the same question concurrently.

    The method deliberately supplies no participant with another participant's response.
    """
    if not providers:
        raise ValueError("At least one provider is required")

    async with asyncio.TaskGroup() as task_group:
        tasks = [task_group.create_task(provider.generate(request)) for provider in providers]

    return [task.result() for task in tasks]
