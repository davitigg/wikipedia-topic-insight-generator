from typing import List, Optional

from beanie import PydanticObjectId
from bson.errors import InvalidId

from repositories.analysis_repository import AnalysisRepository
from schemas.analysis_schema import AnalysisResponse, AnalysisCreate


async def analyze_topic(topic_name: str) -> AnalysisResponse:
    # Placeholder logic for analyzing the topic
    # You should replace this with your actual analysis logic
    analysis_data = {
        "topic_name": topic_name,
        "summary": "This is a summary of the topic.",
        "key_themes": ["Theme1", "Theme2"],
        "trends": ["Trend1", "Trend2"],
        "insights": "These are insights about the topic."
    }
    analysis = AnalysisCreate(**analysis_data)
    new_analysis = await AnalysisRepository.create_analysis(analysis)
    return new_analysis


async def get_analyses(topic_name: Optional[str] = None) -> List[AnalysisResponse]:
    if topic_name:
        return await AnalysisRepository.get_all_analysis_by_topic_name(topic_name)
    else:
        return await AnalysisRepository.get_all_analysis()


async def get_specific_analysis(analysis_id: str) -> Optional[AnalysisResponse]:
    try:
        analysis_id_obj = PydanticObjectId(analysis_id)
    except InvalidId:
        return None
    return await AnalysisRepository.get_specific_analysis(analysis_id_obj)


async def delete_analyses(topic_name: str) -> int:
    if topic_name:
        return await AnalysisRepository.delete_all_analysis_by_topic_name(topic_name)
    else:
        return await AnalysisRepository.delete_all_analysis()


async def delete_specific_analysis(analysis_id: str) -> bool:
    try:
        analysis_id_obj = PydanticObjectId(analysis_id)
    except InvalidId:
        return False
    return await AnalysisRepository.delete_specific_analysis(analysis_id_obj)


async def get_topics() -> List[str]:
    return await AnalysisRepository.get_topics()
