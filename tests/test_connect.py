import pytest

from aiovty import AioVtyClient
from .server import SERVER_NAME, SERVER_CONNECTION_STRING

pytestmark = pytest.mark.asyncio


@pytest.mark.usefixtures('connection_test_vty_server')
async def test_sanity():
    client = AioVtyClient(SERVER_NAME)
    assert await client.connect('127.0.0.1', 8888) == SERVER_CONNECTION_STRING


async def test_connection_error():
    client = AioVtyClient(SERVER_NAME)
    with pytest.raises(ConnectionRefusedError):
        assert await client.connect('127.0.0.1', 8888)
