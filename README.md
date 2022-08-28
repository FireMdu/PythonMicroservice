# PythonMicroservice
Sample Microservice done in Python

## Setup Guide
1. Run the script `.\setup.ps1` in the root of the folder (It will create a virtual env and install required packages)

## Stack

### API Server
Library  | Description | External Content
------------- | ------------- | -------------
FastAPI | Define your API Services | [Official Documentation](https://fastapi.tiangolo.com/)
Uvicorn  | Web Server | [Main Website](https://www.uvicorn.org/)


## Feature Backlog
- [x] Include rolling file logging
- [x] Auto restore dependant libraries
- [ ] Hosted API's (Fast API)
- [x] Asyncronous Schedules (Asyncio)
- [ ] Unit Testing
- [ ] Multiple threads (API, Schedules, etc)
- [ ] ORM Data Access
- [ ] Proxy API Proxies (Request)
