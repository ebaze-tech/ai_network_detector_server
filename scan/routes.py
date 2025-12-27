from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from scan.compute_helpers import compute_best_spot

from . import schemas, models, compute_helpers
from auth.database import get_db

router = APIRouter(prefix="/scan", tags=["Scan"])

# --- 1. Start Scan ---
@router.post("/start", response_model=schemas.StartScanResponse)
def start_scan(
    payload: schemas.StartScanRequest,
    db: Session = Depends(get_db)
):
    new_scan = models.ScanSession(
       user_id=payload.user_id,
        mode=payload.mode,
        provider=payload.provider
        
    )
    db.add(new_scan)
    db.commit()
    db.refresh(new_scan)

    return {
        "scan_id": new_scan.id,
        "message": "Scan started successfully"
    }


# --- 2. Add Scan Points ---
@router.post("/add_points", response_model=List[schemas.ScanPointResponse])
def add_scan_points(
    payload: schemas.AddScanPointsRequest,
    db: Session = Depends(get_db)
):
    db_points = []

    for p in payload.points:
        scan_point = models.ScanPoint(
            scan_id=payload.scan_id,
            latitude=p.latitude,
            longitude=p.longitude,
            download_mbps=p.download_mbps,
            upload_mbps=p.upload_mbps,
            latency_ms=p.latency_ms
        )
        db.add(scan_point)
        db_points.append(scan_point)

    db.commit()
    for p in db_points:
        db.refresh(p)

    return db_points

# --- 3. End Scan ---
@router.post("/end", response_model=schemas.EndScanResponse)
def end_scan(scan_id: int, db: Session = Depends(get_db)):
    scan_points = db.query(models.ScanPoint).filter(models.ScanPoint.scan_id == scan_id).all()
    if not scan_points:
        raise HTTPException(status_code=404, detail="No scan points found")

    result = compute_best_spot(scan_points)

    # mark scan as ended
    scan = db.query(models.ScanSession).get(scan_id)
    if scan:
        scan.ended_at = datetime.utcnow()
        db.commit()

    return result