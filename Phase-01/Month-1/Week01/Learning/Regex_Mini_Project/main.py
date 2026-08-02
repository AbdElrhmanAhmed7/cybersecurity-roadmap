from security_log_parser import *

def security_report(file_content, parser: SecurityLogParser):
    result = parser.analyze(file_content)
    print("=" * 33 + " Security Report " + "=" * 33)
    print(f"IPs Found      : {len(result["Ips"])}")
    print(f"Emails Found   : {len(result["Emails"])}")
    print(f"URLs Found     : {len(result["Urls"])}")
    print(f"Hashes Found   : {len(result["Hashes"])}")
    print(f"Ports          : {len(result["Ports"])}")
    print(f"Times          : {len(result["Dates"])}")

def main():
    parser = SecurityLogParser("SecurityLogParser", "1.0")
    with open(input("Please enter you file path: "), "r", encoding="UTF-8") as f:
        security_report(f.read(), parser)

main()