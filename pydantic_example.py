from datetime import datetime
from pydantic import BaseModel, PositiveInt

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

external_data = {
    "id": 123,
    "signup_ts": "2023-10-01T12:00:00",
    "tastes": {"pizza": 5, "sushi": 3},
}

user = User(**external_data)

print(user.id) 
#> 123
print(user.model_dump())
"""
{ 
    'id': 123, 
    'name': 'John Doe', 
    'signup_ts': datetime.datetime(2023, 10, 1, 12, 0), 
    'tastes': {'pizza': 5, 'sushi': 3}
}
"""