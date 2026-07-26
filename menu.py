import os

from colorama import Fore, Style, init
from pyfiglet import Figlet

from handlers.ip_handler import domain_to_ip, ip_to_domain
from handlers.dns_handler import dns_records
from handlers.whois_handler import whois_lookup
from handlers.ping_handler import ping
from handlers.host_info_handler import host_information
from handlers.port_scanner_handler import port_scanner
from handlers.ip_info_handler import ip_information
from handlers.http_headers_handler import http_headers
from handlers.ssl_certificate_handler import ssl_certificate
from handlers.technology_detector_handler import technology_detector
from handlers.subdomain_finder_handler import subdomain_finder

init(autoreset=True)


def banner():

    fig = Figlet(font="small")

    print(Fore.CYAN + "=" * 70)
    print(Fore.GREEN + fig.renderText("Network   Recon Toolkit"))
    print(Fore.YELLOW + "                     by Xenover")
    print(Fore.WHITE + "                     Version : 1.0.0")
    print(Fore.CYAN + "=" * 70)


def menu():

    print(Fore.LIGHTGREEN_EX + "[01]" + Fore.WHITE + " Domain → IP")
    print(Fore.LIGHTGREEN_EX + "[02]" + Fore.WHITE + " IP → Domain")
    print(Fore.LIGHTGREEN_EX + "[03]" + Fore.WHITE + " DNS Records")
    print(Fore.LIGHTGREEN_EX + "[04]" + Fore.WHITE + " WHOIS Lookup")
    print(Fore.LIGHTGREEN_EX + "[05]" + Fore.WHITE + " Ping Tool")
    print(Fore.LIGHTGREEN_EX + "[06]" + Fore.WHITE + " Host Information")
    print(Fore.LIGHTGREEN_EX + "[07]" + Fore.WHITE + " Port Scanner")
    print(Fore.LIGHTGREEN_EX + "[08]" + Fore.WHITE + " IP Information")
    print(Fore.LIGHTGREEN_EX + "[09]" + Fore.WHITE + " HTTP Headers")
    print(Fore.LIGHTGREEN_EX + "[10]" + Fore.WHITE + " SSL Certificate")
    print(Fore.LIGHTGREEN_EX + "[11]" + Fore.WHITE + " Technology Detector")
    print(Fore.LIGHTGREEN_EX + "[12]" + Fore.WHITE + " Subdomain Finder")
    print(Fore.LIGHTRED_EX + "[13]" + Fore.WHITE + " Exit")

    print(Fore.CYAN + "-" * 70)

    print(
        Fore.YELLOW
        + "Modules : 12    "
        + Fore.GREEN
        + "Status : READY    "
        + Fore.CYAN
        + "Python Toolkit"
    )

    print(Fore.CYAN + "-" * 70)


def wait():

    input(
        Fore.YELLOW
        + "\nPress ENTER to return to menu..."
        + Style.RESET_ALL
    )


def start():

    while True:

        os.system("cls" if os.name == "nt" else "clear")

        print()

        banner()

        menu()

        choice = input(
            Fore.CYAN
            + "\nSelect Option > "
            + Style.RESET_ALL
        ).strip()

        match choice:

            case "1" | "01":
                domain_to_ip()
                wait()

            case "2" | "02":
                ip_to_domain()
                wait()

            case "3" | "03":
                dns_records()
                wait()

            case "4" | "04":
                whois_lookup()
                wait()

            case "5" | "05":
                ping()
                wait()

            case "6" | "06":
                host_information()
                wait()

            case "7" | "07":
                port_scanner()
                wait()

            case "8" | "08":
                ip_information()
                wait()

            case "9" | "09":
                http_headers()
                wait()

            case "10":
                ssl_certificate()
                wait()

            case "11":
                technology_detector()
                wait()

            case "12":
                subdomain_finder()
                wait()

            case "13":
                print(Fore.RED + "\nThank you for using Network Recon Toolkit.")
                print(Fore.YELLOW + "Developed by Xenover\n")
                break

            case _:
                print(Fore.RED + "\n[ERROR] Invalid option. Please select a valid menu item.")
                wait()