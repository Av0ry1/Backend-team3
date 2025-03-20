from dataclasses import dataclass
from fastapi.responses import FileResponse


@dataclass
class Picture:
    id: str
    picture_url: str


@dataclass
class PictureToResponse:
    picture: FileResponse