from colorama import Fore

from core.reverse_dns import reverse_dns_lookup


def run_reverse_dns():

    target = input("\nEnter Domain or IP: ").strip()

    if not target:
        print(Fore.RED + "\n[ERROR] Target cannot be empty.")
        return

    try:

        result = reverse_dns_lookup(target)

        print("\n" + "=" * 60)
        print("                REVERSE DNS LOOKUP")
        print("=" * 60)

        print(f"Target    : {result['target']}")
        print(f"IP        : {result['ip']}")
        print(f"Hostname  : {result['hostname']}")

        print("-" * 60)

        print("Aliases")

        if result["aliases"]:
            for alias in result["aliases"]:
                print(f"  • {alias}")
        else:
            print("  N/A")

        print("-" * 60)

        print("Resolved Addresses")

        for address in result["addresses"]:
            print(f"  • {address}")

        print("=" * 60)

    except Exception as e:

        print(Fore.RED + f"\n[ERROR] {e}")