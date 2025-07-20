"""
Tool: Triage File Info Lister
Author: PatrickWorthey
Description:
    This script prompts the user to select a folder and then recursively scans it,
    listing file information including path, size, creation time, and modified time.

    Designed for digital forensics triage, evidence review, or file metadata snapshots.

Dependencies:
    Built-in: os, datetime, tkinter
"""

import os
import datetime
import tkinter as tk
from tkinter import filedialog

def format_time(epoch_time):
    """Convert epoch time to human-readable format."""
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')

def list_file_info(directory: str):
    """Recursively walk a directory and print file metadata."""
    if not os.path.isdir(directory):
        print(f"[!] Error: '{directory}' is not a valid directory.")
        return

    print(f"\nScanning directory: {directory}\n")

    for root, _, files in os.walk(directory):
        for file in files:
            try:
                full_path = os.path.join(root, file)
                size_kb = os.path.getsize(full_path) / 1024
                created = os.path.getctime(full_path)
                modified = os.path.getmtime(full_path)

                print(f"Path:     {full_path}")
                print(f"Size:     {size_kb:.2f} KB")
                print(f"Created:  {format_time(created)}")
                print(f"Modified: {format_time(modified)}")
                print("-" * 60)

            except Exception as e:
                print(f"[!] Failed to process file: {file} — {e}")

def choose_directory():
    """Open a file picker window to select a folder."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select folder to scan")
    return folder_path

def main():
    print("=== Triage File Info Lister ===\n")
    target_dir = choose_directory()

    if not target_dir:
        print("[!] No folder selected. Exiting.")
        return

    list_file_info(target_dir)

if __name__ == "__main__":
    main()
