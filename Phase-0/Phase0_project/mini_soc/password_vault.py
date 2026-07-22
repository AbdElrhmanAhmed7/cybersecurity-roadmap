# ---------------- Module 1 --------------------------

from security_toolkit import SecurityToolkit
from datetime import datetime
from json import dump, load, JSONDecodeError

class PasswordEntry(SecurityToolkit):
    def __init__(self, website, username, password):
        """
        Assumes: website, username, password are non-empty strings.
        Guarantees: SecurityToolkit.__init__ is called via super();
        self.website, self.username, self._password, and
        self.date_created (datetime.now().date()) are set.
        """
        super().__init__("Password Entry v1", "3.0")
        self.website = website
        self.username = username
        self._password = password
        self.date_created = datetime.now().date()

    def validate(self):
        """
        Guarantees: True only if the password is longer than 8
        characters AND contains at least one digit AND at least one
        character where char.isalnum() is False (a "symbol"). The
        existing version only checks length -- extend it here.
        """
        if len(self.get_password()) > 8 and not self.get_password().isalnum():
            return True
        return False
    
    @staticmethod
    def validate2(new_password):
        """
        Guarantees: True only if the password is longer than 8
        characters AND contains at least one digit AND at least one
        character where char.isalnum() is False (a "symbol"). The
        existing version only checks length -- extend it here.
        """
        if len(new_password) > 8 and not new_password.isalnum():
            return True
        return False
    
    @property
    def password(self):
        return self._password
    
    def is_expired(self, days=90):
        """True if self.date_created is more than `days` days in the past."""
        diff_time = datetime.now().date() - self.date_created
        if diff_time.days > days :
            return True
        return False

    def get_password(self):
        return self._password

    def set_password(self, new_password):
        """Only updates self._password if it passes validate(); otherwise raise ValueError."""
        if PasswordEntry.validate2(new_password):
            self._password = new_password
        else:
            raise ValueError("Week Password!")

    def to_dict(self):
        "Return the data as a dict"
        return {"Website": self.website, "Username": self.username, "Password": self.password, "date_created": self.date_created.isoformat()}
    
    @classmethod
    def from_dict(cls, content):
        args = list(content.values())
        constructor = cls(args[0], args[1], args[2])
        constructor.date_created = args[3]
        return constructor

    def __eq__(self, other):
        """Two entries are equal if their website matches."""
        return self.website == other.website

    def __lt__(self, other):
        """Ordering is by date_created (for sorting)."""
        return self.date_created < other.date_created

    def __len__(self):
        """Returns len(self._password)."""
        return len(self.get_password())

    def __str__(self):
        return f"{self.website} : {self.username}"

    def __repr__(self):
        """
        Must NOT include the raw password. The existing version does
        (PasswordEntry('site','user','realpass123')) -- a real
        security anti-pattern. Show a masked value instead.
        """
        return f"PasswordEntry('{self.website}','{self.username}','******')"

class PasswordVault(SecurityToolkit):
    def __init__(self, name="PasswordVault", version="1.0"):
        # TODO: super().__init__(...), plus self.entries = []
        super().__init__(name, version)
        self.entries = []

    def add_entry(self, entry):
        """Appends entry; logs the action via self.log(...)."""
        self.log(f"A New entery has been added to self.entries : {entry}")
        self.entries.append(entry)

    def find_by_website(self, website):
        """Returns the first matching entry, or None if not found."""
        for entery in self.entries:
            if website == entery.website:
                return entery
        return None

    def sorted_by_date(self):
        """Returns a NEW list of entries sorted using __lt__."""
        return sorted(self.entries)
        
    def save_results(self, path):
        try:
            result = []
            with open(path, "w") as f:
                for entery in self.entries:
                    result.append(entery.to_dict())
                dump(result, f, indent=4)
        except IOError:
            print("An Error occured.")
            return False
        return True
    
    def load_results(self, path):
        try:
            with open(path, "r", encoding="UTF-8") as f:
                for item in load(f):
                    self.entries.append(PasswordEntry.from_dict(item))
        except FileNotFoundError:
            print("The File not exist.")
            return False
        except JSONDecodeError:  
            print("Error: The file is empty or contains invalid JSON.")
            return False

class PasswordVaultIterator:
    def __init__(self, vault):
        # TODO: store vault.entries and a position counter
        self.vault = vault.entries
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        """Returns the next entry, or raises StopIteration."""
        if self.counter < len(self.vault):
            result = self.vault[self.counter]
            self.counter += 1
            return result
        raise StopIteration
    