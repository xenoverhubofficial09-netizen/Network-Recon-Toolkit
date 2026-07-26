from handlers.ip_handler import domain_to_ip, ip_to_domain
from handlers.dns_handler import dns_records
from handlers.whois_handler import whois_lookup
from handlers.ping_handler import ping
from handlers.host_info_handler import host_information
from handlers.port_scanner_handler import port_scanner
from handlers.ip_info_handler import ip_information


def start():

    while True:

        print("\n" + "=" * 50)
        print("           NETWORK RECON TOOLKIT")
        print("=" * 50)

        print("1. Domain → IP")
        print("2. IP → Domain")
        print("3. DNS Records")
        print("4. WHOIS Lookup")
        print("5. Ping Tool")
        print("6. Host Information")
        print("7. Port Scanner")
        print("8. IP Information")
        print("9. Exit")

        choice = input("\nSelect Option: ").strip()

        match choice:

            case "1":
                domain_to_ip()

            case "2":
                ip_to_domain()

            case "3":
                dns_records()

            case "4":
                whois_lookup()

            case "5":
                ping()

            case "6":
                host_information()

            case "7":
                port_scanner()

            case "8":
                ip_information()

            case "9":
                print("\nGoodbye!")
                break

            case _:
                print("\n[ERROR] Invalid option.")