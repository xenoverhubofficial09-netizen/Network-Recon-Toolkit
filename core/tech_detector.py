import requests
import socket


HEADERS = {
    "User-Agent": "NetworkReconToolkit"
}


TECH_SIGNATURES = {
    "wordpress": "WordPress",
    "wp-content": "WordPress",
    "wp-json": "WordPress",

    "shopify": "Shopify",

    "drupal": "Drupal",

    "joomla": "Joomla",

    "laravel": "Laravel",

    "django": "Django",

    "react": "React",

    "next": "Next.js",

    "vue": "Vue.js",

    "angular": "Angular",

    "bootstrap": "Bootstrap",

    "cloudflare": "Cloudflare",

    "nginx": "Nginx",

    "apache": "Apache",
}


def detect_technology(host):

    ip = socket.gethostbyname(host)

    urls = [
        f"https://{host}",
        f"http://{host}"
    ]

    for url in urls:

        try:

            response = requests.get(
                url,
                timeout=8,
                headers=HEADERS
            )

            headers = dict(response.headers)

            html = response.text.lower()

            detected = set()

            server = headers.get("Server", "")

            powered = headers.get("X-Powered-By", "")

            cookies = response.cookies

            for key, value in TECH_SIGNATURES.items():

                if key in html:
                    detected.add(value)

                if key.lower() in server.lower():
                    detected.add(value)

                if key.lower() in powered.lower():
                    detected.add(value)

            return {
                "ip": ip,
                "url": response.url,
                "server": server,
                "powered": powered,
                "headers": headers,
                "cookies": cookies,
                "technology": sorted(detected)
            }

        except requests.RequestException:
            continue

    raise Exception("Unable to connect to target.")