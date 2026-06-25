import time
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start = time.time()

        response = await call_next(
            request
        )

        process_time = round(
            time.time() - start,
            2
        )

        print(
            f"""
[{request.method}]
{request.url.path}
{response.status_code}
{process_time}s
"""
        )

        return response