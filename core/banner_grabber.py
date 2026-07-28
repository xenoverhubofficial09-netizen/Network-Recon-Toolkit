import socket
import ssl

from utils.common_ports import COMMON_PORTS


TIMEOUT = 3


def resolve_host(host: str) -> tuple[str, str]:
    """
    Resolve hostname to IP.

    Returns:
        (hostname, ip_address)
    """

    host = host.strip()

    ip = socket.gethostbyname(host)

    return host, ip


def get_service_name(port: int) -> str:
    """
    Return service name from common ports.
    """

    return COMMON_PORTS.get(port, "Unknown")


def _http_banner(sock: socket.socket, host: str) -> str:

    request = (
        f"HEAD / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: NetworkReconToolkit\r\n"
        f"Connection: close\r\n\r\n"
    )

    sock.sendall(request.encode())

    return sock.recv(4096).decode(errors="ignore")


def _tcp_banner(sock: socket.socket) -> str:

    return sock.recv(4096).decode(errors="ignore")


def grab_banner(host: str, port: int) -> dict:
    """
    Grab banner from a TCP service.

    Returns:
        {
            success,
            host,
            ip,
            port,
            service,
            banner,
            error
        }
    """

    result = {
        "success": False,
        "host": "",
        "ip": "",
        "port": port,
        "service": "",
        "banner": "",
        "error": ""
    }

    try:

        hostname, ip = resolve_host(host)

        result["host"] = hostname
        result["ip"] = ip
        result["service"] = get_service_name(port)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)

        sock.connect((ip, port))

        if port in (443, 8443):

            context = ssl.create_default_context()

            sock = context.wrap_socket(
                sock,
                server_hostname=hostname
            )

        if port in (80, 8080, 8000):

            banner = _http_banner(sock, hostname)

        else:

            banner = _tcp_banner(sock)

        sock.close()

        banner = banner.replace("\r", "")
        banner = banner.replace("\n", "\n")

        banner = banner.strip()

        if not banner:
            banner = "No banner received."

        result["banner"] = banner
        result["success"] = True

    except socket.gaierror:

        result["error"] = "Unable to resolve hostname."

    except TimeoutError:

        result["error"] = "Connection timed out."

    except ConnectionRefusedError:

        result["error"] = "Connection refused."

    except Exception as e:

        result["error"] = str(e)

    return result