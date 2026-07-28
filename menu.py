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
from handlers.traceroute_handler import run_traceroute
from handlers.banner_grabber_handler import banner_grabber
from handlers.asn_lookup_handler import run_asn_lookup
from handlers.reverse_dns_handler import run_reverse_dns
from handlers.security_headers_handler import security_headers_lookup
from handlers.robots_analyzer_handler import robots_analyzer

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
    print(Fore.LIGHTGREEN_EX + "[13]" + Fore.WHITE + " Traceroute")
    print(Fore.LIGHTGREEN_EX + "[14]" + Fore.WHITE + " Banner Grabber")
    print(Fore.LIGHTGREEN_EX + "[15]" + Fore.WHITE + " ASN Lookup")
    print(Fore.LIGHTGREEN_EX + "[16]" + Fore.WHITE + " Reverse DNS Lookup")
    print(Fore.LIGHTGREEN_EX + "[17]" + Fore.WHITE + " Security Headers Analyzer")
    print(Fore.LIGHTGREEN_EX + "[18]" + Fore.WHITE + " Robots.txt Analyzer")
    print(Fore.LIGHTRED_EX + "[19]" + Fore.WHITE + " Exit")

    print(Fore.CYAN + "-" * 70)

    print(
        Fore.YELLOW
        + "Modules : 18    "
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

        ...

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
                run_traceroute()
                wait()

            case "14":
                banner_grabber()
                wait()

            case "15":
                run_asn_lookup()
                wait()

            case "16":
                run_reverse_dns()
                wait()

            case "17":
                target = input("\nEnter URL or Domain: ").strip()

                if target:
                    try:
                        result = security_headers_lookup(target)

                        print("\n" + "=" * 60)
                        print("            SECURITY HEADERS ANALYZER")
                        print("=" * 60)

                        for header, value in result.items():
                            print(f"{header}: {value}")

                        print("=" * 60)

                    except Exception as e:
                        print(Fore.RED + f"\n[ERROR] {e}")

                wait()

            case "18":
                robots_analyzer()
                wait()

            case "19":
                print(
                    Fore.RED
                    + "\nThank you for using Network Recon Toolkit."
                )

                print(
                    Fore.YELLOW
                    + "Developed by Xenover\n"
                )

                break

            case _:
                print(
                    Fore.RED
                    + "\n[ERROR] Invalid option. Please select a valid menu item."
                )

                wait()