from src.website.api.poses.repository import PosesRepository
from src.website.api.poses.schemas import PoseFullOut, PoseOut, PoseOutPagination


class PosesService:
    def __init__(self):
        self.poses_repository = PosesRepository()

    async def get_poses(self, count: int, page: int) -> PoseOutPagination:
        poses_db = await self.poses_repository.get_poses(count, page)
        count_poses = await self.poses_repository.get_count_poses()
        poses = PoseOut.from_db_list(poses_db)

        return PoseOutPagination(
            all_pages=count_poses // count + 1,
            current_page=page + 1,
            poses=poses
        )

    async def get_pose_by_id(self, id_pose: int) -> PoseFullOut:
        pose_db = await self.poses_repository.get_pose_by_id(id_pose)
        titles_of_pose = await self.poses_repository.get_poses_titles(id_pose)
        return PoseFullOut.from_db(pose_db, titles_of_pose)