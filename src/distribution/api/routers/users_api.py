from cmath import log
from fastapi import APIRouter
from src.infrastructure.logger import LogManager

logger = LogManager().logger
router = APIRouter()

@router.get("/")
async def read_users():
    logger.info('do get all users')
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me")
async def read_user_me():
    logger.info('do read_user_me')
    return {"username": "fakecurrentuser"}


@router.get("/{username}")
async def read_user(username: str):
    logger.info('do get user by username')
    return {"username": username}