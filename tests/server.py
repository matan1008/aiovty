import asyncio

SERVER_CONNECTION_STRING = b'This is a minimal server\r\n'
SERVER_NAME = 'Router'


async def handle_connection(reader, writer):
    data = SERVER_CONNECTION_STRING + SERVER_NAME.encode() + b'> '
    writer.write(data)
    await writer.drain()
    await writer.is_closed()


async def vty_sever_task(server):
    try:
        await server.serve_forever()
    except asyncio.CancelledError:
        pass
