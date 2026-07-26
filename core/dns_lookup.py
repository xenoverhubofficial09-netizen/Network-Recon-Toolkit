import socket


def get_ip_address(domain: str) -> str | None:
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None


def get_hostname(ip: str) -> str | None:
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        return None