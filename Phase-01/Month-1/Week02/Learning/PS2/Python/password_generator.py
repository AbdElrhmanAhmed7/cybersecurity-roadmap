import secrets, string, sys, argparse
from json import load, JSONDecodeError
from pathlib import Path

sys.path.append(r"D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python")
from security_toolkit import SecurityToolkit

class PasswordGenerator(SecurityToolkit):
    def __init__(self, name, version):
        super().__init__(name, version)

    def generate(
    self,
    length=16,
    upper=True,
    lower=True,
    digits=True,
    symbols=True
    ) -> str | None:
        """
        Makes a password and returns a string.
        """
        my_dict = {"upper" : (upper, string.ascii_uppercase, str.isupper), 
                   "lower": (lower, string.ascii_lowercase, str.islower), 
                   "digits" : (digits, string.digits, str.isdigit), 
                   "symbols" : (symbols, string.punctuation, lambda x: x in string.punctuation)}
        
        secure_random = secrets.SystemRandom()
        min_length = sum(my_dict[key][0] for key in my_dict)
        characters = ""

        if length < min_length:
            sys.exit(f"length can't be less than {min_length} characters.")
        for key in my_dict:
            if my_dict[key][0]:
                characters += my_dict[key][1]

        if not characters:
            return None
        
        while True:
            flag = True
            password = [secrets.choice(characters) for _ in range(length)]
            secure_random.shuffle(password)
            for key in my_dict:
                if my_dict[key][0]:
                    if not any(my_dict[key][2](ch) for ch in password):
                        flag = False
                        break
            if flag:
                return "".join(password)

    def generate_batch(self, count=1, 
                       length=16, 
                       upper=True, 
                       lower=True, 
                       digits=True, 
                       symbols=True) -> list[str] | None:
        result = []
        for _ in range(count):
            password = self.generate(length, upper, lower, digits, symbols)
            if password is not None:
                result.append(password)
            else:
                return None
        return result

    def generate_passphrase(self, list_words_path : str, words=4, separator="-", capitalize=True) -> str | None:
        try:
            with open(Path(list_words_path), "r", encoding="UTF-8") as f:
                if list_words_path.endswith("json"):
                    dictionary_words = load(f)
                elif list_words_path.endswith("txt"):
                    dictionary_words = f.read().split("\n")

                return separator.join([dictionary_words[secrets.randbelow(len(dictionary_words))].capitalize() if capitalize else dictionary_words[secrets.randbelow(len(dictionary_words))] for _ in range(words) ])
        except FileNotFoundError:
            print("File doesn't exist.")
        except JSONDecodeError:
            print("Invaild json format.")
        except KeyError:
            print("Please enter a file that doesn't contain a dict.")
            
_default_generator = PasswordGenerator("Password", "v1")

if __name__ == "__main__":
    print(_default_generator.generate_passphrase(r"D:\vs code\cybersecurity-roadmap\Phase-01\Month-1\Week02\Learning\Files\words_alpha.txt"))