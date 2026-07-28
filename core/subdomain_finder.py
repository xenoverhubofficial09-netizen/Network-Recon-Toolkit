import socket
import time
import requests


def find_subdomains(domain):

    start = time.time()

    url = f"https://crt.sh/?q=%.{domain}&output=json"

    headers = {
        "User-Agent": "NetworkReconToolkit/1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        raise Exception("crt.sh request failed.")

    try:
        data = response.json()
    except Exception:
        raise Exception("Unable to parse crt.sh response.")

    found = set()

    for item in data:

        value = item.get("name_value", "")

        for sub in value.split("\n"):

            sub = sub.strip().lower()

            if "*" in sub:
                continue

            if sub.endswith(domain):
                found.add(sub)

    results = []

    for subdomain in sorted(found):

        try:

            ip = socket.gethostbyname(subdomain)

            results.append((subdomain, ip))

        except Exception:
            pass

    scan_time = round(time.time() - start, 2)

    return results, scan_time