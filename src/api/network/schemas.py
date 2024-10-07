from pydantic import BaseModel


class PredictIn(BaseModel):
    image: str

