from colorama import Fore

from core.subdomain_finder import find_subdomains


def subdomain_finder():

    domain = input("\nEnter Domain: ").strip()

    try:

        results, scan_time = find_subdomains(domain)

        print("\n" + "=" * 70)
        print("                 SUBDOMAIN FINDER")
        print("=" * 70)

        print(f"Target : {domain}")

        print("\nSUBDOMAIN                                       IP")
        print("-" * 70)

        if results:

            for subdomain, ip in results:

                print(f"{subdomain:<48} {ip}")

        else:

            print(Fore.RED + "No subdomains found.")

        print("-" * 70)
        print(f"Found     : {len(results)}")
        print(f"Scan Time : {scan_time} sec")
        print("=" * 70)

    except Exception as e:

        print(Fore.RED + f"\n[ERROR] {e}")