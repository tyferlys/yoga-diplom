from typing import Optional, Any

from pydantic import BaseModel


class DataClass(BaseModel):
    source_name: str
    russian_name: Optional[str]
    image: Any

    class Config:
        arbitrary_types_allowed = True
