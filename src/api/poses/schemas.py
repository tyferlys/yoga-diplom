from typing import Optional

from pydantic import BaseModel


class PoseOut(BaseModel):
    id: int
    source_title: str
    image: Optional[str] = ""

    @classmethod
    def from_db_list(cls, poses_db) -> list["PoseOut"]:
        return [
            PoseOut(id=item[0], source_title=item[1], image=item[2]) for item in poses_db
        ]


class PoseOutPagination(BaseModel):
    all_pages: int
    current_page: int
    poses: list[PoseOut]


class PoseFullOut(BaseModel):
    id: int
    source_title: str
    image: Optional[str] = ""
    description: Optional[str] = ""
    other_titles: Optional[list[str]] = []


    @classmethod
    def from_db(cls, pose_db, titles_of_pose) -> "PoseFullOut":
        return PoseFullOut(
            id=pose_db[0],
            source_title=pose_db[1],
            image=pose_db[2],
            description=pose_db[3],
            other_titles=[item[2] for item in titles_of_pose]
        )

    @classmethod
    def from_db_list(cls, poses_db) -> list["PoseFullOut"]:
        return [
            PoseFullOut(id=item[0], source_title=item[1], image=item[2], description=item[3]) for item in poses_db
        ]