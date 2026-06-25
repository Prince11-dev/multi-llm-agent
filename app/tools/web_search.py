from duckduckgo_search import DDGS


async def search_web(
    query: str,
    max_results: int = 5
):
    try:
        results = []

        with DDGS(verify=False) as ddgs:
            search_results = list(
                ddgs.text(
                    query,
                    max_results=max_results
                )
            )

        for r in search_results:
            results.append(
                {
                    "title": r.get("title"),
                    "link": r.get("href"),
                    "snippet": r.get("body")
                }
            )

        return {
            "success": True,
            "results": results
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }