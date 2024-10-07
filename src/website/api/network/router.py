from fastapi import APIRouter, Depends

from src.website.api.network.schemas import PredictIn
from src.website.api.network.service import NetworkService
from src.website.api.poses.schemas import PoseFullOut

router = APIRouter()


@router.post("/predict")
async def predict(image: PredictIn, network_service: NetworkService = Depends(NetworkService)) -> PoseFullOut:
    answer = await network_service.predict(image)
    return answer