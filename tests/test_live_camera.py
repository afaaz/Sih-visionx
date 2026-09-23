"""Tests for ForensicLens Live Camera Surveillance Subsystem."""

import base64
import unittest
import numpy as np
import cv2

from forensiclens.live_camera import LiveCameraDetector, CONFIDENCE_THRESHOLD
from forensiclens.dashboard.app import create_app


class LiveCameraSubsystemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.detector = LiveCameraDetector()
        self.app = create_app()
        self.client = self.app.test_client()

    def test_strict_eighty_percent_threshold_constant(self) -> None:
        """Enforce requirement: threshold must be strictly 80% (0.80)."""
        self.assertEqual(CONFIDENCE_THRESHOLD, 0.80)
        status = self.detector.get_status()
        self.assertEqual(status["confidence_threshold"], 0.80)
        self.assertEqual(status["threshold_percentage"], "80%")

    def test_detection_formatting_and_threshold_enforcement(self) -> None:
        """Verify that detect_objects returns valid structure with IST timestamps."""
        # Create a test frame
        img = np.zeros((360, 640, 3), dtype=np.uint8)
        result = self.detector.detect_objects(img)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["threshold"], 0.80)
        self.assertIn("timestamp_ist", result)
        self.assertTrue(result["timestamp_ist"].endswith("IST"))
        self.assertIsInstance(result["detections"], list)

    def test_process_frame_base64(self) -> None:
        """Verify processing base64 encoded frame from client webcam."""
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        _, buffer = cv2.imencode('.jpg', img)
        b64_str = base64.b64encode(buffer).decode('utf-8')
        data_url = f"data:image/jpeg;base64,{b64_str}"

        res = self.detector.process_frame_base64(data_url)
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["threshold"], 0.80)

    def test_api_live_camera_status(self) -> None:
        """Verify /api/live_camera/status endpoint."""
        resp = self.client.get("/api/live_camera/status")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["confidence_threshold"], 0.80)
        self.assertEqual(data["threshold_percentage"], "80%")

    def test_api_live_camera_detect_and_clear(self) -> None:
        """Verify /api/live_camera/detect and /api/live_camera/clear endpoints."""
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        _, buffer = cv2.imencode('.jpg', img)
        b64_str = base64.b64encode(buffer).decode('utf-8')

        resp = self.client.post("/api/live_camera/detect", json={"image": b64_str})
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["threshold"], 0.80)

        # Verify events endpoint
        events_resp = self.client.get("/api/live_camera/events")
        self.assertEqual(events_resp.status_code, 200)
        events_data = events_resp.get_json()
        self.assertEqual(events_data["threshold"], 0.80)

        # Clear events
        clear_resp = self.client.post("/api/live_camera/clear")
        self.assertEqual(clear_resp.status_code, 200)
        self.assertEqual(clear_resp.get_json()["status"], "success")


if __name__ == "__main__":
    unittest.main()

