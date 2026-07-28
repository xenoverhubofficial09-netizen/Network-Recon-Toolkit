from colorama import Fore

from core.banner_grabber import grab_banner


def banner_grabber():

    host = input("\nEnter Host : ").strip()

    if not host:
        print(Fore.RED + "\n[ERROR] Host cannot be empty.")
        return

    port_input = input("Enter Port : ").strip()

    if not port_input.isdigit():
        print(Fore.RED + "\n[ERROR] Invalid port.")
        return

    port = int(port_input)

    if port < 1 or port > 65535:
        print(Fore.RED + "\n[ERROR] Port must be between 1 and 65535.")
        return

    result = grab_banner(host, port)

    print("\n" + "=" * 60)
    print("                 BANNER GRABBER")
    print("=" * 60)

    if not result["success"]:

        print(f"Host    : {host}")
        print(f"Port    : {port}")
        print(f"\nError   : {result['error']}")

        return

    print(f"Host    : {result['host']}")
    print(f"IP      : {result['ip']}")
    print(f"Port    : {result['port']}")
    print(f"Service : {result['service']}")

    print("\n" + "-" * 60)
    print("Banner")
    print("-" * 60)

    print(result["banner"])

    print("=" * 60)