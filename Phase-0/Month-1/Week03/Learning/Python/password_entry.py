# Day 13 (Added some in start of Week 4)

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
    
    def __eq__(self, other):
        return self.website == other.website
    
    def __lt__(self, other):
        return self.date_created < other.date_created
    
    def __len__(self):
        return len(self.password)
    
    def validate(self):
        if len(self.password) > 8:
            return True
        else:
            return False
        

