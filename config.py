"""ForensicLens Configuration Module.

Centralized configuration settings for ForensicLens (SIH PS 26150).
Supports default settings, environment variable overrides, and JSON serialization.
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

# Base Directory
BASE_DIR = Path(__file__).resolve().parent


@dataclass
class ServerConfig:
    """Dashboard web server configuration."""
    host: str = field(default_factory=lambda: os.getenv("FORENSICLENS_HOST", "127.0.0.1"))
    port: int = field(default_factory=lambda: int(os.getenv("FORENSICLENS_PORT", "5000")))
    secret_key: str = field(
        default_factory=lambda: os.getenv(
            "FORENSICLENS_SECRET_KEY", "forensiclens-investigator-session-secret-2026"
        )
    )
    debug: bool = field(
        default_factory=lambda: os.getenv("FORENSICLENS_DEBUG", "false").lower() in ("true", "1", "yes")
    )
    no_browser: bool = field(
        default_factory=lambda: os.getenv("FORENSICLENS_NO_BROWSER", "false").lower() in ("true", "1", "yes")
    )


@dataclass
class PathsConfig:
    """Filesystem paths for exhibits, reports, and models."""
    base_dir: str = str(BASE_DIR)
    evidence_root: str = field(default_factory=lambda: os.getenv("FORENSICLENS_EVIDENCE_ROOT", "dataset/raw"))
    video_root: str = field(default_factory=lambda: os.getenv("FORENSICLENS_VIDEO_ROOT", "dataset/raw/video"))
    reports_dir: str = field(default_factory=lambda: os.getenv("FORENSICLENS_REPORTS_DIR", "reports"))
    models_dir: str = field(default_factory=lambda: os.getenv("FORENSICLENS_MODELS_DIR", "models"))
    case_workspace_file: str = "reports/case_workspace.json"
    current_report_file: str = "reports/forensic_case_report_CURRENT.json"


@dataclass
class VideoIntelligenceConfig:
    """Pretrained offline video intelligence and multi-object tracking settings."""
    model_name: str = field(default_factory=lambda: os.getenv("FORENSICLENS_MODEL_NAME", "yolov8n.pt"))
    confidence_threshold: float = 0.25
    sampling_stride_frames: int = 5
    frame_change_threshold: float = 0.12
    tracker: str = "bytetrack.yaml"
    coco_target_classes: dict[int, str] = field(
        default_factory=lambda: {0: "person", 1: "bicycle", 2: "car", 3: "motorcycle", 5: "bus", 7: "truck"}
    )


@dataclass
class LiveCameraConfig:
    """Real-time live camera surveillance and edge object detection settings."""
    model_name: str = field(default_factory=lambda: os.getenv("FORENSICLENS_LIVE_CAM_MODEL", "yolov8n.pt"))
    # Strictly enforced 80% threshold as required by specification
    confidence_threshold: float = 0.80
    threshold_percentage: str = "80%"
    target_fps: int = 30
    inference_interval_ms: int = 320
    input_resolution_width: int = 1280
    input_resolution_height: int = 720


@dataclass
class ForensicEventsConfig:
    """Forensic event anomaly thresholds and spatio-temporal rules."""
    anomaly_score_threshold: float = 0.65
    prolonged_presence_seconds: float = 10.0
    min_motion_displacement_pixels: float = 30.0


@dataclass
class CorrelationConfig:
    """Surveillance event correlation engine parameters."""
    temporal_proximity_window_seconds: float = 15.0
    cross_camera_window_seconds: float = 30.0


@dataclass
class USBMonitorConfig:
    """Live USB hardware monitor & kernel filesystem watchdog settings."""
    poll_interval_seconds: float = 1.0
    simulation_watch_path: str = "dataset/usb_test"
    max_history_events: int = 500
    auto_start: bool = True


@dataclass
class LegalComplianceConfig:
    """Legal compliance and audit trail configuration."""
    timezone_name: str = "Asia/Kolkata"
    timezone_offset: str = "UTC+05:30"
    legal_framework: str = "Section 65B Indian Evidence Act (Certificate of Electronic Evidence)"
    iso_standard: str = "ISO/IEC 27037 (Guidelines for Digital Evidence Handling)"
    hash_algorithm: str = "SHA-256"


@dataclass
class AppConfig:
    """Master application configuration container."""
    server: ServerConfig = field(default_factory=ServerConfig)
    paths: PathsConfig = field(default_factory=PathsConfig)
    video_intelligence: VideoIntelligenceConfig = field(default_factory=VideoIntelligenceConfig)
    live_camera: LiveCameraConfig = field(default_factory=LiveCameraConfig)
    forensic_events: ForensicEventsConfig = field(default_factory=ForensicEventsConfig)
    correlation: CorrelationConfig = field(default_factory=CorrelationConfig)
    usb_monitor: USBMonitorConfig = field(default_factory=USBMonitorConfig)
    compliance: LegalComplianceConfig = field(default_factory=LegalComplianceConfig)

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary."""
        return asdict(self)

    def save_json(self, path: Path | str = "config.json") -> None:
        """Export configuration to JSON file."""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load_json(cls, path: Path | str = "config.json") -> AppConfig:
        """Load configuration from JSON file."""
        config_path = Path(path)
        if config_path.is_file():
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return cls(
                server=ServerConfig(**data.get("server", {})),
                paths=PathsConfig(**data.get("paths", {})),
                video_intelligence=VideoIntelligenceConfig(**data.get("video_intelligence", {})),
                live_camera=LiveCameraConfig(**data.get("live_camera", {})),
                forensic_events=ForensicEventsConfig(**data.get("forensic_events", {})),
                correlation=CorrelationConfig(**data.get("correlation", {})),
                usb_monitor=USBMonitorConfig(**data.get("usb_monitor", {})),
                compliance=LegalComplianceConfig(**data.get("compliance", {})),
            )
        return cls()


# Default singleton instance
config = AppConfig()
Config = AppConfig
