from colorama import Fore
from core.subdomain_finder import find_subdomains
from utils.spinner import Spinner
import sys


def progress(stage, found, checked, total):

    if stage == "certificate":

        print(
            Fore.GREEN
            + f"\n[✓] Certificate Engine Completed | Found : {found}"
        )

    elif stage == "bruteforce":

        percent = int((checked / total) * 100)

        bar_length = 30

        filled = int(bar_length * checked / total)

        bar = "█" * filled + "░" * (bar_length - filled)

        sys.stdout.write(
            "\r"
            + Fore.CYAN
            + f"[{bar}] {percent:3d}% | Checked: {checked}/{total} | Found: {found}"
        )

        sys.stdout.flush()

        if checked == total:
            print()


def subdomain_finder():

    domain = input("\nEnter Domain: ").strip().lower()

    spinner = Spinner("Initializing Scan...")

    try:

        print()

        spinner.start()

        verified, unverified, scan_time = find_subdomains(

            domain,

            progress_callback=progress

        )

        spinner.stop()

        print()

        print("=" * 90)
        print("                    SUBDOMAIN FINDER")
        print("=" * 90)

        print(f"Target : {domain}")

        #
        # VERIFIED
        #

        print("\n" + Fore.GREEN + "================ VERIFIED ================\n")

        if verified:

            print(f"{'SUBDOMAIN':<55}{'IP':<18}STATUS")
            print("-" * 90)

            for item in verified:

                print(
                    f"{item['host']:<55}"
                    f"{item['ip']:<18}"
                    f"{item['reason']}"
                )

        else:

            print(Fore.RED + "No verified subdomains.")

        #
        # UNVERIFIED
        #

        print("\n" + Fore.YELLOW + "============== UNVERIFIED ==============\n")

        if unverified:

            print(f"{'SUBDOMAIN':<55}{'IP':<18}REASON")
            print("-" * 90)

            for item in unverified:

                print(
                    f"{item['host']:<55}"
                    f"{item['ip']:<18}"
                    f"{item['reason']}"
                )

        else:

            print(Fore.GREEN + "No unverified subdomains.")

        print("\n" + "-" * 90)

        print(Fore.GREEN + f"Verified   : {len(verified)}")
        print(Fore.YELLOW + f"Unverified : {len(unverified)}")
        print(Fore.CYAN + f"Scan Time  : {scan_time} sec")

        print("=" * 90)

    except Exception as e:

        spinner.stop()

        print(Fore.RED + f"\n[ERROR] {e}")