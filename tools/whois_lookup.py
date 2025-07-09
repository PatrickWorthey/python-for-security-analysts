"""
Tool: Simple WHOIS Lookup Tool
Author: 0xPithyTrace
Description:
    This script takes a domain name as input and returns key WHOIS registration
    details. Designed for beginner-friendly use in domain enrichment workflows.

Usage:
    python tools/whois_lookup.py

Requirements:
    pip install python-whois
"""

import re
import whois


def is_valid_domain(domain_name: str) -> bool:
    """
    Validates that the domain input appears to follow standard format.
    Example: example.com, my-site.org, sub.domain.co.uk
    """
    domain_pattern = r"^(?!-)[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(domain_pattern, domain_name) is not None


def lookup_domain(domain_name: str) -> None:
    """
    Performs a WHOIS lookup on the given domain and prints key fields.
    """
    try:
        print(f"\n[+] Looking up WHOIS for: {domain_name}")
        whois_data = whois.whois(domain_name)

        print("\n--- WHOIS Information ---")
        print(f"Domain Name:     {whois_data.domain_name}")
        print(f"Registrar:       {whois_data.registrar}")
        print(f"Creation Date:   {whois_data.creation_date}")
        print(f"Expiration Date: {whois_data.expiration_date}")
        print(f"Emails:          {whois_data.emails}")
        print(f"Name Servers:    {whois_data.name_servers}")

    except Exception as error:
        print(f"\n[!] Error retrieving WHOIS information: {error}")


if __name__ == "__main__":
    user_input = input("Enter a domain (e.g., example.com): ").strip()

    if not user_input:
        print("[!] No domain entered. Exiting.")
    elif not is_valid_domain(user_input):
        print("[!] Invalid domain format. Please enter a valid domain like example.com.")
    else:
        lookup_domain(user_input)

