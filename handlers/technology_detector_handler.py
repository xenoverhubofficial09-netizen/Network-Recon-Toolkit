from core.technology_detector import detect_technology


def technology_detector():

    host = input("\nEnter Host: ").strip()

    try:

        (
            ip,
            server,
            powered_by,
            cms,
            cdn,
            technologies
        ) = detect_technology(host)

        print("\n" + "=" * 60)
        print("             TECHNOLOGY DETECTION")
        print("=" * 60)

        print(f"Host       : {host}")
        print(f"IP         : {ip}")

        print("\nServer")
        print("-" * 45)
        print(server)

        print("\nPowered By")
        print("-" * 45)
        print(powered_by)

        print("\nCMS")
        print("-" * 45)
        print(cms)

        print("\nCDN")
        print("-" * 45)
        print(cdn)

        print("\nDetected Technologies")
        print("-" * 45)

        if technologies:

            for tech in technologies:
                print(f"✓ {tech}")

        else:
            print("No common technologies detected.")

        print("=" * 60)

    except Exception as e:
        print(f"\n[ERROR] {e}")