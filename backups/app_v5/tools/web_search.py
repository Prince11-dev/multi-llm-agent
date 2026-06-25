from duckduckgo_search import DDGS


async def search_web(
    query: str,
    max_results: int = 5
):

    try:

        results = []

        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=max_results
            )

            for result in search_results:

                results.append(
                    {
                        "title": result.get("title", ""),
                        "body": result.get("body", ""),
                        "href": result.get("href", "")
                    }
                )

        return results

    except Exception as e:

        return [
            {
                "title": "Search Error",
                "body": str(e),
                "href": ""
            }
        ]