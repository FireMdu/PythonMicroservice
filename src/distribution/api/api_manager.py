from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from src.distribution.api.endpoints import book_api
from src.infrastructure.logger import LogManager
import uvicorn

logger = LogManager().logger

class App:
    _title = "Python Microservice API Host Service"
    app = None
    
    def __init__(self):
        logger.info("Loading API Endpoints...")

        tmp_app = FastAPI(title = self._title)

        ## Add API endpoints here
        tmp_app.include_router(book_api.router)

        self.app = VersionedFastAPI(tmp_app,
            version_format='{major}',
            prefix_format='/v{major}',
            enable_latest=True
        )

class AppManager():
    _host = '127.0.0.1'
    _port = 8005

    def start(self):
        app = App()
        logger.info(f'Loading and sstarting API Service {app}')
        uvicorn.run(app.app, host=self._host, port=self._port, log_level="info", reload=True)
        logger.info(f"Hosting API Endpoints on Host [{self._host}] Port [{self._port}]")
        