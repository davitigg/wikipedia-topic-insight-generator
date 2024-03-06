from typing import List, Optional

from beanie import PydanticObjectId

from models.analysis_model import AnalysisModel
from schemas.analysis_schema import AnalysisCreate, AnalysisResponse


class AnalysisRepository:

    @staticmethod
    async def create_analysis(analysis: AnalysisCreate) -> AnalysisResponse:
        analysis_model = AnalysisModel(**analysis.dict())
        await analysis_model.insert()
        return AnalysisResponse(**analysis_model.dict(by_alias=True))

    @staticmethod
    async def get_all_analysis() -> List[AnalysisResponse]:
        analyses = await AnalysisModel.find_all().to_list()
        return [AnalysisResponse(**analysis.dict(by_alias=True)) for analysis in analyses]

    @staticmethod
    async def get_all_analysis_by_topic_name(topic_name: [str]) -> List[AnalysisResponse]:
        analyses = await AnalysisModel.find(AnalysisModel.topic_name == topic_name).to_list()
        return [AnalysisResponse(**analysis.dict(by_alias=True)) for analysis in analyses]

    @staticmethod
    async def get_specific_analysis(analysis_id: PydanticObjectId) -> Optional[AnalysisResponse]:
        analysis_model = await AnalysisModel.get(document_id=analysis_id)
        if analysis_model:
            return AnalysisResponse(**analysis_model.dict(by_alias=True))
        return None

    @staticmethod
    async def delete_all_analysis() -> int:
        delete_result = await AnalysisModel.find_all().delete()
        if delete_result:
            return delete_result.deleted_count
        return 0

    @staticmethod
    async def delete_all_analysis_by_topic_name(topic_name: str) -> int:
        delete_result = await AnalysisModel.find(AnalysisModel.topic_name == topic_name).delete()
        if delete_result:
            return delete_result.deleted_count
        return 0

    @staticmethod
    async def delete_specific_analysis(analysis_id: PydanticObjectId) -> bool:
        analysis_model = await AnalysisModel.get(document_id=analysis_id)
        if analysis_model:
            await analysis_model.delete()
            return True
        return False

    @staticmethod
    async def get_topics() -> List[str]:
        collection = AnalysisModel.get_motor_collection()
        topics = await collection.distinct("topic_name")
        return topics
