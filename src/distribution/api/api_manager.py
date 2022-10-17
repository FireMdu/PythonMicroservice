"""
Docs - http://172.0.0.1:8000/docs
"""

import uvicorn
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from src.infrastructure.logger import LogManager
from src.infrastructure.thread_manager import ThreadManager
from src.distribution.api.routers import users_api

__all__ = [
    "App",
    "AppManager"
]

logger = LogManager().logger


class App:
    _title = "Python Microservice API Host Service"
    name = "Microservice API Host"
    application = None
    
    def __init__(self):
        logger.info("Loading API Endpoints...")
        hosting_application = FastAPI(
            title=self._title,
            description="Python Microservice"
        )
        hosting_application.include_router(users_api.router)
        self.application = VersionedFastAPI(
            hosting_application,
            version_format='{major}',
            prefix_format='/v{major}',
            enable_latest=True
        )


class AppManager:
    _host = '0.0.0.0'
    _port = 8000
    thread_manager = None

    def start(self, thread_manager: ThreadManager):
        self.thread_manager = thread_manager
        app_service = App
        app_name = app_service.name
        logger.info(f"Loading - {app_name} ...")
        app = app_service()
        logger.info(f"Starting - {app_name}")
        uvicorn.run(app.application, host=self._host, port=self._port, log_level="info")
        logger.info(f"Hosting API Endpoints on Host [{self._host}] Port [{self._port}]")
