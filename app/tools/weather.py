import requests


async def get_weather(
    city: str
):

    try:

        url = (
            f"https://wttr.in/"
            f"{city}?format=j1"
        )

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        current = data[
            "current_condition"
        ][0]

        return {
            "success": True,
            "city": city,
            "temperature":
                current["temp_C"],
            "description":
                current["weatherDesc"][0]["value"],
            "humidity":
                current["humidity"]
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }