"""
Robots.txt Analyzer Core Module

Responsible for fetching and analyzing robots.txt files.
"""

from urllib.parse import urljoin

import requests


USER_AGENT = "NetworkReconToolkit/1.0"


def normalize_url(target: str) -> str:
    """
    Normalize target URL.

    Args:
        target: Domain or URL.

    Returns:
        str: Normalized URL.
    """

    target = target.strip()

    if not target.startswith(("http://", "https://")):
        target = f"https://{target}"

    return target.rstrip("/")


def fetch_robots(target: str) -> dict:
    """
    Fetch and analyze robots.txt.

    Args:
        target: Target website.

    Returns:
        dict: Robots analysis result.
    """

    base_url = normalize_url(target)

    robots_url = urljoin(
        base_url + "/",
        "robots.txt"
    )

    try:
        response = requests.get(
            robots_url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": USER_AGENT
            },
        )

    except requests.exceptions.RequestException as error:
        raise Exception(
            f"Unable to fetch robots.txt: {error}"
        ) from error


    if response.status_code != 200:
        return {
            "url": robots_url,
            "status": "NOT FOUND",
            "status_code": response.status_code,
            "user_agents": [],
            "disallowed": [],
            "allowed": [],
            "sitemaps": [],
        }


    user_agents = []
    disallowed = []
    allowed = []
    sitemaps = []


    for line in response.text.splitlines():

        line = line.strip()

        if not line or line.startswith("#"):
            continue


        key, _, value = line.partition(":")

        key = key.lower().strip()
        value = value.strip()


        if key == "user-agent":
            user_agents.append(value)

        elif key == "disallow":
            if value:
                disallowed.append(value)

        elif key == "allow":
            if value:
                allowed.append(value)

        elif key == "sitemap":
            sitemaps.append(value)


    return {
        "url": response.url,
        "status": "FOUND",
        "status_code": response.status_code,
        "user_agents": user_agents,
        "disallowed": disallowed,
        "allowed": allowed,
        "sitemaps": sitemaps,
    }