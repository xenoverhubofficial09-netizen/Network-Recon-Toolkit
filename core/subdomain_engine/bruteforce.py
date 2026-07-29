import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

#
# Load wordlist once
#

WORDLIST = None


def load_wordlist(path="utils/wordlists/subdomains.txt"):

    global WORDLIST

    if WORDLIST is None:

        with open(path, "r", encoding="utf-8") as file:

            WORDLIST = [

                line.strip()

                for line in file

                if line.strip()

            ]

    return WORDLIST


def resolve(subdomain):

    try:

        ip = socket.gethostbyname(subdomain)

        return (
            subdomain,
            ip
        )

    except Exception:

        return None


def bruteforce_engine(domain, workers=300, progress_callback=None):

    words = load_wordlist()

    targets = [

        f"{word}.{domain}"

        for word in words

    ]

    found = set()

    checked = 0
    total = len(targets)

    with ThreadPoolExecutor(max_workers=workers) as executor:

        futures = [

            executor.submit(resolve, target)

            for target in targets

        ]

        for future in as_completed(futures):

            checked += 1

            result = future.result()

            if result:

                found.add(result[0])

            if progress_callback:

                progress_callback(

                    checked,

                    total,

                    len(found)

                )

    return found