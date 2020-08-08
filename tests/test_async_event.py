import pytest
import asyncio
from pyee import AsyncIOEventEmitter

pytestmark = pytest.mark.asyncio


@pytest.fixture
async def emitter() -> AsyncIOEventEmitter:
    return AsyncIOEventEmitter(asyncio.get_event_loop())


async def test_event(emitter: AsyncIOEventEmitter):
    async def stream_event(data: str):
        assert data == '1'

    emitter.on('stream', stream_event)
    emitter.emit('stream', '2')
