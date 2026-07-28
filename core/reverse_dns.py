import socket


def reverse_dns_lookup(target):
    """
    Perform Reverse DNS lookup.

    Returns:
        dict
    """

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        raise Exception("Unable to resolve target.")

    try:
        hostname, aliases, addresses = socket.gethostbyaddr(ip)
    except socket.herror:
        hostname = "N/A"
        aliases = []
        addresses = [ip]

    return {
        "target": target,
        "ip": ip,
        "hostname": hostname,
        "aliases": aliases,
        "addresses": addresses,
    }