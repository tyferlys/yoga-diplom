from fastapi import APIRouter, Depends

from src.api.network.schemas import PredictIn
from src.api.network.service import NetworkService
from src.api.poses.schemas import PoseFullOut

router = APIRouter()


@router.post("/predict")
async def predict(image: PredictIn, network_service: NetworkService = Depends(NetworkService)) -> PoseFullOut:
    answer = await network_service.predict(image)
    return answer