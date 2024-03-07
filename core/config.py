from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # MongoDB configurations
    mongo_uri: str
    mongo_dbname: str = "wikipedia_insight_generator"

    # Replicate API Token
    replicate_api_token: str

    # Load environment variables from a .env file
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
