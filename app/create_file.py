import sys
import os
from datetime import datetime
from pathlib import Path


def get_dir_name() -> list:
    if "-f" in sys.argv:
        if sys.argv.index("-f") > sys.argv.index("-d"):
            return sys.argv[sys.argv.index("-d") + 1 : sys.argv.index("-f")]
        else:
            return sys.argv[sys.argv.index("-d") + 1:]
    else:
        return sys.argv[sys.argv.index("-d") + 1:]


def create_dir(directories: list) -> None:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


def file_entry(file_path: str) -> None:
    lines = []
    if file_path.is_file():
        method = "a"
        lines.append("\n")
    else:
        method = "w"

    with open(file_path, method) as file:
        lines.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.writelines(lines)
                break
            lines.append(f"{count} {line}\n")
            count += 1


if "-d" in sys.argv and "-f" not in sys.argv:
    directories = get_dir_name()
    create_dir(directories)

if "-f" in sys.argv and "-d" not in sys.argv:
    file_name = sys.argv[sys.argv.index("-f") + 1]
    file_path = Path(os.path.join(os.getcwd(), file_name))
    file_entry(file_path)

if "-d" in sys.argv and "-f" in sys.argv:
    directories = get_dir_name()
    file_name = sys.argv[sys.argv.index("-f") + 1]
    create_dir(directories)
    file_path = Path(os.path.join(*directories, file_name))
    file_entry(file_path)
