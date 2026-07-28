import socket
import requests


API_URL = "http://ip-api.com/json/"


def asn_lookup(target: str) -> dict:
    """
    Lookup ASN information for a domain or IP.

    Returns:
        dict
    """

    ip = socket.gethostbyname(target)

    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except Exception:
        hostname = "N/A"

    response = requests.get(
        f"{API_URL}{ip}",
        timeout=5
    )

    data = response.json()

    if data.get("status") != "success":
        raise Exception("Unable to retrieve ASN information.")

    asn_data = data.get("as", "N/A")

    if asn_data != "N/A" and " " in asn_data:
        asn, organization = asn_data.split(" ", 1)
    else:
        asn = asn_data
        organization = "N/A"

    return {
        "target": target,
        "ip": ip,
        "hostname": hostname,
        "asn": asn,
        "organization": organization,
        "isp": data.get("isp", "N/A"),
        "country": data.get("country", "N/A"),
    }