import platform
import socket
import subprocess
import time


def traceroute(host: str) -> dict:
    """
    Perform a traceroute to the specified host.
    """

    try:
        ip = socket.gethostbyname(host)

    except socket.gaierror:
        return {
            "success": False,
            "message": "Invalid domain or IP address."
        }

    system = platform.system().lower()

    if system == "windows":
        command = ["tracert", "-d", host]
    else:
        command = ["traceroute", "-n", host]

    start = time.perf_counter()

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=120
        )

    except FileNotFoundError:

        return {
            "success": False,
            "message": "Traceroute command not found."
        }

    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "message": "Traceroute timed out."
        }

    elapsed = round(time.perf_counter() - start, 2)

    return {
        "success": True,
        "host": host,
        "ip": ip,
        "output": result.stdout,
        "scan_time": elapsed,
    }