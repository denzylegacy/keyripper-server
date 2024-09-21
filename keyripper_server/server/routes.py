"""
Request Router
==============

This router handles incoming requests to the keyripper API.
"""

from fastapi import APIRouter, Request, Response, HTTPException, Depends
from fastapi.responses import RedirectResponse

from keyripper_server.infra import API_AUTH_TOKEN
from keyripper_server.application import RequestsController


router = APIRouter(prefix='/request', tags=['request'])

def auth(request: Request):
    if request.headers.get('Authorization') != API_AUTH_TOKEN:
        raise HTTPException(status_code=403, detail='Forbidden: Invalid token!')


@router.get('/swagger')
async def get_swagger():
    """
    Redirects to the API documentation.

    Returns:
        RedirectResponse: Redirects to the API documentation.
    """
    return RedirectResponse(url="/docs")


@router.get('/')
async def get_request(
        request: Request, response: Response, token: str = Depends(auth)
    ):
    """
    Handles GET requests.

    Args:
        request (Request): HTTP request.
        response (Response): HTTP response.

    Returns:
        Response: HTTP response.
    """
    return RequestsController(request, response).handle()


@router.post('/')
async def post_request(
        request: Request, response: Response, token: str = Depends(auth)
    ):
    """
    Handles POST requests.

    Args:
        request (Request): HTTP request.
        response (Response): HTTP response.

    Returns:
        Response: HTTP response.
    """
    return RequestsController(request, response).handle()
