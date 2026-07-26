from core.dns_records import get_records


def dns_records():

    domain = input("\nEnter Domain: ").strip()

    print("\nDNS Record Types")
    print("1. A")
    print("2. AAAA")
    print("3. MX")
    print("4. NS")
    print("5. TXT")

    record_choice = input("\nSelect Record Type: ").strip()

    record_map = {
        "1": "A",
        "2": "AAAA",
        "3": "MX",
        "4": "NS",
        "5": "TXT"
    }

    if record_choice not in record_map:
        print("\n[ERROR] Invalid Record Type")
        return

    records = get_records(domain, record_map[record_choice])

    if records is None:
        print("\n[ERROR] No Records Found")
        return

    print(f"\n{record_map[record_choice]} Records\n")

    for record in records:
        print(record)