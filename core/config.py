from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # MongoDB configurations
    mongo_uri: str = "mongodb://localhost:27017"
    mongo_dbname: str = "wikipedia_insight_generator"

    # External API configurations
    wikipedia_api_url: str = "https://en.wikipedia.org/w/api.php"

    # Other settings
    secret_key: str = "your_secret_key_here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        # If you're using a `.env` file for your environment variables
        env_file = ".env"


settings = Settings()
