from password_entry import PasswordEntry
from json import load, dump, JSONDecodeError
from datetime import datetime
from pathlib import Path
from shutil import copy2
import webbrowser
import re
from abc import ABC, abstractmethod

class PasswordVault:
    def __init__(self, vault_path, storage):
        self._vault = Path(vault_path)
        self._entries = []
        if any(cls == storage for cls in VaultStorage.__subclasses__()):
            self._storage = storage(self)
        else:
            raise ValueError(f"Please enter correct storage class {", ".join([cls.__name__ for cls in VaultStorage.__subclasses__()])}")

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)

    # Review
    def __contains__(self, website):
        return self.get(website) is not None
    
    # Review
    def __getitem__(self, website : str):
        return self.get(website)

    def __repr__(self):
        return f"PasswordVault('{self.vault}', entries={[entry for entry in self.entries]})"

    def __bool__(self):
        return bool(len(self.entries))

    def save(self):
        self.storage.save()

    def load(self):
        self.storage.load()

    @property
    def storage(self):
        return self._storage
    
    @property
    def vault(self):
        return self._vault

    @property
    def entries(self):
        return self._entries
        
    def add(self, entry):
        self.entries.append(entry)

    def get(self, website):
        for entery in self.entries:
            if entery.website == website:
                return entery
        return None

    def delete(self, website):
        for i in range(len(self.entries)):
            if self.entries[i].website == website:
                del self.entries[i]
                return True
        return False

    def list_all(self):
        return self.entries[:]

    def search(self, value):
        answer = []
        for entry in self.entries:
            if value.lower() in entry.website.lower() or value.lower() in entry.username.lower():
                answer.append(entry)
        return answer

    def to_dict(self) -> list[dict]:
        return [entry.to_dict() for entry in self.entries]

    def get_expired(self, days=90):
        return [entry for entry in self.entries if entry.is_expired(days)]

    def backup(self, backup_dir):
        try:
            dst = Path(backup_dir)
            dst.mkdir(exist_ok=True, parents=True)
            copy2(self.vault, dst / f"vault_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.{self.storage.extension}")
        except FileNotFoundError:
            print("File is Not found.")
        else:
            print("Backup is Done!")

    @staticmethod
    def is_full_url(website, url_regex=re.compile(r"""
        ^(?:http|ftp)s?://  # http:// or https:// or ftp:// or ftps://
        (?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|  # domain...
        localhost|  # localhost...
        \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})  # ...or ip
        (?::\d+)?  # optional port
        (?:/?|[/?]\S+)$""", re.IGNORECASE | re.VERBOSE
        )):
        return re.match(url_regex, website) is not None

    def open_browser(self, website : str):
        if PasswordVault.is_full_url(website):
            webbrowser.open(website)
        else:
            print("Please enter the full url.")

    @classmethod
    def from_file(cls, file_path, storage):
        new_obj = cls(file_path, storage)
        new_obj.load()
        return new_obj

class VaultStorage(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass

class JSONStorage(VaultStorage):
    def __init__(self, vault : PasswordVault):
        self.my_vault = vault
        self.extension = "json"

    def save(self):
        with open(self.my_vault.vault, "w", encoding="UTF-8") as f:
            dump(self.my_vault.to_dict(), f, indent=4)

    def load(self):
        self.my_vault.entries.clear()
        try:
            with open(self.my_vault.vault, "r", encoding="UTF-8") as f:
                for entry_data in load(f):
                    self.my_vault.entries.append(PasswordEntry.from_dict(entry_data))
        except FileNotFoundError:
            print(f"No existing vault found at '{self.my_vault.vault}' — starting with an empty vault.")
        except JSONDecodeError:
            print("Invalid json format.")

