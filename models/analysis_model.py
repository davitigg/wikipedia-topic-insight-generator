from datetime import datetime

from beanie import Document
from pydantic import Field


class AnalysisModel(Document):
    topic_name: str
    summary: str
    key_themes: str
    insights: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "analyses"
