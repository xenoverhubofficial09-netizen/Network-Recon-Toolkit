from colorama import Fore

from core.http_headers import get_http_headers


def http_headers():

    host = input("\nEnter Domain: ").strip()

    try:

        ip, url, headers = get_http_headers(host)

        print("\n" + "=" * 70)
        print("                    HTTP HEADERS")
        print("=" * 70)

        print(f"Host : {host}")
        print(f"IP   : {ip}")
        print(f"URL  : {url}")

        print("\nHeaders")
        print("-" * 70)

        for key, value in headers.items():
            print(f"{Fore.CYAN}{key:<30}{Fore.WHITE}: {value}")

    except Exception as e:
        print(f"\n{Fore.RED}[ERROR] {e}")