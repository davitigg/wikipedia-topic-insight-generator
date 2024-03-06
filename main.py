from fastapi import FastAPI

from core.database import init_db
from routers.topic_analysis_router import router as topic_analysis_router

app = FastAPI(
    title="Wikipedia Topic Insight Generator",
    description="This API enables users to retrieve data on specific topics from Wikipedia, analyze it using Large "
                "Language Models (LLMs) for key insights, and store the results in a database for easy access.",
    version="1.0.0"
)

app.include_router(topic_analysis_router)


@app.on_event("startup")
async def startup_event():
    await init_db()  # Initialize the database


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)  # No need to call init_db here
