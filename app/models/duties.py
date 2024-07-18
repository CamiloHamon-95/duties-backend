from pydantic import BaseModel
from datetime import datetime

class Duty(BaseModel):
    title: str
    description: str
    completed: bool = False
    datetime_start: int = int(datetime.timestamp(datetime.now()))
    datetime_end: int = int(datetime.timestamp(datetime.now()))
    created_at: int = int(datetime.timestamp(datetime.now()))
    modified_at: int = int(datetime.timestamp(datetime.now()))

    print('DESDE EL MODELO')
    print(int(datetime.timestamp(datetime.now())))