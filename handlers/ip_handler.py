from core.dns_lookup import get_ip_address, get_hostname


def domain_to_ip():

    domain = input("\nEnter Domain: ").strip()

    ip_address = get_ip_address(domain)

    if ip_address is None:
        print("\n[ERROR] Invalid Domain")
    else:
        print(f"\nDomain     : {domain}")
        print(f"IP Address : {ip_address}")


def ip_to_domain():

    ip = input("\nEnter IP Address: ").strip()

    hostname = get_hostname(ip)

    if hostname is None:
        print("\n[ERROR] Hostname Not Found")
    else:
        print(f"\nIP Address : {ip}")
        print(f"Hostname   : {hostname}")