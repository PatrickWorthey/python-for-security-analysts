"""
Tool: Base64 & ROT13 Decoder
Author: PatrickWorthey
Description:
    This tool decodes strings encoded in either Base64 or ROT13.
    The user is prompted to enter an encoded string and select the decoding method.
    Results are printed to the console. Errors are handled and displayed if decoding fails.

Dependencies:
    No external packages required (uses built-in Python libraries)
"""

import base64
import codecs

def decode_base64(data: str) -> str:
    try:
        return base64.b64decode(data).decode('utf-8')
    except Exception as e:
        return f"[!] Base64 decoding failed: {e}"

def decode_rot13(data: str) -> str:
    try:
        return codecs.decode(data, 'rot_13')
    except Exception as e:
        return f"[!] ROT13 decoding failed: {e}"

def main():
    print("=== Base64 / ROT13 Decoder ===\n")
    encoded_str = input("Enter the encoded string: ").strip()
    print("\nChoose decoding method:")                # Give users a selection instead of having to type
    print("1 - Base64")
    print("2 - ROT13")
    print("3 - Cancel")

    choice = input("Select [1, 2, or 3]: ").strip()

    if choice == "1":
        decoded = decode_base64(encoded_str)
        print(f"\n[Decoded Base64]\n{decoded}")
    elif choice == "2":
        decoded = decode_rot13(encoded_str)
        print(f"\n[Decoded ROT13]\n{decoded}")
    elif choice == "3":                               # Give user a way to exit
        print("[!] Exiting.")
    else:
        print("[!] Invalid selection. Exiting.")

if __name__ == "__main__":
    main()
