from core.whois_lookup import get_whois


def whois_lookup():

    print("WHOIS Handler Started")

    domain = input("Enter Domain: ")

    print(domain)

    info = get_whois(domain)

    print(info)

    input("\nPress Enter to return...")