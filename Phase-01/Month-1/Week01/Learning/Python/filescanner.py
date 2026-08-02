import sys
sys.path.append(r"D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python")
from security_toolkit import SecurityToolkit

from pathlib import Path
from datetime import datetime
import argparse

class FileScanner(SecurityToolkit):
    def __init__(self, name, version):
        super().__init__(name, version)

    @staticmethod
    def walk(directory, extension=None):
        if extension is None:
            extension = "*"
        for file_path in Path(directory).absolute().rglob(extension):
                if file_path.is_file():
                    yield file_path

    @staticmethod
    def find_large_files(directory, min_size_mb) -> list[Path]:
        size_in_bytes = min_size_mb * 1024 **2
        answer = []
        for file_path in FileScanner.walk(directory):
            if file_path.stat().st_size > size_in_bytes:
                answer.append(file_path)
        return answer

    @staticmethod
    def find_recent_files(directory, days=7) -> list[Path]:
        answer = []
        for file_path in FileScanner.walk(directory):
            file_modifed = datetime.fromtimestamp(file_path.stat().st_mtime)
            if (datetime.now() - file_modifed).days <= days:
                answer.append(file_path)
        return answer

    @staticmethod
    def count_by_extension(directory) -> dict:
        my_extensions = {}
        for file_path in FileScanner.walk(directory):
            suffix = file_path.suffix
            if suffix:
                my_extensions[suffix] = my_extensions.get(suffix, 0) + 1
            else:
                my_extensions["No Extension"] = my_extensions.get("No Extension", 0) + 1
        return my_extensions

def make_parser():
    parser = argparse.ArgumentParser(description="A File scanner")
    parser.add_argument("--dir", required=True, type=str, help="The file path")
    parser.add_argument("--cext", help="Count by extension in the file path", default=None, const="*", nargs="?")
    sub_commands = parser.add_subparsers(dest="command", description="Adding some functions")

    parser_walk = sub_commands.add_parser("walk", help="listing file names in the file path", description="listing file names in the file path")
    parser_walk.add_argument("--ext",  type=str,help="An extension to search", default=None)
    parser_walk.add_argument("--count", type=int, help="how many to get back", default=1)

    parser_large_files = sub_commands.add_parser("largefiles", description="Searching large files", help="To search large files")
    parser_large_files.add_argument("--mn_size", type=float, help="Min size to search", required=True)

    parser_recent_files = sub_commands.add_parser("rfiles", description="Finding recent files", help="For finding recent files")
    parser_recent_files.add_argument("--days", type=int, nargs="?" ,help="Days to search", required=True, const=7)
    return parser

def main(args, helper=None):
    if helper is None:
        helper = FileScanner("File scanner", "1.0v")

    if args.cext is not None and args.command is not None:
        print("--cext cannot be used with subcommands. Use it alone.")
    
    elif not Path(args.dir).absolute().exists():
        print(f"'{args.dir}' is not exist.")
        sys.exit(2)

    elif args.cext is not None:
        count_ext = helper.count_by_extension(args.dir)
        if args.cext == "*":
            print(f"The count of {args.cext}: {count_ext}")
        else:
            try:
                print(f"The count of {args.cext}: {count_ext[args.cext]}")
            except KeyError:
                print(f"Invalid key. Valid: {[key for key in count_ext]}")

    elif not Path(args.dir).absolute().is_dir():
        print(f"'{args.dir}' is not a directory.")
        sys.exit(3)

    elif args.command == "walk":
        files_path = helper.walk(args.dir, args.ext)
        for i in range(args.count):
            try:
                print(f"{i + 1}. {next(files_path)}")
            except StopIteration:
                continue

    elif args.command == "largefiles":
        for i, item in enumerate(FileScanner.find_large_files(args.dir, args.mn_size)):
            print(f"{i + 1}. {item} ({item.stat().st_size / 1024**2 :.1f} MB)")

    elif args.command == "rfiles":
        for i, item in enumerate(FileScanner.find_recent_files(args.dir, args.days)):
            print(f"{i + 1}. {item}")
    else:
        print(f"Error: wrong command ['walk','largefiles','rfiles'] and --cext")

if __name__ == "__main__":
    helper = FileScanner("File scanner", "1.0v")
    args = make_parser().parse_args()
    main(args, helper)
