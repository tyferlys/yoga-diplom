from fastapi import APIRouter, Depends

from src.admin.api.poses.schemas import PoseFullOut, PoseOutPagination, PoseIn, OtherTitleIn, OtherTitleInUpdate, \
    OtherTitleOut, ImageIn
from src.admin.api.poses.service import PosesService

router = APIRouter()


@router.get("")
async def get_poses(count: int = 5, page: int = 0, poses_service: PosesService = Depends(PosesService)) -> PoseOutPagination:
    pose = await poses_service.get_poses(count, page)
    return pose


@router.get("/{id_pose}")
async def get_pose_by_id(id_pose: int, poses_service: PosesService = Depends(PosesService)) -> PoseFullOut:
    pose = await poses_service.get_pose_by_id(id_pose)
    return pose


@router.post("/{id_pose}")
async def update_pose_by_id(id_pose: int, pose_data: PoseIn, poses_service: PosesService = Depends(PosesService)) -> PoseFullOut:
    pose = await poses_service.update_pose_by_id(id_pose, pose_data)
    return pose


@router.post("/{id_pose}/image")
async def update_image(id_pose: int, image: ImageIn, poses_service: PosesService = Depends(PosesService)):
    pose = await poses_service.update_image(id_pose, image)
    return pose


@router.post("/{id_pose}/other_titles")
async def create_other_title(id_pose: int, other_title_data: OtherTitleIn, poses_service: PosesService = Depends(PosesService)) -> PoseFullOut:
    pose = await poses_service.create_other_title(id_pose, other_title_data)
    return pose


@router.post("/{id_pose}/other_titles/{id_other_title}")
async def update_other_title(id_pose: int, id_other_title: int, other_title_data: OtherTitleInUpdate, poses_service: PosesService = Depends(PosesService)) -> PoseFullOut:
    pose = await poses_service.update_other_title(id_pose, id_other_title, other_title_data)
    return pose


@router.delete("/{id_pose}/other_titles/{id_other_title}")
async def delete_other_title(id_pose: int, id_other_title: int, poses_service: PosesService = Depends(PosesService)) -> PoseFullOut:
    pose = await poses_service.delete_other_titles(id_pose, id_other_title)
    return pose