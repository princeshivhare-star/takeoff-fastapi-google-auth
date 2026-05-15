from pydantic import BaseModel

class IDRequest(BaseModel):
    generated_id: str