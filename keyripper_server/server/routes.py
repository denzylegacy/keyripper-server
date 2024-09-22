"""
Request Router
==============

This router handles incoming requests to the keyripper API.
"""

from fastapi import APIRouter, Request, Response
from fastapi.responses import RedirectResponse

from keyripper_server.application import RequestsController


router = APIRouter(prefix='/request', tags=['request'])


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
    controller = RequestsController(request, response)
    return await controller.handle()


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
    controller = RequestsController(request, response)
    return await controller.handle()
