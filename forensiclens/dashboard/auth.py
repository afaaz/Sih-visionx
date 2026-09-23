"""ForensicLens Investigator Authentication & User Management.

Provides cryptographically hashed user credential storage, investigator session validation,
and compliance with forensic chain of custody attribution (ISO/IEC 27037).
"""

from __future__ import annotations

import hashlib
import json
import os
import secrets
from pathlib import Path
from typing import Any


DEFAULT_INVESTIGATORS: list[dict[str, Any]] = [
    {
        "id": "inv-001",
        "email": "investigator@cbi.gov.in",
        "name": "Insp. A. K. Sharma",
        "badge_id": "IND-26150",
        "agency": "Central Bureau of Investigation (CBI) - Cyber Crime Division",
        "clearance": "Level 3 - Lead Forensic Examiner (Sec 65B Certifier)",
        "role": "investigator",
        "salt": "a8f3b2c1d0e94a5b6c7d8e9f0a1b2c3d",
        # Default password is: Investigator@2026
        "password_hash": hashlib.pbkdf2_hmac(
            "sha256",
            "Investigator@2026".encode("utf-8"),
            bytes.fromhex("a8f3b2c1d0e94a5b6c7d8e9f0a1b2c3d"),
            100_000,
        ).hex(),
        "created_at": "2026-08-30T10:00:00Z",
        "is_active": True,
    },
    {
        "id": "usr-002",
        "email": "user@forensiclens.gov.in",
        "name": "Operator P. Patel",
        "badge_id": "CAM-26150",
        "agency": "CCTV Control Room - Field Surveillance Unit",
        "clearance": "Field Surveillance Operator",
        "role": "user_investigator",
        "salt": "b7c2d1e0f9a8b6c5d4e3f2a1b0c9d8e7",
        # Default password is: User@2026
        "password_hash": hashlib.pbkdf2_hmac(
            "sha256",
            "User@2026".encode("utf-8"),
            bytes.fromhex("b7c2d1e0f9a8b6c5d4e3f2a1b0c9d8e7"),
            100_000,
        ).hex(),
        "created_at": "2026-09-23T00:00:00Z",
        "is_active": True,
    },
]


class AuthManager:
    """Manages investigator credentials and access control with local persistence."""

    def __init__(self, storage_path: Path | str = "reports/investigators.json") -> None:
        self.storage_path = Path(storage_path)
        self._ensure_storage()

    def _ensure_storage(self) -> None:
        """Initialize the investigators storage file with default demo lead and user investigator."""
        if not self.storage_path.exists():
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            self._save_users(DEFAULT_INVESTIGATORS)
        else:
            # Ensure both default investigator and default user investigator accounts exist
            users = self._load_users()
            user_emails = {u.get("email", "").strip().lower() for u in users}
            updated = False
            for default_user in DEFAULT_INVESTIGATORS:
                if default_user["email"].strip().lower() not in user_emails:
                    users.append(default_user)
                    updated = True
            if updated:
                self._save_users(users)

    def _load_users(self) -> list[dict[str, Any]]:
        try:
            with self.storage_path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return list(DEFAULT_INVESTIGATORS)

    def _save_users(self, users: list[dict[str, Any]]) -> None:
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with self.storage_path.open("w", encoding="utf-8") as f:
            json.dump(users, f, indent=2, ensure_ascii=False)

    def _hash_password(self, password: str, salt: str) -> str:
        return hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(salt),
            100_000,
        ).hex()

    def authenticate(self, identifier: str, password: str) -> dict[str, Any] | None:
        """Authenticate an investigator or user investigator by email or badge ID."""
        cleaned_id = identifier.strip().lower()
        users = self._load_users()
        for user in users:
            if not user.get("is_active", True):
                continue
            user_email = user.get("email", "").strip().lower()
            user_badge = user.get("badge_id", "").strip().lower()
            if cleaned_id in (user_email, user_badge):
                salt = user.get("salt", "")
                computed = self._hash_password(password, salt)
                if computed == user.get("password_hash"):
                    user_role = user.get("role")
                    if not user_role:
                        clearance_str = str(user.get("clearance", "")).lower()
                        user_role = "user_investigator" if ("surveillance" in clearance_str or "operator" in clearance_str) else "investigator"
                    return {
                        "id": user.get("id"),
                        "email": user.get("email"),
                        "name": user.get("name"),
                        "badge_id": user.get("badge_id"),
                        "agency": user.get("agency"),
                        "clearance": user.get("clearance"),
                        "role": user_role,
                    }
        return None

    def register(
        self,
        name: str,
        email: str,
        badge_id: str,
        password: str,
        agency: str = "Digital Forensics Unit",
        clearance: str = "Level 2 - Forensic Analyst",
        role: str = "investigator",
    ) -> dict[str, Any]:
        """Register a new investigator or user investigator."""
        name = name.strip()
        email = email.strip().lower()
        badge_id = badge_id.strip().upper()
        agency = agency.strip()
        clearance = clearance.strip()
        role = role.strip().lower()

        if "surveillance" in clearance.lower() or "user" in role or "surveillance" in role:
            resolved_role = "user_investigator"
        else:
            resolved_role = "investigator"

        if not name or len(name) < 2:
            raise ValueError("Full name must be at least 2 characters.")
        if not email or "@" not in email:
            raise ValueError("A valid email address is required.")
        if not badge_id or len(badge_id) < 2:
            if resolved_role == "user_investigator":
                badge_id = f"CAM-{secrets.token_hex(2).upper()}"
            else:
                raise ValueError("A valid Badge or Operator ID is required.")
        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters.")

        users = self._load_users()
        for u in users:
            if u.get("email", "").strip().lower() == email:
                raise ValueError(f"An account with email '{email}' already exists.")
            if u.get("badge_id", "").strip().upper() == badge_id:
                raise ValueError(f"An account with Badge ID '{badge_id}' already exists.")

        salt = secrets.token_hex(16)
        password_hash = self._hash_password(password, salt)

        prefix = "usr" if resolved_role == "user_investigator" else "inv"
        new_user = {
            "id": f"{prefix}-{secrets.token_hex(4)}",
            "email": email,
            "name": name,
            "badge_id": badge_id,
            "agency": agency or ("CCTV Surveillance Monitoring Cell" if resolved_role == "user_investigator" else "Digital Forensics Unit"),
            "clearance": clearance or ("Field Surveillance Operator" if resolved_role == "user_investigator" else "Level 2 - Forensic Analyst"),
            "role": resolved_role,
            "salt": salt,
            "password_hash": password_hash,
            "created_at": "2026-09-23T00:00:00Z",
            "is_active": True,
        }

        users.append(new_user)
        self._save_users(users)

        return {
            "id": new_user["id"],
            "email": new_user["email"],
            "name": new_user["name"],
            "badge_id": new_user["badge_id"],
            "agency": new_user["agency"],
            "clearance": new_user["clearance"],
            "role": new_user["role"],
        }

    def get_user_by_id(self, user_id: str) -> dict[str, Any] | None:
        """Fetch sanitized user details by ID."""
        for u in self._load_users():
            if u.get("id") == user_id:
                user_role = u.get("role")
                if not user_role:
                    clearance_str = str(u.get("clearance", "")).lower()
                    user_role = "user_investigator" if ("surveillance" in clearance_str or "operator" in clearance_str) else "investigator"
                return {
                    "id": u.get("id"),
                    "email": u.get("email"),
                    "name": u.get("name"),
                    "badge_id": u.get("badge_id"),
                    "agency": u.get("agency"),
                    "clearance": u.get("clearance"),
                    "role": user_role,
                }
        return None
