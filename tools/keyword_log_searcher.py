"""
Tool: Log File Keyword Searcher
Author: PatrickWorthey
Description:
    This script allows the user to search a .log or .txt file for one or more
    user-defined keywords. It uses a GUI file picker and prints matching lines
    with line numbers. Great for quick triage during investigations.

Features:
    - Case-insensitive keyword search
    - Supports multiple keywords (comma-separated)
    - Easy file selection via tkinter GUI
    - Outputs matching lines with line numbers

Example:
    Enter keywords such as : admin, error, failed, attachment
    
    If any of the entered keywords match, user can expect an output such as the following when searching for 'attachment':
    "[Line 4] 1. Select the form from the attachment index listing."
Dependencies:
    - Standard Library only (tkinter included with Python)

"""

import os
from tkinter import Tk, filedialog

def choose_log_file():
    """Open a file dialog for the user to select a log or text file."""
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(
        title="Select a log or text file",
        filetypes=[("Text files", "*.log *.txt")]
    )
    return file_path

def search_keywords_in_file(file_path, keywords):
    """Search each line of the file for any of the provided keywords."""
    print(f"\n Searching for keywords: {', '.join(keywords)}\n" + "-" * 50)          # Print to user to show what term(s) are being searched

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line_number, line in enumerate(file, start=1):
                if any(keyword.lower() in line.lower() for keyword in keywords):     # Allows user input and doucment searched to be case insensitive
                    print(f"[Line {line_number}] {line.strip()}")                    # Prints line number within document followed by line containing text
    except Exception as e:
        print(f"[!] Error reading file: {e}")

def main():
    print("Log File Keyword Searcher\n")
    file_path = choose_log_file()

    if not file_path:
        print("No file selected. Exiting.")
        return

    user_input = input("Enter keywords to search for (comma-separated): ")
    keywords = [kw.strip() for kw in user_input.split(",") if kw.strip()]

    if not keywords:
        print("No valid keywords entered. Exiting.")
        return

    search_keywords_in_file(file_path, keywords)

if __name__ == "__main__":
    main()
