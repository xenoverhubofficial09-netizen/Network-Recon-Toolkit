from core.ip_info import get_ip_information


def ip_information():

    target = input("\nEnter Domain or IP: ").strip()

    try:

        info = get_ip_information(target)

        print("\n" + "=" * 60)
        print("                 IP INFORMATION")
        print("=" * 60)

        print(f"Target       : {info['target']}")
        print(f"IP Address   : {info['ip']}")
        print(f"Hostname     : {info['hostname']}")

        print("\nLOCATION")
        print("-" * 60)
        print(f"Country      : {info['country']}")
        print(f"Region       : {info['region']}")
        print(f"City         : {info['city']}")
        print(f"ZIP Code     : {info['zip']}")

        print("\nCOORDINATES")
        print("-" * 60)
        print(f"Latitude     : {info['lat']}")
        print(f"Longitude    : {info['lon']}")

        print("\nNETWORK")
        print("-" * 60)
        print(f"Timezone     : {info['timezone']}")
        print(f"ISP          : {info['isp']}")
        print(f"Organization : {info['org']}")
        print(f"ASN          : {info['asn']}")

        print("=" * 60)

    except Exception as e:
        print(f"\n[ERROR] {e}")