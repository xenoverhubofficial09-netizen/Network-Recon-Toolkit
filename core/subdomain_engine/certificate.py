import requests

HEADERS = {
    "User-Agent": "NetworkReconToolkit/1.0"
}


def from_crtsh(domain):
    """
    Fetch subdomains from crt.sh
    Returns: set()
    """

    results = set()

    try:

        url = f"https://crt.sh/?q=%.{domain}&output=json"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=8
        )

        if response.status_code != 200:
            return results

        data = response.json()

        for item in data:

            names = item.get("name_value", "")

            for sub in names.split("\n"):

                sub = sub.strip().lower()

                if "*" in sub:
                    continue

                if sub.endswith(domain):
                    results.add(sub)

    except Exception:
        pass

    return results


def from_bufferover(domain):
    """
    Fetch subdomains from BufferOver
    Returns: set()
    """

    results = set()

    try:

        url = f"https://dns.bufferover.run/dns?q=.{domain}"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=8
        )

        if response.status_code != 200:
            return results

        data = response.json()

        for item in data.get("FDNS_A", []):

            try:

                sub = item.split(",")[1].strip().lower()

                if sub.endswith(domain):
                    results.add(sub)

            except Exception:
                pass

    except Exception:
        pass

    return results


def certificate_engine(domain):
    """
    Merge all certificate sources
    """

    found = set()

    found.update(from_crtsh(domain))
    found.update(from_bufferover(domain))

    return found