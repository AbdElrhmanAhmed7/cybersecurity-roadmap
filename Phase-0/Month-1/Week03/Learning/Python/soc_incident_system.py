## Day 16 A-(Exercise everything i learnt in OOP)
# (https://www.youtube.com/watch?v=iLRZi0Gu8Go&t=4380s)

from json import dumps

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

class SecurityIncident:
    total_incidents_logged = 1
    organization_name = "Alien Inc."

    def __init__(self, incident_title, assigned_analyst): 
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
        return "INC-" + str(self.total_incidents_logged).zfill(4)
    
    @staticmethod
    def is_valid_severity(level):
        valid_values = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        if level not in valid_values:
            return False
        return True
    
    # Review (Abstract methods)
    def _base_priority_score(self):
        priority = {"LOW": 2.0, "MEDIUM": 4.5, "HIGH": 7.5, "CRITICAL": 10}
        return priority[self.severity]
    
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




    
