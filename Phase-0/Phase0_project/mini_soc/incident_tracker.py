# ------------------ Module 3 ---------------------------
from security_toolkit import SecurityToolkit
from algorthims import merge_sort
from json import dumps,dump,load,JSONDecodeError


class Analyst:
    def __init__(self, name, email):
        self.name = name
        self._email = email
        self._active_cases = []

    def assign_case(self, case):
        """
        Adds a case name to self._active_cases
        """
        self._active_cases.append(case)

    def get_email(self):
        "Return the self.email"
        return self._email
    
    def set_email(self, value):
        """
        Sets the self.email to the new value
        """
        if not "@" in value:
            raise ValueError("Invalid email.")
        self._email = value

    def __repr__(self):
        return f"Analyst('{self.name}', '{self.get_email()}')"


class SecurityIncident(SecurityToolkit):
    """
    Same hierarchy as the existing soc_incident_system.py, but this
    class now also inherits from SecurityToolkit. Keep
    total_incidents_logged, the severity property, and the existing
    subclasses (PhishingIncident, MalwareIncident,
    UnauthorizedAccessIncident) as they are -- just add the
    SecurityToolkit inheritance and call super().__init__() from both
    SecurityIncident and SecurityToolkit correctly.
    """
    # TODO: retrofit
    total_incidents_logged = 0
    organization_name = "Alien Inc."

    def __init__(self, incident_title, assigned_analyst):
        super().__init__("Incident v1", "1.0")
        self.incident_title = incident_title
        self._severity = None
        self.assigned_analyst = assigned_analyst
        self.__incident_id = self.__generate_incident_id()

        SecurityIncident.total_incidents_logged += 1

    @property
    def severity(self):
        return self._severity
    
    @property
    def incident_id(self):
        return self.__incident_id
    
    @severity.setter
    def severity(self, value):
        if not SecurityIncident.is_valid_severity(value):
            raise ValueError("Incorrect severity type.")
        self._severity = value

    def __generate_incident_id(self):
        return "INC-" + str(SecurityIncident.total_incidents_logged).zfill(4)
    
    @staticmethod
    def is_valid_severity(level):
        valid_values = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        if level not in valid_values:
            return False
        return True
    
    def _base_priority_score(self):
        priority = {"LOW": 2.0, "MEDIUM": 4.5, "HIGH": 7.5, "CRITICAL": 10}
        return priority[self.severity]
    
    def to_dict(self):
        result = {"cls" : type(self).__name__,
                  "Incident ID" : self.incident_id, "Incident_name" : self.incident_title,
                  "Analyst name" : self.assigned_analyst.name, 
                  "Analyst email" : self.assigned_analyst.get_email(),
                  "Priority score": self._base_priority_score()
                }
        if result["cls"] == "PhishingIncident":
            result["num_emails"] = self.num_emails_sent
        elif result["cls"] == "MalwareIncident":
            result["is_ransomware"] = self.is_ransomware
        elif result["cls"] == "UnauthorizedAccessIncident":
            result["affected_system"] = self.affected_system
        return result
    
    @staticmethod
    def from_dict(content : dict) -> PhishingIncident | MalwareIncident | UnauthorizedAccessIncident:
        analyst = Analyst(content["Analyst name"], content["Analyst email"])
        if content["cls"] == "PhishingIncident":
            return PhishingIncident(content["Incident_name"], analyst, content["num_emails"])
        elif content["cls"] == "MalwareIncident":
            return MalwareIncident(content["Incident_name"], analyst, content["is_ransomware"])
        elif content["cls"] == "UnauthorizedAccessIncident":
            return UnauthorizedAccessIncident(content["Incident_name"], analyst, content["affected_system"])
            
    def __str__(self):
        return f"Incident_id : {self.incident_id}, Name : {self.incident_title}, priority_score : {self._base_priority_score()}"
    
    def __repr__(self):
        return f"('{self.incident_id}', '{self.assigned_analyst}', '{self._base_priority_score()}')"


class PhishingIncident(SecurityIncident):
    def __init__(self, incident_title, assigned_analyst, num_emails_sent):
        super().__init__(incident_title, assigned_analyst)
        self.num_emails_sent = num_emails_sent

    def _base_priority_score(self):
        priority = {"LOW": 2.0, "MEDIUM": 4.5, "HIGH": 7.5, "CRITICAL": 10, "NONE": 0}
        self.assess_severity()
        return priority[self.severity]

    def assess_severity(self):
        if 0 <= self.num_emails_sent <= 50:
            self.severity = "LOW"
        elif 50 <= self.num_emails_sent <= 200:
            self.severity = "MEDIUM"
        elif 200 <= self.num_emails_sent <= 1000:
            self.severity = "HIGH"
        elif 1000 <= self.num_emails_sent:
            self.severity = "CRITICAL"
            
    def generate_report(self):
        return dumps([self._base_priority_score(), self.num_emails_sent])
    
