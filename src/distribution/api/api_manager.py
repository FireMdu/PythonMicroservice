"""
Docs - http://172.0.0.1:8000/docs
"""

from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from src.infrastructure.logger import LogManager
from src.distribution.api.routers import book_api
from src.distribution.api.routers import users_api

import uvicorn

logger = LogManager().logger

class App:
    _title = "Python Microservice API Host Service"
    App = None
    
    def __init__(self):
        logger.info("Loading API Endpoints...")

        router = FastAPI(title = self._title)

        ## Add API endpoints here
        router.include_router(
            users_api.router, 
            prefix="/users", 
            tags=["users"])

        self.App = VersionedFastAPI(router,
            version_format='{major}',
            prefix_format='/v{major}',
            enable_latest=True
        )

class AppManager():
    _host = '127.0.0.1'
    _port = 8000
    thread_manager = None

    def start(self, thread_manager):
        self.thread_manager = thread_manager
        app = App()
        logger.info(f'Loading and starting API Service {app}')

        # Read more - https://www.uvicorn.org/deployment/ / "src.distribution.api.api_manager:App"
        uvicorn.run(app.App, host=self._host, port=self._port, log_level="info") # , reload=True
        logger.info(f"Hosting API Endpoints on Host [{self._host}] Port [{self._port}]")
        