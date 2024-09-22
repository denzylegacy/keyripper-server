"""
Request Router
==============

This router handles incoming requests to the keyripper API.
"""

from fastapi import APIRouter, Request, Response, HTTPException, Depends
from fastapi.responses import RedirectResponse

from keyripper_server.infra import log, API_AUTH_TOKEN
from keyripper_server.application import RequestsController


router = APIRouter(prefix='/request', tags=['request'])

def auth(request: Request):
    if str(request.headers.get('Authorization')) != str(API_AUTH_TOKEN):
        log.warn("Access attempt denied!")
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
        request: Request, response: Response
    ):
    """
    Handles GET requests.

    Args:
        request (Request): HTTP request.
        response (Response): HTTP response.

    Returns:
        Response: HTTP response.
    """
    auth(request=request)
    return RequestsController(request, response).handle()


@router.post('/')
async def post_request(
        request: Request, response: Response
    ):
    """
    Handles POST requests.

    Args:
        request (Request): HTTP request.
        response (Response): HTTP response.

    Returns:
        Response: HTTP response.
    """
    auth(request=request)
    return RequestsController(request, response).handle()
