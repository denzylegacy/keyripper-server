from typing import Any
from fastapi import Request, Response
from keyripper_server.infra import log

class RequestsController:

    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response

    def handle(self) -> None:
        try:
            request_data = {
                "method": self.request.method,
                "url": str(self.request.url),
                "headers": dict(self.request.headers),
                "query_params": dict(self.request.query_params),
                "path_params": dict(self.request.path_params),
                "body": self.request.json() if self.request.method in ["POST", "PUT"] else None
            }

            log.info(f'[request] Content: {request_data}')
            
            return {"success": "Ok"}
        except Exception as error:
            log.error(f'Error handling request: {error}')
            return {"error": str(error)}
