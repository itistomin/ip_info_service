from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException

from schemas.schemas import IPInfo, IPInfoResponse
from services.database import IPDatabase


db: IPDatabase | None = None


@asynccontextmanager
async def prepare_db(_: FastAPI):
    global db
    db = IPDatabase()
    yield


app = FastAPI(
    title="IP Info Demo",
    description="Provide IP information from a given IP address.",
    lifespan=prepare_db,
)


@app.get("/me")
async def get_my_ip_info(request: Request):
    data: IPInfo | None = await db.get_ip_info(request.client.host)
    if not data:
        raise HTTPException(status_code=404, detail="IP not found in the database")
    return IPInfoResponse(message="IP information successfully retrieved", results=data)


@app.get("/{ip}")
async def get_ip_info(ip: str) -> IPInfoResponse:
    data: IPInfo | None = await db.get_ip_info(ip)
    if not data:
        raise HTTPException(status_code=404, detail="IP not found in the database")
    return IPInfoResponse(message="IP information successfully retrieved", results=data)
