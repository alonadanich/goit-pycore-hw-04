
import sys
from pathlib import Path
from colorama import Fore, Style, init


init(autoreset=True)


def print_directory_structure(directory: Path, indent: str = ""):
    try:
        if not directory.is_dir():
            print(f"{Fore.RED}Помилка: {directory} не є директорією.")
            return
        items = list(directory.iterdir())
        for index, item in enumerate(items):
            connector = "┗" if index == len(items) - 1 else "┣"
            if item.is_dir():
                print(f"{indent}{connector} {Fore.GREEN}{item.name}")
                print_directory_structure(item, indent + "┃  ")
            else:
                print(f"{indent}{connector} {Fore.YELLOW}{item.name}")

    except Exception as e:
        print(f"{Fore.RED}Помилка: {str(e)}")


def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw23.py /goit-pycore-hw-04")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: Шлях {directory_path} не існує.")
        sys.exit(1)

    
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()
