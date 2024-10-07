from src.admin.api.poses.repository import PosesRepository
from src.admin.api.poses.schemas import PoseFullOut, PoseOut, PoseOutPagination, PoseIn, OtherTitleIn, \
    OtherTitleInUpdate, OtherTitleOut


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

    async def update_pose_by_id(self, id_pose: int, pose_data: PoseIn) -> PoseFullOut:
        await self.poses_repository.update_pose_by_id(id_pose, pose_data)
        pose_db = await self.poses_repository.get_pose_by_id(id_pose)
        titles_of_pose = await self.poses_repository.get_poses_titles(id_pose)
        return PoseFullOut.from_db(pose_db, titles_of_pose)

    async def create_other_title(self, id_pose, other_title_data: OtherTitleIn) -> PoseFullOut:
        await self.poses_repository.create_other_title(id_pose, other_title_data)
        return await self.get_pose_by_id(id_pose)

    async def update_other_title(self, id_pose, id_other_title: int, other_title_data: OtherTitleInUpdate) -> PoseFullOut:
        await self.poses_repository.update_other_title(id_other_title, other_title_data)
        return await self.get_pose_by_id(id_pose)

    async def delete_other_titles(self, id_pose: int, id_other_title: int) -> PoseFullOut:
        await self.poses_repository.delete_other_title(id_other_title)
        return await self.get_pose_by_id(id_pose)