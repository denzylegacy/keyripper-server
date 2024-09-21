import uvicorn

from keyripper_server import app
from keyripper_server.infra import settings


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=settings.HOST, 
        port=settings.PORT, 
        reload=settings.DEBUG,
    )
