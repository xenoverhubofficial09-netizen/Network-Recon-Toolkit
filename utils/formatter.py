from utils.constants import MENU_WIDTH


def print_header(title: str) -> None:
    print()
    print("=" * MENU_WIDTH)
    print(title.center(MENU_WIDTH))
    print("=" * MENU_WIDTH)


def print_footer() -> None:
    print("=" * MENU_WIDTH)