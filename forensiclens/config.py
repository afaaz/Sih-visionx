"""ForensicLens package configuration alias."""

from __future__ import annotations

import sys
from pathlib import Path

# Add project root to sys.path if not present
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config import (
    AppConfig,
    Config,
    CorrelationConfig,
    ForensicEventsConfig,
    LegalComplianceConfig,
    LiveCameraConfig,
    PathsConfig,
    ServerConfig,
    USBMonitorConfig,
    VideoIntelligenceConfig,
    config,
)

__all__ = [
    "config",
    "Config",
    "AppConfig",
    "ServerConfig",
    "PathsConfig",
    "VideoIntelligenceConfig",
    "LiveCameraConfig",
    "ForensicEventsConfig",
    "CorrelationConfig",
    "USBMonitorConfig",
    "LegalComplianceConfig",
]
