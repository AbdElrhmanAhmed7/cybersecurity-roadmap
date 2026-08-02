# Day 23 Exercise

import sys 
sys.path.append(r"D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python")
from security_toolkit import SecurityToolkit

import re
import argparse
import ipaddress

class RegexHelper(SecurityToolkit):
    def __init__(self, name, version):
        super().__init__(name, version)

    def find_ips(self, text) -> list[ipaddress.ip_address]:
        answer = []
        for ip in re.findall(r"\b[0-9a-f.-:]+\b", text, flags=re.IGNORECASE):
            try:
                answer.append(ipaddress.ip_address(ip))
            except ValueError:
                continue
        self.log(f"Found ip/s in string: {answer}.")
        return RegexHelper.remove_duplicates(answer)

    def find_emails(self, text) -> list[str]:
        answer = [email.group() for email in re.finditer(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b", text, flags=re.IGNORECASE)]
        self.log(f"Found email/s in string: {answer}.")
        return RegexHelper.remove_duplicates(answer)

    def find_urls(self, text) -> list[str]:
        answer = [url.group() for url in re.finditer(r"(https|http)\:\/\/\S+\b", text)]
        self.log(f"Found url/s in string: {answer}.")
        return answer

    def find_hashes(self, text) -> list[str]:
        answer = [hash.group() for hash in re.finditer(r"\b[a-fA-F0-9]{64}\b|\b[a-fA-F0-9]{32}\b", text)]
        self.log(f"Found hash/es in string: {answer}.")
        return answer

    @staticmethod
    def remove_duplicates(text: list[str]) -> list[str]:
        new_lst = []
        for item in text:
            if item not in new_lst:
                new_lst.append(item)
        return new_lst

def make_parser():
    parser = argparse.ArgumentParser(description="A regex helper for finding things in text.")
    parser.add_argument("--text", help="The text you want to search", type=str, required=True)
    parser.add_argument("--find", choices=["urls", "ips", "emails", "hashes"], help="Search categery", required=True)
    parser.add_argument("-v", "--verbose", action="store_true", help="for showing the logs")
    return parser

def main(args, helper=None):
    if helper is None:
        helper = RegexHelper("Regex helper", "1.0v")

    if args.find == "emails":
        print(f"Found {helper.find_emails(args.text)} email/s")
    elif args.find == "urls":
        print(f"Found {helper.find_urls(args.text)} url/s")
    elif args.find == "ips":
        print(f"Found {helper.find_ips(args.text)} ip/s")
    elif args.find == "hashes":
        print(f"Found {helper.find_hashes(args.text)} hash/es")

    if args.verbose:
        print(helper.logs)

if __name__ == "__main__":
    helper = RegexHelper("Regex helper", "1.0v")
    args = make_parser().parse_args()
    main(args, helper)


