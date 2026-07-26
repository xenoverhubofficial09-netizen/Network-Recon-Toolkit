from core.subdomain_finder import find_subdomains


def subdomain_finder():

    domain = input("\nEnter Domain: ").strip()

    try:

        results, scan_time = find_subdomains(domain)

        print("\n" + "=" * 65)
        print("                 SUBDOMAIN FINDER")
        print("=" * 65)

        print(f"Target : {domain}")

        print("\nSUBDOMAIN                           IP")
        print("-" * 65)

        if results:

            for subdomain, ip in results:

                print(f"{subdomain:<35} {ip}")

        else:

            print("No subdomains found.")

        print("\n" + "-" * 65)
        print(f"Found     : {len(results)}")
        print(f"Scan Time : {scan_time} sec")

    except Exception as e:

        print(f"\n[ERROR] {e}")