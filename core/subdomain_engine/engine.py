import time

from core.subdomain_engine.certificate import certificate_engine
from core.subdomain_engine.bruteforce import bruteforce_engine
from core.subdomain_engine.permutation import permutation_engine
from core.subdomain_engine.merger import merge_results
from core.subdomain_engine.verifier import verify_subdomains
from core.subdomain_engine.wildcard import wildcard_detect


def subdomain_engine(domain, progress_callback=None):

    start = time.time()

    #
    # Certificate Engine
    #

    certificate_results = certificate_engine(domain)

    if progress_callback:

        progress_callback(
            "certificate",
            len(certificate_results),
            0,
            0
        )

    #
    # Bruteforce Engine
    #

    bruteforce_results = bruteforce_engine(

        domain,

        progress_callback=lambda checked, total, found:
        progress_callback(
            "bruteforce",
            found,
            checked,
            total
        ) if progress_callback else None

    )

    #
    # Merge Results
    #

    merged = merge_results(

        certificate_results,

        bruteforce_results

    )

    #
    # Permutation Engine
    #

    permutation_results = permutation_engine(merged)

    merged = merge_results(

        merged,

        permutation_results

    )

    #
    # Remove Duplicate Again
    #

    merged = sorted(set(merged))

    #
    # Wildcard Detection
    #

    wildcard_enabled, wildcard_ip = wildcard_detect(domain)

    #
    # Verification
    #

    verified, unverified = verify_subdomains(

        merged,

        wildcard_enabled,

        wildcard_ip

    )

    #
    # Scan Time
    #

    scan_time = round(

        time.time() - start,

        2

    )

    return (

        verified,

        unverified,

        scan_time

    )