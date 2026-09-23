"""ForensicLens Live USB & Removable Media Forensic Monitor Runner.

Executable standalone backend script to run real-time USB storage discovery,
kernel filesystem watchdog monitoring, cryptographic SHA-256 integrity hashing,
and Section 65B forensic audit ledger tracking directly from the terminal.

Usage:
    python run_usb_monitor.py                     # Run live real-time monitoring
    python run_usb_monitor.py --simulate          # Run automated USB demo simulation
    python run_usb_monitor.py --watch-path <dir>  # Watch a custom local drive/folder
    python run_usb_monitor.py --export-md out.md  # Export audit report upon exit
    python run_usb_monitor.py --export-json out.json
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure project root is importable
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from forensiclens.usb_monitor import main

if __name__ == "__main__":
    main()
