import os

import replicate

from core.config import settings
from repositories.analysis_repository import AnalysisRepository
from schemas.analysis_schema import AnalysisResponse, AnalysisCreate
from services.topic_retrieval_service import fetch_wikipedia_data

os.environ["REPLICATE_API_TOKEN"] = settings.replicate_api_token


async def analyze_topic(topic_name: str) -> AnalysisResponse | None:
    topic_name = topic_name.lower()

    # Fetch data from Wikipedia
    wiki_data = fetch_wikipedia_data(topic_name)

    if wiki_data:
        # extract title and text of wikipedia page
        title, text = wiki_data

        # Analyze data
        analysis_result = await __perform_analysis(title, text)

        # Store the analysis result
        new_analysis = await AnalysisRepository.create_analysis(analysis_result)

        return new_analysis
    else:
        return None


async def __perform_analysis(title: str, text: str) -> AnalysisCreate:
    summary = await __generate_summary(text)
    key_themes = await __generate_key_themes(text)
    insights = await __generate_insights(text)

    return AnalysisCreate(
        topic_name=title,
        summary=summary,
        key_themes=key_themes,
        insights=insights
    )


async def __generate_summary(text: str):
    summary_input = __create_llama_input(
        f'Summarize the following information: {text}',
        1000)
    output = await replicate.async_run("meta/llama-2-70b-chat", input=summary_input)
    return ''.join(output)


async def __generate_key_themes(text: str):
    key_themes_input = __create_llama_input(
        f'List the key themes (up to 50 words) associated with the following information: {text}',
        200)
    output = await replicate.async_run("meta/llama-2-70b-chat", input=key_themes_input)
    return ''.join(output)


async def __generate_insights(text: str):
    insights_input = __create_llama_input(
        f'What are some insights about the following information: {text}',
        2000)
    output = await replicate.async_run("meta/llama-2-70b-chat", input=insights_input)
    return ''.join(output)


def __create_llama_input(prompt_text, max_new_tokens):
    return {
        "debug": False,
        "top_k": 50,
        "top_p": 0.9,
        "system_prompt": (
            "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, "
            "while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, "
            "dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in "
            "nature. If a question does not make any sense, or is not factually coherent, explain why instead of "
            "answering something not correct. If you don't know the answer to a question, please don't share false "
            "information."
        ),
        "prompt": prompt_text,
        "temperature": 1,
        "max_new_tokens": max_new_tokens,
        "min_new_tokens": -1
    }
