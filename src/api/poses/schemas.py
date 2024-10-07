from pydantic import BaseModel


class PoseOut(BaseModel):
    id: int
    source_title: str

    @classmethod
    def from_db_list(cls, poses_db) -> list["PoseOut"]:
        return [
            PoseOut(id=item[0], source_title=item[1]) for item in poses_db
        ]


class PoseOutPagination(BaseModel):
    all_pages: int
    current_page: int
    poses: list[PoseOut]


class PoseFullOut(BaseModel):
    id: int
    source_title: str

    @classmethod
    def from_db(cls, pose_db) -> "PoseFullOut":
        return PoseFullOut(id=pose_db[0], source_title=pose_db[1])

    @classmethod
    def from_db_list(cls, poses_db) -> list["PoseFullOut"]:
        return [
            PoseFullOut(id=item[0], source_title=item[1]) for item in poses_db
        ]