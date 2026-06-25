import time
import uuid


def generate_session_id():

    return str(
        uuid.uuid4()
    )


def execution_timer():

    return time.time()


def calculate_time(
    start: float
):

    return round(
        time.time() - start,
        2
    )