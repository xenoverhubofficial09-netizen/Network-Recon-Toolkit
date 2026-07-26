import dns.resolver


def get_records(domain: str, record_type: str):

    try:

        answers = dns.resolver.resolve(domain, record_type)

        return [answer.to_text() for answer in answers]

    except Exception:

        return None