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

        min_length = sum(my_dict[key][0] for key in my_dict)
        if length < min_length:
            sys.exit(f"length can't be less than {min_length} characters.")
        characters = ""

        for key in my_dict:
            if my_dict[key][0]:
                characters += my_dict[key][1]

        if not characters:
            return None
        
        while True:
            flag = True
            password = "".join(secrets.choice(characters) for _ in range(length))
            for key in my_dict:
                if my_dict[key][0]:
                    if not any(my_dict[key][2](ch) for ch in password):
                        flag = False
                        break
            if flag:
                return password

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

    def generate_passphrase(self, words=4, separator="-", dictionary=r"..\Files\words.json", capitalize=True) -> str | None:
        try:
            with open(Path(dictionary), "r", encoding="UTF-8") as f:
                dictionary_words = load(f)
        except FileNotFoundError:
            print("File don't exist.")
        except JSONDecodeError:
            print("Invaild json format.")
        else:
            return separator.join([dictionary_words[secrets.randbelow(len(dictionary_words))].capitalize() if capitalize else dictionary_words[secrets.randbelow(len(dictionary_words))] for _ in range(words) ])

def make_parser():
    parser_chooses = argparse.ArgumentParser(add_help=False)
    parser_chooses.add_argument("--length", type=int, help="The length of the password.", default=16)
    parser_chooses.add_argument("--noupper", action="store_false", help="for making sure that the password doesn't consist of uppercase letters.", default=True)
    parser_chooses.add_argument("--nolower", action="store_false", help="for making sure that the password doesn't consist of lowercase letters.", default=True)
    parser_chooses.add_argument("--nodigits", action="store_false", help="for making sure that the password doesn't consist of digits.", default=True)
    parser_chooses.add_argument("--nosymbols", action="store_false", help="for making sure that the password doesn't consist of symbols.", default=True)

    parser = argparse.ArgumentParser(description="Making a secure password with functions.")
    subparsers = parser.add_subparsers(dest="command" ,description="The three main functions.", required=True)

    parser_password = subparsers.add_parser("password", help="For generating a secure password." , description="For generating a secure password.", parents=[parser_chooses])

    parser_batch = subparsers.add_parser("batch", description="For generating a count of passwords.", help="For generating a count of passwords.", parents=[parser_chooses])
    parser_batch.add_argument("--count", type=int, help="How many count of passwords you need", default=1)

    parser_passphrase = subparsers.add_parser("passphrase", help="Creating a secure login key made of multiple random words.", description="Creating a secure login key made of multiple random words.")
    parser_passphrase.add_argument("--dict", type=str, help="where is the dictionary file path?", required=True)
    parser_passphrase.add_argument("--words", type=int, help="how many words you want.", default=4)
    parser_passphrase.add_argument("--sep", type=str, help="What separator you want to put between?", default="-")
    parser_passphrase.add_argument("--caps", action="store_true", help="Do you wanna to capitalize the words?")
    
    return parser

def main(args, password_helper = None):
    if password_helper is None:
        password_helper = PasswordGenerator("Password Generator", "1.0v")
        
    if args.command == "password":
        print(password_helper.generate(args.length, args.noupper, args.nolower, args.nodigits, args.nosymbols))

    elif args.command == "batch":
        print(password_helper.generate_batch(args.count ,args.length, args.noupper, args.nolower, args.nodigits, args.nosymbols))

    elif args.command == "passphrase":
        print(password_helper.generate_passphrase(args.words, args.sep, args.dict, args.caps))

def check_sep_format(argv : list):
    for i in range(1, len(argv) - 1):
        curr = argv[i]
        next = argv[i+1]
        if curr == "--sep" and next == "--":
            sys.exit(f"❌ Error: You wrote '{curr}' '{next}' which won't work!\n💡 Tip: Use '{curr}={next}' instead.\n  Example: python script.py passphrase --sep={next} --dict ...")

if __name__ == "__main__":
    check_sep_format(sys.argv)
    args = make_parser().parse_args()
    helper = PasswordGenerator("Password Generator", "1.0v")
    main(args, helper)
