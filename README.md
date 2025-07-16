# Python for Security Analysts

A collection of Python scripts built to support real-world cybersecurity workflows — with a focus on DFIR, automation, triage, and investigation.

This repository is designed for analysts, investigators, and engineers who want tools they can adapt to their own environments. The code here addresses problems encountered in practical blue team work, from log review to file analysis to evidence enrichment.

---

## Tools Included

| Tool | Description | Link |
|------|-------------|------|
| **WHOIS Lookup** | Query domain registration information (registrar, dates, contacts). | [whois_lookup.py](tools/whois_lookup.py) |
| **File Hash Calculator** | Compute MD5, SHA1, and SHA256 hashes for integrity checks. | [file_hash_calculator.py](tools/file_hash_calculator.py) |
| **Metadata Extractor (EXIF)** | Extract EXIF data from image files: GPS, timestamps, device info. | [metadata_extractor.py](tools/metadata_extractor.py) |
| **Log Keyword Searcher** | Search `.log` or `.txt` files for custom keywords like "error", "admin", or IOCs. | [keyword_log_searcher.py](tools/keyword_log_searcher.py) |
| **Base64 / ROT13 Decoder** | Decode common encodings often used in malware, kits, or CTFs. | [base64_rot13_decoder.py](tools/base64_rot13_decoder.py) |
| **Triage File Info Lister** | Recursively list files with size, type, and timestamps for evidence collection. | _In Progress_ |
| **URL/IP Extractor** | Parse text or clipboard for domains, URLs, and IPs. Useful for phishing triage. | _In Progress_ |
| **Chrome History Parser** | Read and parse Chrome SQLite history to extract URLs and visit timestamps. | _In Progress_ |
| **Timestamp Converter** | Convert between UNIX/Epoch and human-readable time for log correlation. | _In Progress_ |
| **Memory String Finder** | Scan raw `.bin` or `.dmp` files for keywords like "mimikatz" or "powershell". | _In Progress_ |

---

## How to Use

You can run these tools locally with minimal setup.

### Option 1: Download and Run
1. Click the green **Code** button → **Download ZIP**
2. Unzip the folder
3. Open any `.py` file in your Python editor (VS Code, PyCharm, IDLE, etc.)

### Option 2: Clone the Repository
```bash
git clone https://github.com/PatrickWorthey/python-for-security-analysts.git
cd python-for-security-analysts
```
