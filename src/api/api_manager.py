from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from src.endpoints import book_api

class App:
    _title = "Python Microservice API Host Service"
    App = None
    
    def __init__(self):
        print("Initializing API Services...")

        tmp_app = FastAPI(title = self._title)

        ## Add API endpoints here
        tmp_app.include_router(book_api.router)

        self.App = VersionedFastAPI(tmp_app,
            version_format='{major}',
            prefix_format='/v{major}',
            enable_latest=True
        )
        