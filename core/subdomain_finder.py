from core.subdomain_engine.engine import subdomain_engine


def find_subdomains(domain, progress_callback=None):

    return subdomain_engine(

        domain,

        progress_callback=progress_callback

    )