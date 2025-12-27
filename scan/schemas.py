from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime



from pydantic import BaseModel
from typing import List


# ---------- START SCAN ----------
class StartScanRequest(BaseModel):
    user_id: int
    mode: str          # "stationary" or "moving"
    provider: str


class StartScanResponse(BaseModel):
    scan_id: int
    message: str


# ---------- ADD POINT ----------
class ScanPointRequest(BaseModel):
    latitude: float
    longitude: float
    download_mbps: float
    upload_mbps: float
    latency_ms: float


class ScanPointResponse(ScanPointRequest):
    id: int


# ---------- ADD POINTS ----------
class AddScanPointsRequest(BaseModel):
    scan_id: int
    points: List[ScanPointRequest]


# ---------- END SCAN ----------
class EndScanRequest(BaseModel):
    scan_id: int


class EndScanResponse(BaseModel):
    message: str
    best_latitude: float
    best_longitude: float
    best_download_mbps: float
    best_upload_mbps: float
    best_latency_ms: float
    total_points: int
