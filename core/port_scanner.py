import socket
import time
from concurrent.futures import ThreadPoolExecutor

from utils.common_ports import COMMON_PORTS


def grab_banner(host, port):
    """
    Grab service banner from an open port.
    """

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            sock.connect((host, port))

            if port == 80:
                request = (
                    f"HEAD / HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"User-Agent: NetworkReconToolkit\r\n"
                    f"Connection: close\r\n\r\n"
                )
                sock.send(request.encode())

            banner = sock.recv(1024).decode(errors="ignore").strip()

            banner = banner.replace("\r", " ").replace("\n", " ")

            return banner[:100]

    except Exception:
        return ""


def scan_port(host, port):
    """
    Scan one TCP port.

    Returns:
        (port, service, banner)

    Returns None if the port is closed.
    """

    service = COMMON_PORTS.get(port, "Unknown")

    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.settimeout(1)

            if sock.connect_ex((host, port)) == 0:

                banner = grab_banner(host, port)

                return (port, service, banner)

    except Exception:
        pass

    return None


def scan_host(host):
    """
    Scan common TCP ports.

    Returns:
        ip
        results
        scan_time
    """

    ip = socket.gethostbyname(host)

    start = time.time()

    ports = sorted(COMMON_PORTS.keys())

    results = []

    with ThreadPoolExecutor(max_workers=100) as executor:

        futures = [executor.submit(scan_port, ip, port) for port in ports]

        for future in futures:

            result = future.result()

            if result:
                results.append(result)

    scan_time = round(time.time() - start, 2)

    return ip, results, scan_time