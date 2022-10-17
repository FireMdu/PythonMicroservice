# PythonMicroservice
Sample Microservice done in Python

![image](https://user-images.githubusercontent.com/2478826/192550186-33d45858-6f77-44ee-9fb1-0b0941e5b188.png)

## Setup Guide
1. Run the powershell script `.\setup.ps1` in the root of the folder (It will create a virtual env and install required packages)

## Stack Overview

### Overall
| Library        | Description | External Content                 |
|----------------|-------------|----------------------------------|
 | [sqlalchemy]() | ORM - DAL   | [Introduction]() > [Deep Dive]() |

### Scheduler
| Library     | Description               | External Content                 |
|-------------|---------------------------|----------------------------------|
 | [asyncio]() | Asyncronous Processessing | [Introduction]() > [Deep Dive]() |

### API Server
The swagger document can be found at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

| Library                                 | Description              | External Content                                                                                     |  
|-----------------------------------------|--------------------------|------------------------------------------------------------------------------------------------------|
 | [FastAPI](https://fastapi.tiangolo.com) | Design and document APIs | [Introduction](https://blog.devgenius.io/brief-introduction-to-fastapi-d6f25793b11a) > [Deep Dive]() |
 | [Uvicorn](https://www.uvicorn.org/)     | Web Server               | [Introduction]() > [Deep Dive]()                                                                     |

### Website
| Library                                              | Description         | External Content                 |
|------------------------------------------------------|---------------------|----------------------------------|
 | [Flask](https://flask.palletsprojects.com/en/2.2.x/) | Micro Web Framework | [Introduction]() > [Deep Dive]() |

### Testing
| Library                                               | Description              | External Content                                                                                                                               | 
|-------------------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
 | [Pytest](https://docs.pytest.org/en/7.1.x/index.html) | Python testing framework | [Introduction](https://docs.pytest.org/en/7.1.x/getting-started.html) > [Deep Dive](https://docs.pytest.org/en/7.1.x/reference/reference.html) |

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
- [ ] Users get emails/messages when documents are due
- [ ] Loan maximum durations are document specific
- [ ] Document loan process should include some sort of holding zone before checkout
- [ ] Take into account holidays and weekend for due dates
- [ ] How are documents getting to the users? Maybe order and collect at start, the delivery system later (for off campus users)
- [ ] Provide shipping of documents from different campuses and a lead time concept
- [ ] The maximum documents a user can loan should depend on some sort of user role attribute

## Inoversity App Description

A university library management system where registered library users(staff and students) can loan library documents for a specific period.

The library has a few rules and assumptions:
- [x] The loaning of documents is in good faith and free. It's assumed the users are honest people who will oblige.  
  Otherwise, the app owners will start charging for taking out documents and put in place a fine system.
- [ ] The library can only have a limited number of copies for a document.
- [ ] Each user can only take out a limited number of documents, and they can only take out one copy of each document.
- [ ] The due date of the document is driven by the maximum loan duration set for the document.
- [ ] Only the documents available in the library system can be loaned.
- [ ] The documents can be returned to the library before their due date
