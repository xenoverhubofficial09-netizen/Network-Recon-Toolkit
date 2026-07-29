COMMON_SUFFIXES = [
    "dev",
    "test",
    "stage",
    "staging",
    "prod",
    "api",
    "beta",
    "old",
    "new",
    "backup",
    "vpn",
    "mail",
    "cdn"
]


def permutation_engine(subdomains):

    generated = set()

    for sub in subdomains:

        try:

            prefix = sub.split(".")[0]
            domain = ".".join(sub.split(".")[1:])

            for suffix in COMMON_SUFFIXES:

                generated.add(
                    f"{prefix}-{suffix}.{domain}"
                )

                generated.add(
                    f"{suffix}-{prefix}.{domain}"
                )

                generated.add(
                    f"{prefix}{suffix}.{domain}"
                )

                generated.add(
                    f"{suffix}{prefix}.{domain}"
                )

        except Exception:
            pass

    return generated