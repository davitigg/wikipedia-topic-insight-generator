from typing import List, Optional

from fastapi import APIRouter, HTTPException, Path, Query

from schemas import analysis_schema
from services import analysis_storage_service, topic_analysis_service

router = APIRouter()


@router.post("/analysis", response_model=analysis_schema.AnalysisResponse, tags=["Topic Analysis"])
async def analyze_topic(
        topic_name: str = Query(..., description="The name of the topic to analyze")):
    analysis_result = await topic_analysis_service.analyze_topic(topic_name)
    return analysis_result


@router.get("/analysis", response_model=List[analysis_schema.AnalysisResponse], tags=["Topic Analysis"])
async def get_analyses(
        topic_name: Optional[str] = Query(None,
                                          description="Optional. If provided, filters the results to only include "
                                                      "analyses for the specified topic.")):
    results = await analysis_storage_service.get_analyses(topic_name)
    return results


@router.get("/analysis/{analysis_id}", response_model=analysis_schema.AnalysisResponse, tags=["Topic Analysis"])
async def get_specific_analysis(analysis_id: str = Path(..., description="The unique ID of the analysis result")):
    result = await analysis_storage_service.get_specific_analysis(analysis_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Analysis result not found")
    return result


@router.delete("/analysis", status_code=200, tags=["Management"])
async def delete_analyses(
        topic_name: Optional[str] = Query(None,
                                          description="Optional. If provided, deletes all analyses for the specified "
                                                      "topic. If not provided, deletes all analyses.")):
    deleted_count = await analysis_storage_service.delete_analyses(topic_name)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="No analysis found")
    return {"message": f"Deleted {deleted_count} analysis"}


@router.delete("/analysis/{analysis_id}", status_code=200, tags=["Management"])
async def delete_specific_analysis(
        analysis_id: str = Path(..., description="The unique ID of the analysis result to delete")):
    result = await analysis_storage_service.delete_specific_analysis(analysis_id)
    if result is False:
        raise HTTPException(status_code=404, detail="Analysis result not found")
    return {"message": "Analysis deleted successfully"}


@router.get("/topics", response_model=List[str], tags=["Topics"])
async def get_topics():
    topics = await analysis_storage_service.get_topics()
    return topics
