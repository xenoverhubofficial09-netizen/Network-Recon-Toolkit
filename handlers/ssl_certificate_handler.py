from core.ssl_certificate import get_ssl_certificate


def ssl_certificate():

    host = input("\nEnter Host: ").strip()

    try:

        (
            ip,
            subject,
            issuer,
            valid_from,
            valid_until,
            days_remaining,
        ) = get_ssl_certificate(host)

        print("\n" + "=" * 60)
        print("            SSL CERTIFICATE INFORMATION")
        print("=" * 60)

        print(f"Host           : {host}")
        print(f"IP             : {ip}")
        print(f"Subject        : {subject}")
        print(f"Issuer         : {issuer}")
        print(f"Valid From     : {valid_from}")
        print(f"Valid Until    : {valid_until}")
        print(f"Days Remaining : {days_remaining}")

        if days_remaining > 30:
            print("Status         : VALID")

        elif days_remaining >= 0:
            print("Status         : EXPIRING SOON")

        else:
            print("Status         : EXPIRED")

        print("=" * 60)

    except Exception as e:
        print(f"\n[ERROR] {e}")