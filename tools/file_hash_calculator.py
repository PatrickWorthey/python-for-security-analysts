"""
Tool: File Hash Calculator
Author: 0xPithyTrace
Description:
    This Python script calculates the hash value (MD5, SHA-1, SHA-256) of a file. 
    It's a fundamental tool for digital forensics and incident response (DFIR) to 
    verify file integrity or identify malicious files.

Usage:
    python tools/file_hash_calculator.py

Requirements:
    python 3.x
    Built-in modules: haslib, tkinter, time
"""

import hashlib
import time
from tkinter import Tk, filedialog

# Supported algorithms
algorithms = ['md5', 'sha1', 'sha256']

def calculate_hash(file_path, algorithm):
    """Calculate and return the hash of a file using the specified algorithm."""
    try:
        hash_func = getattr(hashlib, algorithm)()
        with open(file_path, "rb") as f:
            data = f.read()
            hash_func.update(data)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"[!] Error: {e}")
        return None

def main():
    # Display algorithm options
    print("Choose a hashing algorithm:")
    for i, algo in enumerate(algorithms, start=1):
        print(f"{i}. {algo.upper()}")

    # Get user choice
    try:
        choice = int(input("Enter the number of the algorithm: "))
        algorithm = algorithms[choice - 1]
    except (ValueError, IndexError):
        print("[!] Invalid selection.")
        return

    # Notify user before file picker opens
    print("\nA file selection window will now open. Please choose the file you want to hash.")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
        
    # Open file picker dialog
    Tk().withdraw()  # Hide the tkinter root window
    file_path = filedialog.askopenfilename(title="Select a file to hash") #Create popup window to choose the target file

    if not file_path:
        print("[!] No file selected.")
        return

    # Calculate and display the hash
    hash_value = calculate_hash(file_path, algorithm)
    if hash_value:
        print(f"\n{algorithm.upper()} hash of '{file_path}':\n{hash_value}")

if __name__ == "__main__":
    main()
