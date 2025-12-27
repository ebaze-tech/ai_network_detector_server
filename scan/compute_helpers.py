from typing import List
from scan.models import ScanPoint  # your ScanPoint model

def compute_best_spot(points: List[ScanPoint]):
    """
    Compute best spot based on download speed.
    Returns dict matching EndScanResponse schema.
    """
    if not points:
        return {
            "message": "No points found",
            "best_latitude": 0.0,
            "best_longitude": 0.0,
            "best_download_mbps": 0.0,
            "best_upload_mbps": 0.0,
            "best_latency_ms": 0.0,
            "total_points": 0
        }

    best_point = max(points, key=lambda p: p.download_mbps)

    return {
        "message": "Scan completed successfully",
        "best_latitude": best_point.latitude,
        "best_longitude": best_point.longitude,
        "best_download_mbps": best_point.download_mbps,
        "best_upload_mbps": best_point.upload_mbps,
        "best_latency_ms": best_point.latency_ms,
        "total_points": len(points)
    }


def compute_stationary(scan_points: List[ScanPoint]):
    """
    Compute average performance for stationary mode.
    Returns average download, upload, latency, and a representative location.
    """
    if not scan_points:
        return {
            "message": "No scan points available",
            "best_latitude": 0.0,
            "best_longitude": 0.0,
            "avg_download_mbps": 0.0,
            "avg_upload_mbps": 0.0,
            "avg_latency_ms": 0.0,
        }

    total_download = sum(p.download_mbps for p in scan_points)
    total_upload = sum(p.upload_mbps for p in scan_points)
    total_latency = sum(p.latency_ms for p in scan_points)
    count = len(scan_points)

    avg_download = total_download / count
    avg_upload = total_upload / count
    avg_latency = total_latency / count

    # Use the first point's location as representative
    representative_point = scan_points[0]

    return {
        "message": "Stationary scan completed",
        "best_latitude": representative_point.latitude,
        "best_longitude": representative_point.longitude,
        "avg_download_mbps": avg_download,
        "avg_upload_mbps": avg_upload,
        "avg_latency_ms": avg_latency,
    }