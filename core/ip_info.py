import socket
import requests


def get_ip_information(target):

    ip = socket.gethostbyname(target)

    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except Exception:
        hostname = "N/A"

    url = f"http://ip-api.com/json/{ip}"

    response = requests.get(url, timeout=5)

    data = response.json()

    if data.get("status") != "success":
        raise Exception("Unable to retrieve IP information.")

    return {
        "target": target,
        "ip": ip,
        "hostname": hostname,
        "country": data.get("country", "N/A"),
        "region": data.get("regionName", "N/A"),
        "city": data.get("city", "N/A"),
        "zip": data.get("zip", "N/A"),
        "lat": data.get("lat", "N/A"),
        "lon": data.get("lon", "N/A"),
        "timezone": data.get("timezone", "N/A"),
        "isp": data.get("isp", "N/A"),
        "org": data.get("org", "N/A"),
        "asn": data.get("as", "N/A"),
    }