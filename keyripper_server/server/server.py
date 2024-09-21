from fastapi import FastAPI

from .routes import router


app = FastAPI(
    title='keyripper server',
    responses={
        404: {'error': True, 'message': 'Not Found', 'data': []},
        500: {'error': True, 'message': 'Internal Server Error', 'data': []},
    },
)

app.include_router(router)
