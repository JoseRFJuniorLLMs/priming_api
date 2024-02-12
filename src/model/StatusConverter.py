from src.model.Status import Status


def convert_to_string(status: Status) -> str:
    return status.value


def convert_to_status(value: str) -> Status:
    return Status(value)


class StatusConverter:
    def __init__(self):
        pass

