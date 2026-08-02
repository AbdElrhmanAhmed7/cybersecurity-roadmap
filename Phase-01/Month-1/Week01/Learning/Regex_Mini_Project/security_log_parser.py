# Extra Exercise on Regex
import sys
sys.path.append(r"D:\vs code\cybersecurity-roadmap\Phase-01\Month-1\Week01\Learning\Python")

from regexhelper import RegexHelper
import re

class SecurityLogParser(RegexHelper):
    def __init__(self, name, version):
        super().__init__(name, version)

    def extract_dates(self, text):
        dates = [date.group() for date in re.finditer(r"\b\d{4}-(0[0-9]|1[0-2])-([1-2][0-9]|3[0-1])\b", text)]
        self.log(f"Extracted date/s : {dates}")
        return dates

    def extract_times(self, text):
        times = re.findall(r"(?:[0-1][0-9]|2[0-4]):(?:[0-5][0-9]|60):(?:[0-5][0-9]|60)", text)
        self.log(f"Extracted time/s : {times}")
        return times

    def extract_levels(self, text):
        levels = re.findall(r"\b(?:INFO|WARNING|ALERT|ERROR|CRITICAL|DEBUG|ALERT)\b", text)
        self.log(f"Extracted level/s : {levels}")
        return levels

    def extract_usernames(self, text):
        usernames = re.findall(r"(?<=user )[\w.-]+", text, flags=re.IGNORECASE)
        self.log(f"Extracted username/s : {usernames}")
        return usernames

    def extract_email_domain(self, text):
        email_domain = re.findall(r"(?<=[\w.-]@)[a-z.]+", text)
        self.log(f"Extracted email domain/s : {email_domain}")
        return email_domain

    def extract_filename_from_url(self, text):
        filename_from_url = re.findall(r"[\w]+\.\w+$", "".join(self.find_urls(text)))
        self.log(f"Extracted filename from url : {filename_from_url}")
        return filename_from_url

    def extract_file_extension(self, text):
        file_extension = re.findall(r"(?<=\w\.)\w+", "\n".join(self.extract_filename_from_url(text)))
        self.log(f"Extracted file extension from url : {file_extension}")
        return file_extension

    def extract_ports(self, text):
        ips = self.find_ips(text)
        if ips:
            ports = [re.findall(rf"(?<={ip}:)\d+", text) for ip in ips]
            self.log(fr"Extracted port\s : {ports}")
        else:
            return []
        return ports

    def extract_start_with_alert(self, text):
        start_with_alert = re.findall(r"^ALERT", text, flags=re.MULTILINE)
        self.log(fr"Extracted line\s start with ALERT : {start_with_alert}")
        return start_with_alert

    @staticmethod
    def ip_type(ip : str):
        if not SecurityLogParser.validate_ip(ip):
            return "Not an ip."
        
        ip_classes = {"Class A": ("10.0.0.0", "10.255.255.255"), "Class B": ("172.16.0.0", "172.31.255.255"), "Class C": ("192.168.0.0", "192.168.255.255")}
        ip = list(map(int,ip.split(".")))
        for ip_class in ip_classes:
            start_ip = list(map(int,ip_classes[ip_class][0].split(".")))
            end_ip = list(map(int,ip_classes[ip_class][1].split(".")))
            flag = True
            for i in range(4):
                if end_ip[i] < ip[i] or ip[i] < start_ip[i]:
                    flag = False
                    break
            if flag:
                return f"Private ip of type: {ip_class}"
        return f"Public ip"

    @staticmethod
    def detect_weak_passwords(text):
        return re.findall(r"(?<=password=)[\w!@#$%^&*._]+",text)

    def detect_credit_cards(self,text):
        credit_cards = [card.group() for card in re.finditer(r"\b(\d{4})([\s-]?)(\d{4})\2(\d{4})\2(\d{4})\b", text)]
        self.log(f"Found {len(credit_cards)} credit cards in logs.")
        return credit_cards

    @staticmethod
    def detect_windows_path(text):
        return re.findall(r"[A-Z\s]:\\[\w\\.\s]+", text, flags=re.IGNORECASE)

    @staticmethod
    def detect_linux_path(text):
        return re.findall(r"\/[-.\w\/]+", text)

    @staticmethod
    def detect_mac_address(text):
        return re.findall(r"[0-9A-F:-]{17}", text, flags=re.IGNORECASE)

    def analyze(self, text):
        my_dict = {"Ips": self.find_ips(text), "Emails": self.find_emails(text), 
                   "Urls": self.find_urls(text), "Hashes" : self.find_hashes(text),
                   "Dates": self.extract_dates(text), "Times": self.extract_times(text),
                   "Log Levels": self.extract_levels(text), "Domains": self.extract_email_domain(text),
                   "Ports": self.extract_ports(text)}
        if not my_dict:
            raise ValueError("Invalid input.")
        return my_dict

