"""A decorator for handling requests and errors"""

from functools import wraps
from typing import Callable, Any, Awaitable
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError


def request_handler(
    func: Callable[..., Awaitable[Any]]
) -> Callable[..., Awaitable[JSONResponse]]:
    @wraps(func)
    async def wrapper(request: Request, *args: Any, **kwargs: Any) -> JSONResponse:
        try:
            result = await func(request, *args, **kwargs)
            status_code = 201 if request.method == "POST" else 200
            return JSONResponse(content=result, status_code=status_code)

        except ValidationError as e:
            return JSONResponse(
                status_code=400,
                content={"message": "Validation error", "errors": e.errors()},
            )
        except HTTPException as e:
            return JSONResponse(
                status_code=e.status_code, content={"message": e.detail}
            )
        except Exception as e:
            print(f"Unhandled error: {str(e)}")
            return JSONResponse(
                status_code=500, content={"message": "Internal server error"}
            )

    return wrapper
