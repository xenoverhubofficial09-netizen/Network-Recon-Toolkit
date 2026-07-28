from colorama import Fore

from core.asn_lookup import asn_lookup


def run_asn_lookup():

    target = input("\nEnter Domain or IP: ").strip()

    if not target:
        print(Fore.RED + "\n[ERROR] Target cannot be empty.")
        return

    try:

        result = asn_lookup(target)

        print("\n" + "=" * 60)
        print("                    ASN LOOKUP")
        print("=" * 60)

        print(f"Target       : {result['target']}")
        print(f"IP Address   : {result['ip']}")
        print(f"Hostname     : {result['hostname']}")

        print("-" * 60)

        print(f"ASN          : {result['asn']}")
        print(f"Organization : {result['organization']}")
        print(f"ISP          : {result['isp']}")
        print(f"Country      : {result['country']}")

        print("=" * 60)

    except Exception as e:

        print(Fore.RED + f"\n[ERROR] {e}")