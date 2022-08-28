# PythonMicroservice
Sample Microservice done in Python

## Setup Guide
1. Run the script `.\setup.ps1` in the root of the folder (It will create a virtual env and install required packages)

## Stack

### API Server
The swagger document can be found at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
Library  | Description | External Content
------------- | ------------- | -------------
[FastAPI](https://fastapi.tiangolo.com) | Design and document APIs | [Introduction](https://blog.devgenius.io/brief-introduction-to-fastapi-d6f25793b11a) > [Deep Dive]()
[Uvicorn](https://www.uvicorn.org/) | Web Server | [Introduction]() > [Deep Dive]()


## Feature Backlog
- [x] Include rolling file logging
- [x] Auto restore dependant libraries
- [ ] Hosted API's (Fast API)
- [x] Asyncronous Schedules (Asyncio)
- [ ] Unit Testing
- [ ] Multiple threads (API, Schedules, etc)
- [ ] ORM Data Access
- [ ] Proxy API Proxies (Request)
