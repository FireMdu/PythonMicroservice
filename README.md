# PythonMicroservice
Sample Microservice done in Python

## Setup Guide
1. Open terminal in root directory
2. Run 'pip install -r 'requirements.txt' to install dependant packages

## Known Issues
- When the logfile size limit is reached and it tries to rename the file to archive it fails saing the file is already being used by another process (~10mb)

## Feature Backlog
- [x] Include rolling file logging
- [x] Auto restore dependant libraries
- [ ] Hosted API's (Fast API)
- [ ] Asyncronous Schedules (Asyncio)
- [ ] Unit Testing
- [ ] Multiple threads (API, Schedules, etc)
- [ ] ORM Data Access
- [ ] Proxy API Proxies (Request)