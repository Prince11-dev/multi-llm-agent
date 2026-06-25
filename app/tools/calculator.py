import math


async def calculate(
    expression: str
):

    try:

        result = eval(
            expression,
            {
                "__builtins__": None,
                "math": math
            },
            {}
        )

        return {
            "success": True,
            "expression": expression,
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }