import ipaddress
import socket


def get_host_information(host: str) -> dict:
    """
    Retrieve basic host information.
    """

    try:
        ip_address = socket.gethostbyname(host)

        try:
            reverse_dns = socket.gethostbyaddr(ip_address)[0]
        except Exception:
            reverse_dns = "Not Available"

        ip = ipaddress.ip_address(ip_address)

        if ip.version == 4:
            version = "IPv4"
        else:
            version = "IPv6"

        if ip.is_private:
            address_type = "Private"
        else:
            address_type = "Public"

        return {
            "success": True,
            "host": host,
            "ip": ip_address,
            "reverse_dns": reverse_dns,
            "ip_version": version,
            "address_type": address_type,
        }

    except socket.gaierror:

        return {
            "success": False,
            "message": "Invalid domain or IP address.",
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error),
        }