"""
  aim: print http-body in middleware

Reference:
  - https://github.com/tiangolo/fastapi/issues/394
"""
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def set_body(self, request: Request):
        _msg = await request._receive()

        async def new_receive():
            return _msg

        request._receive = new_receive

    async def dispatch(self, request, call_next):
        await self.set_body(request)
        body = await request.body()
        print('http-body: ', body)

        response = await call_next(request)

        return response

