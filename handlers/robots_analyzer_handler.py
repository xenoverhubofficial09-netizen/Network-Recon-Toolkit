"""
Robots Analyzer Handler

Handles user interaction and connects
CLI layer with robots analyzer core.
"""

from colorama import Fore

from core.robots_analyzer import fetch_robots


def robots_analyzer():
    """
    Run robots.txt analyzer.
    """

    target = input(
        Fore.CYAN
        + "\nEnter URL or Domain: "
    ).strip()


    if not target:
        print(
            Fore.RED
            + "\n[ERROR] Target cannot be empty."
        )
        return


    try:

        result = fetch_robots(target)


        print(
            Fore.GREEN
            + "\n"
            + "=" * 60
        )

        print(
            Fore.YELLOW
            + "             ROBOTS.TXT ANALYZER"
        )

        print(
            Fore.GREEN
            + "=" * 60
        )


        print(
            Fore.WHITE
            + f"\nURL: {result['url']}"
        )

        print(
            Fore.WHITE
            + f"Status: {result['status']}"
        )

        print(
            Fore.WHITE
            + f"Status Code: {result['status_code']}"
        )


        print(
            Fore.CYAN
            + "\nUser Agents:"
        )

        for agent in result["user_agents"]:
            print(
                Fore.WHITE
                + f" - {agent}"
            )


        print(
            Fore.CYAN
            + "\nDisallowed Paths:"
        )

        for path in result["disallowed"]:
            print(
                Fore.WHITE
                + f" - {path}"
            )


        print(
            Fore.CYAN
            + "\nAllowed Paths:"
        )

        for path in result["allowed"]:
            print(
                Fore.WHITE
                + f" - {path}"
            )


        print(
            Fore.CYAN
            + "\nSitemaps:"
        )

        for sitemap in result["sitemaps"]:
            print(
                Fore.WHITE
                + f" - {sitemap}"
            )


        print(
            Fore.GREEN
            + "\n"
            + "=" * 60
        )


    except Exception as error:

        print(
            Fore.RED
            + f"\n[ERROR] {error}"
        )