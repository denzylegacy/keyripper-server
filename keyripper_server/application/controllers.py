from typing import Any
from fastapi import Request, Response

from keyripper_server.infra import log


class RequestsController:

    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response


    def handle(self) -> None:
        try:        
            log.info(f'[request] Content: {self.request}')
            
            return {"success": "Ok"}
        except Exception as error:
            return {"error": error}
