from core.traceroute import traceroute
from utils.constants import ERROR_EMPTY_INPUT
from utils.formatter import print_header, print_footer
from utils.validators import validate_host


def run_traceroute():

    host = input("\nEnter Domain or IP: ").strip()

    if not host:
        print(f"\n[ERROR] {ERROR_EMPTY_INPUT}")
        return

    if not validate_host(host):
        print("\n[ERROR] Invalid domain or IP address.")
        return

    print_header("TRACEROUTE")

    print("\nRunning traceroute...\n")

    result = traceroute(host)

    if not result["success"]:
        print(f"Reason : {result['message']}")
        print_footer()
        return

    print(f"Target       : {result['host']}")
    print(f"Resolved IP  : {result['ip']}")
    print(f"Duration     : {result['scan_time']} sec")

    print("\n---------------------------------------------\n")

    print(result["output"])

    print_footer()