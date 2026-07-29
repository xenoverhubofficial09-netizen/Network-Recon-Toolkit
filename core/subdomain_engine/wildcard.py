import random
import string
import socket


def random_host(domain):

    token = "".join(

        random.choice(string.ascii_lowercase)

        for _ in range(20)

    )

    return f"{token}.{domain}"


def wildcard_detect(domain):

    host = random_host(domain)

    try:

        ip = socket.gethostbyname(host)

        return True, ip

    except Exception:

        return False, None