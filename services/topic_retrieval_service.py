import wikipediaapi


def fetch_wikipedia_data(topic_name: str) -> tuple[str, str] | None:
    wiki_wiki = wikipediaapi.Wikipedia('wikipedia_topic_insight_generator')
    page = wiki_wiki.page(topic_name)

    # Check if the page exists
    if page.exists():
        return page.title, page.text
    else:
        return None
