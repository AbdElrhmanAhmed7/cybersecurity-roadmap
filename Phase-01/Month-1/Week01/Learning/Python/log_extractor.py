import re
from json import load, dump, JSONDecodeError
from csv import DictWriter
import sys
import argparse

sys.path.append(r"D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python")

from security_toolkit import SecurityToolkit

class LogExtractor(SecurityToolkit):
    def __init__(self, name, version):
        super().__init__(name, version)

    def extract_from_log(self, log_path) -> list[dict]:
        my_list = []
        try:
            with open(log_path, "r", encoding="UTF-8") as f:
                for line in f:
                    if LogExtractor.is_correct_format(line):
                        log_ip = re.search(r"(\d{1,3}\.){3}\d{1,3}", line).group()
                        log_timestamp = re.search(r"\d{4}-\d{2}-\d{2} \S+", line).group()
                        log_action = re.search(r"(?<=- )\w+(?= -)", line).group()
                        log_status = re.search(r"\w+$", line).group()
                        my_list.append({"ip": log_ip, "timestamp": log_timestamp,
                                                "action": log_action, "status": log_status})
        except FileNotFoundError:
            print("File is Not found.")
            sys.exit(4)

        return my_list

    def save_json(self, data, output_path) -> None:
        try:
            with open(output_path, "w", encoding="UTF-8") as f:
                dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(e)

    def load_json(self, path) -> list[dict]:
        try:
            with open(path, "r", encoding="UTF-8") as f:
                return load(f)
        except Exception as e:
            print("Something wrong has happend.")

    def summary(self, data : list[dict]) -> dict:
        total = len(data)
        try:
            unique_ips = len(set([my_dict["ip"] for my_dict in data]))
            failed_count = sum(1 for my_dict in data if my_dict["status"].upper() == "FAILED")
        except KeyError:
            print("Key is not found.")
            return {"total": "None", "unique_ips": "None", "failed_count": "None"}
        else:
            return {"total": total, "unique_ips": unique_ips, "failed_count": failed_count}

    def to_csv(self, data, output_path) -> None:
        with open(output_path, "w", encoding="UTF-8", newline="") as f:
            try:
                dict_writer = DictWriter(f, list(data[0].keys()))
            except IndexError:
                print("The data is empty.")
                sys.exit(5)
                
            dict_writer.writeheader()
            dict_writer.writerows(data)

    @staticmethod
    def is_correct_format(line) -> bool:
        if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \d{4}-\d{2}-\d{2} (?:\d{2}:?){3} - \w+ - \w+", line) is None:
            return False
        return True

def make_parser():
    parser = argparse.ArgumentParser(description="Extract data from log files")
    parser.add_argument("--log", required=True, type=str, help="The log file path")
    parser.add_argument("--output", type=str, help="The output file path", required=True)
    parser.add_argument("--summary", action="store_true", help="The summary of the program")
    return parser

def main(args, loghelper=None):
    if loghelper is None:
        loghelper = LogExtractor("Log Extractor", "1.0v")
        
    data = loghelper.extract_from_log(args.log)
    if not data:
        print(f"Incorrect format in {args.log}")
        sys.exit()

    if args.output.endswith("csv"):
        loghelper.to_csv(data, args.output)
        print(f"Saved the file to {args.output}.")
    elif args.output.endswith("json"):
        loghelper.save_json(data, args.output)
        print(f"Saved the file to {args.output}.")
    else:
        print("Incorrcet format. ['csv', 'json']")
        
    if args.summary:
        summary = loghelper.summary(data)
        for key in summary:
            print(f"{key}: {summary[key]}")

if __name__ == "__main__":
    loghelper = LogExtractor("Log Extractor", "1.0v")
    args = make_parser().parse_args()
    main(args, loghelper)
