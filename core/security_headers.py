import requests


SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "Cross-Origin-Opener-Policy",
    "Cross-Origin-Embedder-Policy",
    "Cross-Origin-Resource-Policy",
    "X-XSS-Protection",
]


def normalize_url(target):
    """
    Normalize target into a valid URL.
    """

    target = target.strip()

    if not target.startswith(("http://", "https://")):
        target = f"https://{target}"

    return target


def analyze_security_headers(target):
    """
    Analyze HTTP Security Headers.

    Returns:
        dict
    """

    url = normalize_url(target)

    try:

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "NetworkReconToolkit/1.0"
            },
        )

    except requests.exceptions.SSLError:

        url = url.replace("https://", "http://", 1)

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "NetworkReconToolkit/1.0"
            },
        )

    headers = response.headers

    found = {}
    missing = []

    for header in SECURITY_HEADERS:

        if header in headers:
            found[header] = headers[header]
        else:
            missing.append(header)

    return {
        "url": response.url,
        "status_code": response.status_code,
        "server": headers.get("Server", "Unknown"),
        "found": found,
        "missing": missing,
    }