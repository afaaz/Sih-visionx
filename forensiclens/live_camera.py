"""ForensicLens Live Camera Surveillance & Real-Time Object Detection Subsystem."""

from __future__ import annotations

import base64
from datetime import datetime, timezone, timedelta
import hashlib
from pathlib import Path
import time
from typing import Any

import cv2
import numpy as np

# Indian Standard Time (IST, UTC+05:30)
IST_TZ = timezone(timedelta(hours=5, minutes=30))

# Strictly enforced confidence threshold as required: 80% (0.80)
CONFIDENCE_THRESHOLD = 0.80


class LiveCameraDetector:
    """Manages real-time camera object detection with strictly enforced 80% confidence threshold."""

    def __init__(self, model_name: str = "yolov8n.pt") -> None:
        self.model_name = model_name
        self._model: Any = None
        self.is_running = False
        self.start_time: float | None = None
        self.total_frames = 0
        self.total_detections_count = 0
        self.detection_history: list[dict[str, Any]] = []
        self.max_history = 500

    def get_model(self) -> Any:
        """Lazily load the YOLO model."""
        if self._model is None:
            from ultralytics import YOLO
            self._model = YOLO(self.model_name)
        return self._model

    def get_status(self) -> dict[str, Any]:
        """Return operational status and metrics."""
        return {
            "status": "ready" if self._model is not None else "standby",
            "model_name": self.model_name,
            "confidence_threshold": CONFIDENCE_THRESHOLD,
            "threshold_percentage": "80%",
            "total_frames_analyzed": self.total_frames,
            "total_detections_count": self.total_detections_count,
            "recent_detections_count": len(self.detection_history),
            "is_running": self.is_running,
        }

    def start_session(self) -> None:
        """Mark camera surveillance session as active."""
        self.is_running = True
        self.start_time = time.time()

    def stop_session(self) -> None:
        """Stop camera surveillance session."""
        self.is_running = False

    def process_frame_base64(self, b64_image_data: str) -> dict[str, Any]:
        """Process an image frame encoded as base64 JPEG from the client webcam."""
        t0 = time.time()
        self.total_frames += 1

        if not self.is_running:
            self.start_session()

        # Strip data URL prefix if present (e.g. data:image/jpeg;base64,...)
        if "," in b64_image_data:
            b64_image_data = b64_image_data.split(",", 1)[1]

        try:
            image_bytes = base64.b64decode(b64_image_data)
            np_arr = np.frombuffer(image_bytes, np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        except Exception as e:
            return {"status": "error", "error": f"Failed to decode image frame: {e}", "detections": []}

        if frame is None:
            return {"status": "error", "error": "Invalid frame data", "detections": []}

        return self.detect_objects(frame, execution_start=t0)

    def detect_objects(self, frame: np.ndarray, execution_start: float | None = None) -> dict[str, Any]:
        """Run YOLO inference and strictly filter objects with confidence >= 0.80."""
        t0 = execution_start or time.time()
        model = self.get_model()

        # Run inference strictly with conf=0.80
        results = model(frame, conf=CONFIDENCE_THRESHOLD, verbose=False)
        boxes = results[0].boxes if results and len(results) > 0 else []

        now_ist = datetime.now(IST_TZ)
        ist_timestamp_str = now_ist.strftime("%d-%b-%Y %H:%M:%S.%f")[:-3] + " IST"
        time_elapsed = round(time.time() - (self.start_time or t0), 2)

        detections: list[dict[str, Any]] = []

        if boxes is not None:
            for box in boxes:
                conf = float(box.conf[0])
                # Double-check strict 80% threshold enforcement
                if conf < CONFIDENCE_THRESHOLD:
                    continue

                cls_id = int(box.cls[0])
                cls_name = model.names.get(cls_id, f"object_{cls_id}")
                xyxy = [int(v) for v in box.xyxy[0].tolist()]

                self.total_detections_count += 1
                det_id = f"det-live-{self.total_detections_count:06d}"

                # Generate Section 65B forensic verification hash
                seed = f"{det_id}:{cls_name}:{conf:.4f}:{ist_timestamp_str}:{xyxy}".encode("utf-8")
                item_hash = hashlib.sha256(seed).hexdigest()[:16]

                det = {
                    "detection_id": det_id,
                    "class_name": cls_name,
                    "confidence": round(conf, 4),
                    "confidence_pct": f"{conf * 100:.1f}%",
                    "bounding_box_xyxy": xyxy,
                    "timestamp_ist": ist_timestamp_str,
                    "timestamp_elapsed_seconds": time_elapsed,
                    "review_priority": "high",
                    "explanation": f"YOLOv8 confirmed '{cls_name}' with {conf * 100:.1f}% confidence (>= 80% threshold).",
                    "forensic_hash": item_hash,
                }
                detections.append(det)

                # Append to history ring-buffer
                self.detection_history.insert(0, det)
                if len(self.detection_history) > self.max_history:
                    self.detection_history.pop()

        proc_time_ms = round((time.time() - t0) * 1000, 1)

        return {
            "status": "success",
            "detections": detections,
            "count": len(detections),
            "threshold": CONFIDENCE_THRESHOLD,
            "processing_time_ms": proc_time_ms,
            "timestamp_ist": ist_timestamp_str,
            "timestamp_elapsed": time_elapsed,
        }

    def clear_history(self) -> None:
        """Clear detection history log."""
        self.detection_history.clear()
        self.total_detections_count = 0


# Global singleton instance for live camera surveillance
live_camera_detector = LiveCameraDetector()
