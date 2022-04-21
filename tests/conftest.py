import asyncio

import pytest_asyncio

from .server import handle_connection, vty_sever_task

asyncio_mode = 'strict'


@pytest_asyncio.fixture
async def connection_test_vty_server():
    server = await asyncio.start_server(handle_connection, '127.0.0.1', 8888)
    async with server:
        server_task = asyncio.create_task(vty_sever_task(server))
        await asyncio.sleep(0)
        try:
            yield
        finally:
            server_task.cancel()
            await server_task
