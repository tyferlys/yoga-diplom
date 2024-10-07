import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.website.api.poses.router import router as poses_router
from src.website.api import router as network_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(poses_router, prefix="/poses", tags=["Позы"])
app.include_router(network_router, prefix="/network", tags=["Нейронная сеть"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8070)

#uvicorn main:app --port 8090 --host 0.0.0.0 --workers 6