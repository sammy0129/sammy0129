import time
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from fastapi import Request


class BaseMiddleware:

    def __init__(self,  app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return
        start_time = time.time()
        request = Request(scope, receive, send)
        if not request.session.get('session'):
            request.session.setdefault('session', 'fuck')

        async def send_wrapper(message: Message) -> None:
            process_time = time.time() - start_time
            if message['type'] == 'http.response.start':
                headers = MutableHeaders(scope=message)
                headers.append('X-Process-Time', str(process_time))
            await send(message)
        await self.app(scope, receive, send_wrapper)


