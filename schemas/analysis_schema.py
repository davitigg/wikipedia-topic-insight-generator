from datetime import datetime
from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class AnalysisBase(BaseModel):
    topic_name: str = Field(..., description="The name of the topic being analyzed.")
    summary: str = Field(..., description="A brief summary of the analyzed topic.")
    key_themes: List[str] = Field(..., description="A list of key themes identified in the analysis.")
    trends: Optional[List[str]] = Field(None, description="Optional. A list of trends observed in the analysis.")
    insights: str = Field(..., description="Insights derived from the analysis.")


class AnalysisCreate(AnalysisBase):
    pass


class AnalysisResponse(AnalysisBase):
    id: str = Field(None, alias='_id', description="The unique identifier of the analysis result.")
    created_at: datetime = Field(..., description="The timestamp when the analysis result was created.")

    class Config:
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "topic_name": "Artificial Intelligence",
                "summary": "Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural "
                           "intelligence displayed by humans and animals.",
                "key_themes": ["Machine Learning", "Robotics", "Natural Language Processing"],
                "trends": ["Increasing use in healthcare", "Ethical considerations rising"],
                "insights": "AI technology is rapidly advancing and has the potential to disrupt various industries."
            }
        }
