import socket
import requests


def detect_technology(host):
    """
    Detect common web technologies.

    Returns:
        ip
        server
        powered_by
        cms
        cdn
        technologies
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

            headers = response.headers
            html = response.text.lower()

            server = headers.get("Server", "Unknown")
            powered_by = headers.get("X-Powered-By", "Not Found")

            cms = "Not Detected"

            if "wp-content" in html or "wordpress" in html:
                cms = "WordPress"

            elif "joomla" in html:
                cms = "Joomla"

            elif "drupal" in html:
                cms = "Drupal"

            elif "shopify" in html:
                cms = "Shopify"

            elif "wix" in html:
                cms = "Wix"

            cdn = "Not Detected"

            if "cloudflare" in server.lower():
                cdn = "Cloudflare"

            elif headers.get("CF-RAY"):
                cdn = "Cloudflare"

            elif "akamai" in server.lower():
                cdn = "Akamai"

            elif "fastly" in server.lower():
                cdn = "Fastly"

            elif "cloudfront" in server.lower():
                cdn = "Amazon CloudFront"

            technologies = []

            if headers.get("Strict-Transport-Security"):
                technologies.append("HSTS")

            if headers.get("Content-Encoding") == "gzip":
                technologies.append("Gzip")

            if headers.get("Content-Encoding") == "br":
                technologies.append("Brotli")

            if response.raw.version == 11:
                technologies.append("HTTP/1.1")

            elif response.raw.version == 10:
                technologies.append("HTTP/1.0")

            return (
                ip,
                server,
                powered_by,
                cms,
                cdn,
                technologies
            )

        except requests.RequestException:
            continue

    raise Exception("Unable to connect to target.")