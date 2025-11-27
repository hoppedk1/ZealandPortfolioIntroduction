#!/usr/bin/env python3

import socket
import argparse
import re
import sys

def main():
    # -------------------------------
    # Argument parser
    # -------------------------------
    parser = argparse.ArgumentParser(description="Banner Grabber with Vulnerability Matching")
    parser.add_argument("--target", required=True, help="Target IP or hostname")
    parser.add_argument("--port", required=True, type=int, help="Target port")
    args = parser.parse_args()

    # -------------------------------
    # Load vulnerable banners
    # -------------------------------
    try:
        with open("vulnbanners.txt", "r", encoding="utf-8") as file:
            vulnbanners = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("[!] Error: vulnbanners.txt not found.")
        sys.exit(1)

    # -------------------------------
    # Set up socket
    # -------------------------------
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    print(f"[+] Connecting to {args.target}:{args.port} ...")

    try:
        sock.connect((args.target, args.port))
    except socket.timeout:
        print("[!] Connection timed out.")
        sys.exit(1)
    except socket.error as e:
        print(f"[!] Socket error: {e}")
        sys.exit(1)

    # -------------------------------
    # Build proper HTTP Request
    # -------------------------------
    request = (
        "GET / HTTP/1.1\r\n"
        f"Host: {args.target}\r\n"
        "User-Agent: BannerGrabber/1.0\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    try:
        sock.sendall(request.encode("utf-8"))
    except socket.error as e:
        print(f"[!] Failed to send request: {e}")
        sys.exit(1)

    # -------------------------------
    # Receive data
    # -------------------------------
    try:
        response = sock.recv(2048)
    except socket.timeout:
        print("[!] Timeout receiving data.")
        sys.exit(1)
    except socket.error as e:
        print(f"[!] Error receiving data: {e}")
        sys.exit(1)
    finally:
        sock.close()

    # -------------------------------
    # Decode response
    # -------------------------------
    try:
        decoded = response.decode("utf-8", errors="replace")
    except Exception:
        print("[!] Could not decode server response.")
        decoded = str(response)

    print("\n===== Raw Server Response =====")
    print(decoded)
    print("================================\n")

    # -------------------------------
    # Extract headers and highlight Server:
    # -------------------------------
    print("===== Parsed Headers =====")

    for line in decoded.splitlines():
        if line.lower().startswith("server:"):
            print(f"***** {line} *****")
        else:
            print(line)

    print("===============================\n")

    # -------------------------------
    # Vulnerability Banner Matching
    # -------------------------------
    for vulnbanner in vulnbanners:
        if vulnbanner.lower() in decoded.lower():
            print("[!!!] VULNERABLE SERVER DETECTED!")
            print("       Matched banner :", vulnbanner)
            print("       Target         :", args.target)
            print("       Port           :", args.port)
            print()
            break  # Only report first match

if __name__ == "__main__":
    main()
