import base64
from datetime import datetime
from io import BytesIO

from PIL import Image

from src.api.network.repository import NetworkRepository
from src.api.network.schemas import PredictIn
from src.api.poses.repository import PosesRepository
from src.api.poses.schemas import PoseFullOut
from src.network.network import predict_model


class NetworkService:
    def __init__(self):
        self.network_repository = NetworkRepository()
        self.poses_repository = PosesRepository()

    def base64_to_image(self, image: str):
        image_data = base64.b64decode(image)
        image = Image.open(BytesIO(image_data))

        now = datetime.now()
        timestamp = int(now.timestamp() * 1000)
        fileName = f"./images_for_predict/image{timestamp}.png"

        image.save(fileName)

        return f"./images_for_predict/image{timestamp}.png"

    async def predict(self, image: PredictIn) -> PoseFullOut:
        path_to_image = self.base64_to_image(image.image)
        id_pose = predict_model(path_to_image)
        pose_db = await self.poses_repository.get_pose_by_id(id_pose)
        return PoseFullOut.from_db(pose_db)