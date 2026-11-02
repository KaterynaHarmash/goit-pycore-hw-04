
import sys
from pathlib import Path
from colorama import Fore

FILE_COLORS = {
    ".py": Fore.YELLOW,
    ".txt": Fore.WHITE,
    ".js": Fore.CYAN,
    ".json": Fore.CYAN,
    ".md": Fore.GREEN,
    ".png": Fore.MAGENTA,
    ".jpg": Fore.MAGENTA,
    ".jpeg": Fore.MAGENTA,
    ".svg": Fore.MAGENTA,
    ".pdf": Fore.RED,
    ".zip": Fore.LIGHTRED_EX,
    ".xlsx": Fore.LIGHTGREEN_EX,
    ".csv": Fore.LIGHTGREEN_EX,
}


def print_tree(directory, prefix=""):
    try:
        items = list(directory.iterdir())
    except PermissionError:
        print(Fore.RED + f"{prefix}Немає доступу до директорії")
        return
    except OSError as error:
        print(Fore.RED + f"{prefix}Помилка читання: {error}")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1

        connector = "└── " if is_last else "├── "
        new_prefix = prefix + ("    " if is_last else "│   ")

        if item.is_dir():
            print(Fore.BLUE + prefix + connector + "📂 " + item.name)
            print_tree(item, new_prefix)
        else:
            color = FILE_COLORS.get(item.suffix.lower(), Fore.WHITE)
            print(color + prefix + connector + "📄 " + item.name)


def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: не вказано шлях до директорії")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + f"Помилка: шлях не існує — {path}")
        return

    if not path.is_dir():
        print(Fore.RED + f"Помилка: це не директорія — {path}")
        return

    print(Fore.BLUE + f"📦 {path.name}")
    print_tree(path)


if __name__ == "__main__":
    main()
