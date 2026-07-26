from core.port_scanner import scan_host


def port_scanner():

    host = input("\nEnter Host: ").strip()

    try:

        ip, results, scan_time = scan_host(host)

        print("\n" + "=" * 60)
        print("                 PORT SCAN RESULT")
        print("=" * 60)

        print(f"Host : {host}")
        print(f"IP   : {ip}")

        print("\nPORT    SERVICE")
        print("-" * 45)

        for port, service, banner in results:

            print(f"{port:<7} {service}")

            if banner:
                print(f"        Banner : {banner}")

        print("\n" + "-" * 45)
        print(f"Open Ports : {len(results)}")
        print(f"Scan Time  : {scan_time} sec")

    except Exception as e:
        print(f"\n[ERROR] {e}")