#!/usr/bin/env python3

import requests

url = input("Enter URL or hostname: ").strip()

# Normalize input
if not url.startswith(("http://", "https://")):
    url = "http://" + url

# Try sending the request
try:
    response = requests.get(url, timeout=5)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
    exit(1)

# Print status code
print("\nStatus code:", response.status_code)

# Try to print JSON
try:
    print("\nJSON body:")
    print(response.json())
except ValueError:
    print("\nBody is not valid JSON.")

# Print headers
print("\nResponse headers:")
for k, v in response.headers.items():
    print(f"{k}: {v}")

print("\nRequest headers:")
for k, v in response.request.headers.items():
    print(f"{k}: {v}")
