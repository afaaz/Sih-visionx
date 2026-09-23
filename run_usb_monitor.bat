@echo off
title ForensicLens Live USB Forensic Monitor
echo =========================================================================
echo  Starting ForensicLens Live USB Forensic Monitor (SIH PS 26150)
echo =========================================================================
set PYTHONPATH=.
python run_usb_monitor.py
pause
