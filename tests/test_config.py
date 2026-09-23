"""Tests for ForensicLens Configuration System."""

import json
import unittest
from pathlib import Path

import config
from config import AppConfig, Config, ServerConfig, PathsConfig, LiveCameraConfig
from forensiclens.config import config as pkg_config


class ConfigTests(unittest.TestCase):
    def test_default_config_values(self) -> None:
        """Verify standard system default configuration values."""
        cfg = AppConfig()
        self.assertEqual(cfg.server.port, 5000)
        self.assertEqual(cfg.server.host, "127.0.0.1")
        self.assertEqual(cfg.live_camera.confidence_threshold, 0.80)
        self.assertEqual(cfg.live_camera.threshold_percentage, "80%")
        self.assertEqual(cfg.compliance.timezone_name, "Asia/Kolkata")
        self.assertEqual(cfg.compliance.hash_algorithm, "SHA-256")

    def test_config_json_file_exists_and_valid(self) -> None:
        """Verify config.json exists in root and is valid JSON."""
        json_path = Path("config.json")
        self.assertTrue(json_path.is_file(), "config.json must exist in project root")

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("server", data)
        self.assertIn("paths", data)
        self.assertIn("live_camera", data)
        self.assertIn("compliance", data)
        self.assertEqual(data["live_camera"]["confidence_threshold"], 0.80)
        self.assertEqual(data["server"]["port"], 5000)

    def test_config_load_and_save_json(self) -> None:
        """Verify AppConfig load_json and save_json methods."""
        loaded = AppConfig.load_json("config.json")
        self.assertEqual(loaded.server.port, 5000)
        self.assertEqual(loaded.live_camera.confidence_threshold, 0.80)
        d = loaded.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["server"]["port"], 5000)

    def test_package_config_import(self) -> None:
        """Verify forensiclens.config import matches root config."""
        self.assertEqual(pkg_config.server.port, config.config.server.port)
        self.assertEqual(pkg_config.live_camera.confidence_threshold, 0.80)

    def test_dot_config_file_exists_and_valid(self) -> None:
        """Verify .config file exists in project root and is valid INI/properties format."""
        import configparser
        dot_config_path = Path(".config")
        self.assertTrue(dot_config_path.is_file(), ".config file must exist in project root")

        parser = configparser.ConfigParser()
        parsed = parser.read(dot_config_path, encoding="utf-8")
        self.assertTrue(len(parsed) > 0, ".config must be successfully parsed")
        self.assertIn("server", parser)
        self.assertIn("paths", parser)
        self.assertIn("video_intelligence", parser)
        self.assertIn("live_camera", parser)
        self.assertIn("compliance", parser)
        self.assertEqual(parser.get("server", "port"), "5000")
        self.assertEqual(parser.get("server", "host"), "127.0.0.1")
        self.assertEqual(parser.get("live_camera", "confidence_threshold"), "0.80")
        self.assertEqual(parser.get("compliance", "hash_algorithm"), "SHA-256")


if __name__ == "__main__":
    unittest.main()

