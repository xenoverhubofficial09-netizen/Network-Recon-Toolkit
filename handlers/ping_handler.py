from core.ping_tool import ping_host
from utils.constants import ERROR_EMPTY_INPUT, FAILED, SUCCESS
from utils.formatter import print_footer, print_header
from utils.validators import validate_host


def ping():
    host = input("\nEnter Domain or IP: ").strip()

    if not host:
        print(f"\n[ERROR] {ERROR_EMPTY_INPUT}")
        return

    if not validate_host(host):
        print("\n[ERROR] Invalid domain or IP address.")
        return

    result = ping_host(host)

    print_header("PING RESULT")

    if result["success"]:

        print(f"Host             : {result['host']}")
        print(f"Resolved IP      : {result['ip']}")
        print(f"Status           : {SUCCESS}")
        print(f"Packets Sent     : {result['packets_sent']}")
        print(f"Packets Received : {result['packets_received']}")
        print(f"Packets Lost     : {result['packets_lost']}")
        print(f"Packet Loss      : {result['packet_loss']}")

        if result["latency"]:
            print(f"Average Latency  : {result['latency']}")

        if result["ttl"]:
            print(f"TTL              : {result['ttl']}")

        print(f"Checked At       : {result['checked_at']}")

    else:

        if "host" in result:
            print(f"Host             : {result['host']}")

        if "ip" in result:
            print(f"Resolved IP      : {result['ip']}")

        print(f"Status           : {FAILED}")
        print(f"Reason           : {result['message']}")
        print(f"Checked At       : {result['checked_at']}")

    print_footer()