from pydantic import BaseModel

class Drum(BaseModel):
    id: int
    name: str
