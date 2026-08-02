import sys
sys.path.append(r"D:\vs code\cybersecurity-roadmap\Phase-01\Month-1\Week01\Learning\Python")

from filescanner import make_parser as parser_scanner, main as main_scanner
from log_extractor import make_parser as parser_log, main as main_log
from regexhelper import make_parser as parser_regex, main as main_regex
import argparse

def make_cli():
    parser = argparse.ArgumentParser(description="PS1 - Make three files in one CLI")
    subparsers= parser.add_subparsers(dest="command", help="The three commands", required=True)

    # File scanner
    parser_file = subparsers.add_parser("scan", parents=[parser_scanner()], add_help=False, description="For scanning files.")
    parser_file.set_defaults(main= main_scanner)

    # Log Extractor
    parser_extractor = subparsers.add_parser("logs", parents=[parser_log()], add_help=False, description="For Extracting data from log files.")
    parser_extractor.set_defaults(main=main_log)

    # Regex
    parser_search = subparsers.add_parser("regex", parents=[parser_regex()], add_help=False, description="For Searching in files.")
    parser_search.set_defaults(main=main_regex)

    args = parser.parse_args()

    args.main(args)

if __name__ == "__main__":
    make_cli()