from src.infrastructure.logger import LogManager
logger = LogManager.new()

logger.info('Starting microservice...')





# Auto dependancy resolution
# Instrumentation: Loging [Log4J] 
# Create async schedules [Asyncio]
# Host HTTP API [Fast API]
# Run schedules and API in Seperate Threads
# ORM DAL
# Consume API's [Requests]
# Make common classes global by loading them in the __init__.py

#import logging
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)

#import logging

# load the logging configuration
#logging.config.fileConfig('logging.ini')

