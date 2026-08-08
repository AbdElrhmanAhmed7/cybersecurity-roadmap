# Day 30 Exercise
from datetime import datetime
import string
from password_generator import PasswordGenerator, _default_generator


class PasswordEntry:
    def __init__(self, website, username, password, notes="", created_at= None):
        self.website = website
        self.username = username
        self.password = password
        self.notes = notes
        self.created_at = datetime.now() if created_at is None else created_at

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value) -> bool:
        if PasswordEntry.strength_label(value) != "Weak":
            self._password = value
        else:
            raise ValueError("Weak Password!")
        
    def __str__(self):
        return f"Website '{self.website}' : {self.username}"

    def __repr__(self):
        return f"PasswordEntry('{self.website}', '{self.username}', '****', '{self.notes}', '{self.created_at}')"

    def __eq__(self, other):
        return self.created_at == other.created_at and self.website == other.website

    def __lt__(self, other):
        return self.created_at < other.created_at

    @staticmethod
    def _validate(password) -> dict:
        my_values = {
                     "upper": str.isupper, 
                     "lower": str.islower, 
                     "digit": str.isdigit,
                     "symbol": lambda x: x in string.punctuation
                     }
        score = {}

        if len(password) >= 12:
            score["length"] = True
        else:
            score["length"] = False

        for key in my_values:
            if any(my_values[key](ch) for ch in password):
                score[key] = True
            else:
                score[key] = False

        score["score"] = sum(score[key] for key in score)
        return score

    @staticmethod
    def strength_label(password) -> str:
        count = PasswordEntry._validate(password)["score"]
        if count <= 2:
            return "Weak"
        elif count <= 4:
            return "Medium"
        else:
            return "Strong"

    def is_expired(self, days=90) -> bool:
        time_diff = datetime.now() - self.created_at
        if time_diff.days > days:
            return True
        return False

    def to_dict(self) -> dict:
        return {
        "website": self.website,
        "username": self.username,
        "password": self.password,
        "notes": self.notes,
        "created_at": self.created_at.isoformat(),
    }

    @classmethod
    def from_dict(cls, data : dict):
        return cls(data["website"], data["username"], data["password"], data["notes"], datetime.fromisoformat(data["created_at"]))

    @classmethod
    def from_generated(cls, website, username, *args):
        password = _default_generator.generate(*args)
        return cls(website, username, password)
