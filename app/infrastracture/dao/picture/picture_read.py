from bson import ObjectId

from app.core.picture.dao.picture_read import PictureRead
from app.core.picture.entities.picture import Picture, PictureToResponse
from app.infrastracture.dao.base import BaseDao
from fastapi.responses import FileResponse


class PictureReadImpl(BaseDao, PictureRead):
    def get_picture_by_id(self, id: str) -> Picture:
        picture = self._database["picture"].find_one({"_id": ObjectId(id)})
        if not picture:
            raise TypeError
        return PictureToResponse(picture=FileResponse(picture["picture_url"]))
