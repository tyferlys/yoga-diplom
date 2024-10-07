from fastapi import APIRouter, Depends

from src.admin.api.poses.schemas import PoseFullOut, PoseOutPagination, PoseIn
from src.admin.api.poses.service import PosesService

router = APIRouter()


@router.get("")
async def get_poses(count: int = 5, page: int = 0, poses_service: PosesService = Depends(PosesService)) -> PoseOutPagination:
    pose = await poses_service.get_poses(count, page)
    return pose


@router.get("/{id}")
async def get_pose_by_id(id_pose: int, poses_service: PosesService = Depends(PosesService)) -> PoseFullOut:
    pose = await poses_service.get_pose_by_id(id_pose)
    return pose


@router.post("/{id}")
async def update_pose_by_id(id_pose: int, pose_data: PoseIn, poses_service: PosesService = Depends(PosesService)) -> PoseFullOut:
    pose = await poses_service.update_pose_by_id(id_pose, pose_data)
    return pose