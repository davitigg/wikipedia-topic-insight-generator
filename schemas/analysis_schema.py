from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, Field


class AnalysisBase(BaseModel):
    topic_name: str = Field(..., description="The name of the topic being analyzed.")
    summary: str = Field(..., description="A brief summary of the analyzed topic.")
    key_themes: str = Field(..., description="The key themes identified in the analysis.")
    insights: str = Field(..., description="Insights derived from the analysis.")


class AnalysisCreate(AnalysisBase):
    pass


class AnalysisResponse(AnalysisBase):
    id: str = Field(None, alias='_id', description="The unique identifier of the analysis result.")
    created_at: datetime = Field(..., description="The timestamp when the analysis result was created.")

    class Config:
        json_encoders = {ObjectId: str}
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "topic_name": "Artificial Intelligence",
                "summary": "Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural "
                           "intelligence displayed by humans and animals.",
                "key_themes": "Machine Learning, Robotics, Natural Language Processing",
                "insights": "AI technology is rapidly advancing and has the potential to disrupt various industries."
            }
        }
