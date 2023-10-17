import sys
sys.path.append("/Users/cucuridas/Desktop/project/TG-Chatbot2")

from fastapi import FastAPI
from app.api.v1.api import api_router
from app.db.init_db import *
from app.db.session import *
import uvicorn
def createApp() -> FastAPI:
    #WebexHook().addHook()
    db = SessionLocal()
    init_db(db)
    fastApiServer = FastAPI()
    fastApiServer.include_router(api_router)
    return fastApiServer


app = createApp()

class Server(uvicorn.Server):
    """Customized uvicorn.Server

    Uvicorn server overrides signals and we need to include
    Rocketry to the signals."""

    def handle_exit(self, sig: int, frame) -> None:
        return super().handle_exit(sig, frame)


def main():
    "Run scheduler and the API"
    server = Server(
        config=uvicorn.Config(
            app,
            workers=1,
            loop="asyncio",
            host="localhost",
            port=8000,
        )
    )

if __name__ == "__main__":
    main()