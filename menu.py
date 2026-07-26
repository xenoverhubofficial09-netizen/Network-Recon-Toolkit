from colorama import Fore, Style, init
from pyfiglet import Figlet

from handlers.ip_handler import domain_to_ip, ip_to_domain
from handlers.dns_handler import dns_records
from handlers.whois_handler import whois_lookup
from handlers.ping_handler import ping
from handlers.host_info_handler import host_information
from handlers.port_scanner_handler import port_scanner
from handlers.ip_info_handler import ip_information


init(autoreset=True)


def start():

    while True:

        print("\n" + Fore.CYAN + "=" * 70)

        fig = Figlet(font="big")

        print(Fore.GREEN + fig.renderText("NETWORK"))
        print(Fore.GREEN + fig.renderText("RECON"))
        print(Fore.GREEN + fig.renderText("TOOLKIT"))
        print(Fore.YELLOW + fig.renderText("BY XENOVER !"))

        print(Fore.CYAN + "=" * 70)

        print(Fore.WHITE + """
[1] Domain → IP
[2] IP → Domain
[3] DNS Records
[4] WHOIS Lookup
[5] Ping Tool
[6] Host Information
[7] Port Scanner
[8] IP Information
[9] Exit
""")

        choice = input(
            Fore.CYAN + "Select Option: " + Style.RESET_ALL
        ).strip()


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
                print(Fore.RED + "\nGoodbye!")
                break

            case _:
                print(Fore.RED + "\n[ERROR] Invalid option.")