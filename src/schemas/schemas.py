from pydantic import BaseModel


class IPInfo(BaseModel):
    ip: str
    country_key: str
    country: str
    region: str
    city: str
    latitude: float
    longitude: float
    zip_code: str
    timezone: str


class IPInfoResponse(BaseModel):
    message: str
    results: IPInfo
