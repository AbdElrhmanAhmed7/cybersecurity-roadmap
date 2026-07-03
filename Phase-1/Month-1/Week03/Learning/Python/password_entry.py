# Day 13

from datetime import datetime

class PasswordEntry:
    entry_count = 0
    

    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password
        self.date_created = datetime.now().date()
        self.id = PasswordEntry.entry_count
        PasswordEntry.entry_count += 1

    def __str__(self):
        return f"{self.website} : {self.username}"
    
    def __repr__(self):
        return f"PasswordEntry('{self.website}', '{self.username}', '{self.password}')"
    
    def validate(self):
        if len(self.password) > 8:
            return True
        else:
            return False
        
# Test code
e1 = PasswordEntry("gmail.com", "ahmed", "passssss@123")
e2 = PasswordEntry("github.com", "ali", "secure456")
print(e1.is_expired())