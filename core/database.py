from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings
from models.analysis_model import AnalysisModel


async def init_db():
    # Create a Motor client
    client = AsyncIOMotorClient(settings.mongo_uri)

    # Select the database
    database = client[settings.mongo_dbname]

    # Initialize Beanie with the selected database and document models
    await init_beanie(database=database, document_models=[AnalysisModel])
