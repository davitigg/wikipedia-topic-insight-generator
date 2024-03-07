import asyncio

import wikipediaapi
from cachetools import TTLCache

# Create a cache with a maximum size of 100 items and a TTL of 15 minutes
cache = TTLCache(maxsize=100, ttl=900)


async def fetch_wikipedia_data(topic_name: str) -> tuple[str, str] | None:
    def get_data():
        wiki_wiki = wikipediaapi.Wikipedia('wikipedia_topic_insight_generator')
        page = wiki_wiki.page(topic_name)

        # Check if the page exists
        if page.exists():
            return page.title, page.text
        else:
            return None

    # Check if the topic is in the cache
    if topic_name in cache:
        return cache[topic_name]

    # Fetch data and add it to the cache
    data = await asyncio.to_thread(get_data)
    if data:
        cache[topic_name] = data
    return data
