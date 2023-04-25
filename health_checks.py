#!/usr/bin/env python3
"""Checks the health of a system"""

import shutil
import psutil

def check_disk_usage(disk) -> bool:
    """Checks amount of free disk space available
    Returns a boolean value"""
    disk_usage = shutil.disk_usage(disk)
    free = disk_usage.free / disk_usage.total * 100
    return free > 20

def check_cpu_usage() -> bool:
    """Checks the percentage of processor in use.
    Returns a boolean value."""
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is okay")
