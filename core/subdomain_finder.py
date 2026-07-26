import socket
import time
from concurrent.futures import ThreadPoolExecutor


WORDLIST = "utils/wordlists/subdomains.txt"


def check_subdomain(subdomain):

    try:

        ip = socket.gethostbyname(subdomain)

        return (subdomain, ip)

    except Exception:

        return None


def find_subdomains(domain):

    start = time.time()

    with open(WORDLIST, "r", encoding="utf-8") as file:

        words = [
            line.strip()
            for line in file
            if line.strip()
        ]

    targets = [
        f"{word}.{domain}"
        for word in words
    ]

    results = []

    with ThreadPoolExecutor(max_workers=200) as executor:

        futures = [
            executor.submit(check_subdomain, target)
            for target in targets
        ]

        for future in futures:

            result = future.result()

            if result:
                results.append(result)

    results.sort()

    scan_time = round(time.time() - start, 2)

    return results, scan_time