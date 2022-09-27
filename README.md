# PythonMicroservice
Sample Microservice done in Python

![image](https://user-images.githubusercontent.com/2478826/192550186-33d45858-6f77-44ee-9fb1-0b0941e5b188.png)

## Setup Guide
1. Run the script `.\setup.ps1` in the root of the folder (It will create a virtual env and install required packages)

## Stack Overview

### Overall
Library  | Description | External Content
------------- | ------------- | -------------
[sqlalchemy]() | ORM - DAL | [Introduction]() > [Deep Dive]()

### Scheduler
Library  | Description | External Content
------------- | ------------- | -------------
[asyncio]() | Asyncronous Processessing | [Introduction]() > [Deep Dive]()

### API Server
The swagger document can be found at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
Library  | Description | External Content
------------- | ------------- | -------------
[FastAPI](https://fastapi.tiangolo.com) | Design and document APIs | [Introduction](https://blog.devgenius.io/brief-introduction-to-fastapi-d6f25793b11a) > [Deep Dive]()
[Uvicorn](https://www.uvicorn.org/) | Web Server | [Introduction]() > [Deep Dive]()

### Website
Library  | Description | External Content
------------- | ------------- | -------------
[Flask](https://flask.palletsprojects.com/en/2.2.x/) | Micro Web Framework | [Introduction]() > [Deep Dive]()

## Feature Backlog
- [x] Include rolling file logging
- [x] Auto restore dependant libraries
- [x] Hosted API's (Fast API)
- [x] Asyncronous Schedules (Asyncio)
- [ ] Unit Testing
- [x] Multiple threads (API, Schedules, etc)
- [ ] Stress Testing (API Calls, Large Batches)
- [ ] ORM Data Access
- [ ] Proxy API Proxies (Request)
- [ ] Azure DevOps hosted in Linux container
