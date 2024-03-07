from fastapi import FastAPI

from core.database import init_db
from routers.topic_analysis_router import router as topic_analysis_router


async def start_application() -> None:
    # Initialize the database on application startup
    await init_db()


app = FastAPI(
    title="Wikipedia Topic Insight Generator",
    description="This API enables users to retrieve data on specific topics from Wikipedia, "
                "analyze it using Large Language Models (LLMs) for key insights, "
                "and store the results in a database for easy access.",
    version="1.0.0"
)

# Include the router for topic analysis endpoints
app.include_router(topic_analysis_router)

# Add a startup event handler to initialize the app
app.add_event_handler("startup", start_application)


def run():
    """Run the application server."""
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


# Check if the run environment is main, which indicates direct execution
if __name__ == "__main__":
    run()
