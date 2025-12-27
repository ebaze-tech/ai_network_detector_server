from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from auth.database import Base


class ScanSession(Base):
    __tablename__ = "scan_sessions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, index=True)

    mode = Column(String, nullable=False)  # "stationary" or "moving"

    provider = Column(String, nullable=False)  # MTN, Airtel, Glo, etc

    started_at = Column(DateTime, default=datetime.utcnow)

    ended_at = Column(DateTime, nullable=True)

    # relationship
    points = relationship("ScanPoint", back_populates="scan", cascade="all, delete")


class ScanPoint(Base):
    __tablename__ = "scan_points"

    id = Column(Integer, primary_key=True, index=True)

    scan_id = Column(Integer, ForeignKey("scan_sessions.id"), index=True)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    ssid = Column(String, nullable=True)      # optional for Wi-Fi networks
    rssi = Column(Float, nullable=True)       # optional for Wi-Fi

    download_mbps = Column(Float, nullable=False)
    upload_mbps = Column(Float, nullable=False)
    latency_ms = Column(Float, nullable=False)

    timestamp = Column(DateTime, default=datetime.utcnow)

    # relationship
    scan = relationship("ScanSession", back_populates="points")
