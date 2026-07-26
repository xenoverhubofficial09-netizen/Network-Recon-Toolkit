import platform
import re
import socket
import subprocess
from datetime import datetime

from utils.constants import (
    DEFAULT_TIMEOUT,
    ERROR_INVALID_HOST,
    ERROR_TIMEOUT,
    ERROR_UNREACHABLE,
    PING_COUNT,
)


def _build_command(host: str) -> list[str]:
    system = platform.system().lower()

    if system == "windows":
        return ["ping", "-n", str(PING_COUNT), host]

    return ["ping", "-c", str(PING_COUNT), host]


def _parse_ping_output(output: str) -> dict:
    data = {
        "latency": None,
        "ttl": None,
        "packets_sent": PING_COUNT,
        "packets_received": 0,
        "packets_lost": PING_COUNT,
        "packet_loss": "100%",
    }

    latency = re.search(r"time[=<]?\s*([\d.]+)", output, re.IGNORECASE)

    ttl = re.search(r"ttl[=\s:]*(\d+)", output, re.IGNORECASE)

    if latency:
        data["latency"] = f"{latency.group(1)} ms"

    if ttl:
        data["ttl"] = ttl.group(1)

    received = re.search(
        r"Received\s*=\s*(\d+)",
        output,
        re.IGNORECASE,
    )

    if received:
        packets = int(received.group(1))

        data["packets_received"] = packets
        data["packets_lost"] = PING_COUNT - packets

        if packets > 0:
            data["packet_loss"] = "0%"

    else:
        if "bytes from" in output.lower() or "reply from" in output.lower():
            data["packets_received"] = 1
            data["packets_lost"] = 0
            data["packet_loss"] = "0%"

    return data


def ping_host(host: str) -> dict:

    try:
        ip_address = socket.gethostbyname(host)

    except socket.gaierror:
        return {
            "success": False,
            "message": ERROR_INVALID_HOST,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    command = _build_command(host)

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=DEFAULT_TIMEOUT,
        )

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "message": ERROR_TIMEOUT,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    except Exception as error:
        return {
            "success": False,
            "message": str(error),
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    parsed = _parse_ping_output(result.stdout)

    if parsed["packets_received"] == 0:
        return {
            "success": False,
            "message": ERROR_UNREACHABLE,
            "host": host,
            "ip": ip_address,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    return {
        "success": True,
        "host": host,
        "ip": ip_address,
        "latency": parsed["latency"],
        "ttl": parsed["ttl"],
        "packets_sent": parsed["packets_sent"],
        "packets_received": parsed["packets_received"],
        "packets_lost": parsed["packets_lost"],
        "packet_loss": parsed["packet_loss"],
        "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }