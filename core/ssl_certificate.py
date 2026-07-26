import socket
import ssl
from datetime import datetime


def get_ssl_certificate(host):
    """
    Fetch SSL Certificate Information.

    Returns:
        ip
        issuer
        subject
        valid_from
        valid_until
        days_remaining
    """

    ip = socket.gethostbyname(host)

    context = ssl.create_default_context()

    with socket.create_connection((host, 443), timeout=5) as sock:

        with context.wrap_socket(sock, server_hostname=host) as secure_sock:

            cert = secure_sock.getpeercert()

    subject = dict(x[0] for x in cert["subject"])

    issuer = dict(x[0] for x in cert["issuer"])

    valid_from = datetime.strptime(
        cert["notBefore"],
        "%b %d %H:%M:%S %Y %Z"
    )

    valid_until = datetime.strptime(
        cert["notAfter"],
        "%b %d %H:%M:%S %Y %Z"
    )

    days_remaining = (valid_until - datetime.utcnow()).days

    return (
        ip,
        subject.get("commonName", "Unknown"),
        issuer.get("commonName", "Unknown"),
        valid_from.strftime("%Y-%m-%d"),
        valid_until.strftime("%Y-%m-%d"),
        days_remaining
    )