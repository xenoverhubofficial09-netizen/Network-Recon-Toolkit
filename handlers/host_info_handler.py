from core.host_info import get_host_information
from utils.formatter import print_header, print_footer
from utils.validators import validate_host
from utils.constants import ERROR_EMPTY_INPUT


def host_information():

    host = input("\nEnter Domain or IP: ").strip()

    if not host:
        print(f"\n[ERROR] {ERROR_EMPTY_INPUT}")
        return

    if not validate_host(host):
        print("\n[ERROR] Invalid domain or IP address.")
        return

    result = get_host_information(host)

    print_header("HOST INFORMATION")

    if result["success"]:

        print(f"Host             : {result['host']}")
        print(f"Resolved IP      : {result['ip']}")
        print(f"Reverse DNS      : {result['reverse_dns']}")
        print(f"IP Version       : {result['ip_version']}")
        print(f"Address Type     : {result['address_type']}")

    else:

        print("Status           : Failed")
        print(f"Reason           : {result['message']}")

    print_footer()