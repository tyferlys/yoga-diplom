from fastapi import APIRouter, Depends

from src.website.api.poses.schemas import PoseFullOut, PoseOutPagination
from src.website.api.poses.service import PosesService

router = APIRouter()


@router.get("")
async def get_poses(count: int = 5, page: int = 0, poses_service: PosesService = Depends(PosesService)) -> PoseOutPagination:
    pose = await poses_service.get_poses(count, page)
    return pose


@router.get("/{id_pose}")
async def get_pose_by_id(id_pose: int, poses_service: PosesService = Depends(PosesService)) -> PoseFullOut:
    pose = await poses_service.get_pose_by_id(id_pose)
    return pose