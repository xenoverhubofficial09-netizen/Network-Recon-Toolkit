import requests
import socket


def get_http_headers(host):
    """
    Fetch HTTP/HTTPS response headers.
    Returns:
        ip
        url
        headers
    """

    ip = socket.gethostbyname(host)

    urls = [
        f"https://{host}",
        f"http://{host}"
    ]

    for url in urls:

        try:

            response = requests.get(
                url,
                timeout=5,
                allow_redirects=True,
                headers={
                    "User-Agent": "NetworkReconToolkit"
                }
            )

            return (
                ip,
                response.url,
                dict(response.headers)
            )

        except requests.RequestException:
            continue

    raise Exception("Unable to connect to target.")