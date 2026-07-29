import socket
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib3.exceptions import InsecureRequestWarning
import urllib3

urllib3.disable_warnings(InsecureRequestWarning)

HEADERS = {
    "User-Agent": "NetworkReconToolkit/2.0"
}

DNS_CACHE = {}


def verify_host(subdomain, wildcard_enabled=False, wildcard_ip=None):

    #
    # DNS Resolve
    #

    try:

        if subdomain in DNS_CACHE:

            ip = DNS_CACHE[subdomain]

        else:

            ip = socket.gethostbyname(subdomain)

            DNS_CACHE[subdomain] = ip

    except Exception:

        return {
            "host": subdomain,
            "status": "UNVERIFIED",
            "reason": "DNS Failed",
            "ip": "-"
        }

    #
    # Wildcard Detection
    #

    if wildcard_enabled and wildcard_ip:

        if ip == wildcard_ip:

            return {
                "host": subdomain,
                "status": "UNVERIFIED",
                "reason": "Wildcard DNS",
                "ip": ip
            }

    #
    # HTTPS Check
    #

    try:

        response = requests.get(

            f"https://{subdomain}",

            headers=HEADERS,

            timeout=3,

            allow_redirects=True,

            verify=False

        )

        title = ""

        if "<title>" in response.text.lower():

            try:

                title = response.text.lower().split("<title>")[1].split("</title>")[0][:60]
            except Exception:
                title = ""

        return {
            "host": subdomain,
            "status": "VERIFIED",
            "reason": f"HTTPS {response.status_code}",
            "ip": ip,
            "server": response.headers.get("Server", "-"),
            "title": title
        }

    except Exception:
        pass

    #
    # HTTP Check
    #

    try:

        response = requests.get(

            f"http://{subdomain}",

            headers=HEADERS,

            timeout=3,

            allow_redirects=True

        )

        title = ""

        if "<title>" in response.text.lower():

            try:

                title = response.text.lower().split("<title>")[1].split("</title>")[0][:60]
            except Exception:
                title = ""

        return {
            "host": subdomain,
            "status": "VERIFIED",
            "reason": f"HTTP {response.status_code}",
            "ip": ip,
            "server": response.headers.get("Server", "-"),
            "title": title
        }

    except Exception:

        return {
            "host": subdomain,
            "status": "UNVERIFIED",
            "reason": "No HTTP Response",
            "ip": ip
        }


def verify_subdomains(

    subdomains,

    wildcard_enabled=False,

    wildcard_ip=None,

    workers=200

):

    verified = []

    unverified = []

    with ThreadPoolExecutor(max_workers=workers) as executor:

        futures = [

            executor.submit(

                verify_host,

                sub,

                wildcard_enabled,

                wildcard_ip

            )

            for sub in subdomains

        ]

        for future in as_completed(futures):

            result = future.result()

            if result["status"] == "VERIFIED":

                verified.append(result)

            else:

                unverified.append(result)

    verified.sort(key=lambda x: x["host"])

    unverified.sort(key=lambda x: x["host"])

    return verified, unverified