SYSTEM_ANALYST = Analyst("Auto-Triage", "system@minisoc.local")

class MalwareIncident(SecurityIncident):
    def __init__(self, incident_title, assigned_analyst, is_ransomware):
        super().__init__(incident_title, assigned_analyst)
        self.is_ransomware = is_ransomware

    def _base_priority_score(self):
        priority = {"LOW": 2.0, "MEDIUM": 4.5, "HIGH": 7.5, "CRITICAL": 10, "NONE": 0}
        self.assess_severity()
        return priority[self.severity]

    def assess_severity(self):
        if self.is_ransomware:
            self.severity = "HIGH"
        else:
            self.severity = "MEDIUM"

    def generate_report(self):
        return dumps(self._base_priority_score())

class UnauthorizedAccessIncident(SecurityIncident):
    def __init__(self, incident_title, assigned_analyst, affected_system):
        super().__init__(incident_title, assigned_analyst)
        self.affected_system = affected_system

    def _base_priority_score(self):
        priority = {"LOW": 2.0, "MEDIUM": 4.5, "HIGH": 7.5, "CRITICAL": 10, "NONE": 0}
        self.assess_severity()
        return priority[self.severity]

    def assess_severity(self):
        if "db" in self.affected_system.lower() or "admin" in (self.affected_system).lower():
            self.severity = "CRITICAL"
        else:
            self.severity = "MEDIUM"

    def generate_report(self):
        return dumps(self._base_priority_score())



def open_incident_from_log(log_entry):
    """
    Assumes: log_entry is a (timestamp, level, message) tuple where
    level is 'WARNING' or 'ERROR'.
    Guarantees: returns the right Incident subclass based on keywords
    in `message` (see mapping below), or None if no keyword matches.
    """

    if any(message in log_entry[2].lower() for message in ["phishing", "email"]):
        num_emails = ""
        for ch in log_entry[2]:
            if ch.isdigit():
                num_emails += ch
        if not num_emails:
            num_emails = "1"
        return PhishingIncident("Phishing emails", SYSTEM_ANALYST, int(num_emails))
    elif any(message in log_entry[2].lower() for message in ["malware", "ransomware"]):
        is_ransomware = False
        if "ransomware" in log_entry[2].lower():
            is_ransomware = True
        return MalwareIncident("A Malware has found.", SYSTEM_ANALYST, is_ransomware)
    elif any(message in log_entry[2].lower() for message in ["unauthorized", "access"]):
        return UnauthorizedAccessIncident("UnauthorizedAccess", SYSTEM_ANALYST, log_entry[2])
    else:
        return None

def sort_incidents_by_priority(incidents, reverse=False):
    """
    SecurityIncident has no __lt__, so merge_sort(incidents) directly
    will crash trying to compare two incident objects. Wrap each one in
    a tuple first: merge_sort([(inc._base_priority_score(), inc.incident_id, inc)
    for inc in incidents]), then pull `inc` back out of each result. The
    incident_id is a tie-breaker -- without it, two incidents with an
    identical score would still make Python try to compare the objects
    directly.
    """
    new_incidents = merge_sort([(incident._base_priority_score(), incident.incident_id, incident) for incident in incidents])
    if reverse:
        return [inc[2] for inc in new_incidents][::-1]
    return [inc[2] for inc in new_incidents]

class IncidentLog(SecurityToolkit):
    def __init__(self, name="IncidentLog", version="1.0"):
        # TODO: super().__init__(...), plus self.incidents = []
        super().__init__(name , version)
        self.incidents = []

    def add_incident(self, incident):
        """Appends incident; logs the action via self.log(...)."""
        self.log(incident)
        self.incidents.append(incident)

    
    def save_results(self, path):
        """
        Overrides SecurityToolkit.save_results -- must serialize
        self.incidents (each incident's to_dict() should include a
        "type" field like "PhishingIncident" so load_results knows
        which class to rebuild), not self.logs. Same reasoning as
        PasswordVault in the project brief section 1.5.
        """
        try:
            result = []
            with open(path, "w") as f:
                for incident in self.incidents:
                    result.append(incident.to_dict())
                dump(result, f, indent=4)
        except IOError:
            print("An Error occured.")
            return False
        return True

    def load_results(self, path):
        """Reconstructs self.incidents from JSON via from_dict()."""
        try:
            with open(path, "r", encoding="UTF-8") as f:
                for line in load(f):
                    self.add_incident(SecurityIncident.from_dict(line))
        except FileNotFoundError:
            print("The File not exist.")
            return False
        except JSONDecodeError:  
            print("Error: The file is empty or contains invalid JSON.")
            return False
        return True
