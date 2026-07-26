import whois

def get_whois(domain: str):
    try:
        return whois.whois(domain)
    except Exception as e:
        print(f"[ERROR] {e}")
        return None