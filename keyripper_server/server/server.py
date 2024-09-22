from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router


app = FastAPI(
    title='keyripper server',
    responses={
        404: {'error': True, 'message': 'Not Found', 'data': []},
        500: {'error': True, 'message': 'Internal Server Error', 'data': []},
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
