from pydantic import BaseModel

class AudioRequest(BaseModel):
    file_path: str