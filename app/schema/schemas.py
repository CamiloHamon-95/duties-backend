def indiviual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "completed": todo["completed"],
        "datetime_start": todo["datetime_start"],
        "datetime_end": todo["datetime_end"]
    }

def list_serial(todos) -> list:
    return [indiviual_serial(todo) for todo in todos]