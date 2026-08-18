from pathlib import Path
import stat, argparse, sys
from json import dump


class FilePermissionsChecker:
        def scan(self, directory):
                for file_path in Path(directory).rglob("*"):
                        file_permission = stat.filemode(Path(file_path).stat().st_mode)
                        yield str(file_path), file_permission, "s" == file_permission[3].lower()

        def suid_find(self, start="/"):
                suid_list = []
                for file_path,file_permission, is_suid in self.scan(start):
                        if is_suid:
                                suid_list.append(file_path)
                return suid_list

        def world_writable(self, directory):
                world_writable_list = []
                for file_path, file_permission, is_suid in self.scan(directory):
                        if file_permission[8] == "w":
                                world_writable_list.append(file_path)
                return world_writable_list
                                
        def report_json(self, data, output_path):
                with open(output_path, "w", encoding="UTF-8") as f:
                        dump(data, f, indent=4)

FILE_CHECKER = FilePermissionsChecker()

def make_parser():
        parser = argparse.ArgumentParser(description="File Permissions Checker")
        parser.add_argument("--dir", required=True, type=str, help="Directory to search", const=r".", nargs="?")
        parser.add_argument("--count", type=int, help="Number of files you want to get")
        parser.add_argument("--check", choices=["suid", "writable"], help="What you want to do", dest="command")
        parser.add_argument("--output", help="Output file ONLY JSON is accepted")

        return parser

def main(args):

        if args.count is not None and args.command is not None:
                print("Please use --count with --dir only")
                sys.exit(2)

        if args.command is None:
                scanner = FILE_CHECKER.scan(args.dir)
                scan_dir = []
                for i in range(10 if args.count is None else args.count):
                        try:
                                scan_dir.append(next(scanner))
                        except StopIteration:
                                continue
                command_result = scan_dir

        elif args.command is not None:
                if args.command == "suid":
                        command_result = FILE_CHECKER.suid_find(args.dir)
                else:
                        command_result = FILE_CHECKER.world_writable(args.dir)

        if args.output is not None:
                if args.output.endswith("json"):
                        FILE_CHECKER.report_json(command_result, args.output)
                        print("File saved successfully !")
                else:
                        print("Please enter a file that is .json format")
        else:
                print(command_result)


if __name__ == "__main__":
        main(make_parser().parse_args())