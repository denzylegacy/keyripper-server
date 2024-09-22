from typing import Any
from abc import ABC, abstractmethod
from fastapi import HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from keyripper_server.infra import log, API_AUTH_TOKEN


class ResponseSchema(BaseModel):
    status_code: int
    message: str
    data: Any = None


class Controller(ABC):
    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response

    async def __handle(self, *args, **kwargs) -> ResponseSchema:
        try:
            response = await self.perform(*args, **kwargs)
            if response.status_code != status.HTTP_200_OK:
                raise HTTPException(
                    status_code=response.status_code, detail=response.message
                )
            return response
        except HTTPException as e:
            self.response.status_code = e.status_code
            response = ResponseSchema(
                status_code=e.status_code, message=str(e.detail)
            )
            log.error(f'Error [{e.status_code}] - {str(e)}')
            return response
        except Exception as e:
            self.response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response = ResponseSchema(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message='Internal server error',
                data={'error': str(e)[:45] + ' [...]'}
            )
            log.error(f'Error [500] - {str(e)}')
            return response

    @abstractmethod
    async def perform(self, *args, **kwargs) -> ResponseSchema:
        """Controller child class, which implements this abstract class."""

    async def handle(self, *args, **kwargs) -> JSONResponse:
        response_data = await self.__handle(*args, **kwargs)
        return JSONResponse(content=response_data.dict(), status_code=response_data.status_code)


class RequestsController(Controller):

    def __init__(self, request: Request, response: Response):
        super().__init__(request, response)

    async def perform(self) -> ResponseSchema:
        if str(self.request.headers.get('Authorization')) != str(API_AUTH_TOKEN):
            log.warn("Access attempt denied!")
            raise HTTPException(status_code=403, detail='Forbidden: Invalid token!')

        request_data = {
            "method": self.request.method,
            "url": str(self.request.url),
            "body": await self.request.json() if self.request.method in ["POST", "PUT"] else None
        }

        log.info(f'[request] Content: {request_data}')

        response_data = {
            "success": "Ok",
        }

        return ResponseSchema(status_code=status.HTTP_200_OK, message="Request processed successfully", data=response_data)
