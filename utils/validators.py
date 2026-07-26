import ipaddress
import re


DOMAIN_REGEX = re.compile(
    r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)"
    r"(\.[A-Za-z0-9-]{1,63})+$"
)


def validate_host(host: str) -> bool:

    host = host.strip()

    if not host:
        return False

    try:
        ipaddress.ip_address(host)
        return True

    except ValueError:
        pass

    return bool(DOMAIN_REGEX.fullmatch(host))