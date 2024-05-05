import logging
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from Exceptions.app_exception import AppException
from Exceptions.duplicated_error_exception import DuplicatedErrorException
from Exceptions.not_found_error_exception import NotFoundErrorException
from Exceptions.unauthorized_exception import UnauthorizedException

logger = logging.getLogger(__name__)

class Exception_Handler_Middleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as http_exception:
            return JSONResponse(
                status_code=http_exception.status_code,
                content={"error": "Client Error", "message": str(http_exception.detail)},
            )
        except AppException as app_exception:
            return JSONResponse(
                status_code=400,
                content={"error": "Bad Request", "message": str(app_exception)},
            )
        except NotFoundErrorException as app_exception:
            return JSONResponse(
                status_code=404,
                content={"error": "Not Found", "message": str(app_exception)},
            )
        except DuplicatedErrorException as app_exception:
            return JSONResponse(
                status_code=409,
                content={"error": "Conflict", "message": str(app_exception)},
            )
        except UnauthorizedException as app_exception:
            return JSONResponse(
                status_code=401,
                content={"error": "Unauthorized", "message": str(app_exception)},
            )
        except Exception as e:
            logger.exception(e)
            return JSONResponse(
                status_code=500,
                content={"error": "Internal Server Error", "message": "An unexpected error occurred."},
            )