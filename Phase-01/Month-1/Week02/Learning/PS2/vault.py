import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "Python"))

from password_generator import PasswordGenerator,_default_generator
from password_entry import PasswordEntry
from password_vault import *
import argparse

# ------------- CLI of password_generator.py ------------------------
def password_chooses():
    parser_chooses = argparse.ArgumentParser(add_help=False)
    parser_chooses.add_argument("--length", type=int, help="The length of the password.", default=16)
    parser_chooses.add_argument("--noupper", action="store_false", help="for making sure that the password doesn't consist of uppercase letters.", default=True)
    parser_chooses.add_argument("--nolower", action="store_false", help="for making sure that the password doesn't consist of lowercase letters.", default=True)
    parser_chooses.add_argument("--nodigits", action="store_false", help="for making sure that the password doesn't consist of digits.", default=True)
    parser_chooses.add_argument("--nosymbols", action="store_false", help="for making sure that the password doesn't consist of symbols.", default=True)

    return parser_chooses
    
def make_parser_generator():

    parser = argparse.ArgumentParser(description="Making a secure password with functions.")
    subparsers = parser.add_subparsers(dest="command_gen", description="The three main functions.", required=True)

    parser_password = subparsers.add_parser("password", help="For generating a secure password." , description="For generating a secure password.", parents=[password_chooses()])

    parser_batch = subparsers.add_parser("batch", description="For generating a count of passwords.", help="For generating a count of passwords.", parents=[password_chooses()])
    parser_batch.add_argument("--count", type=int, help="How many count of passwords you need", default=1)

    parser_passphrase = subparsers.add_parser("passphrase", help="Creating a secure login key made of multiple random words.", description="Creating a secure login key made of multiple random words.")
    parser_passphrase.add_argument("--dict", type=str, help="where is the dictionary file path?", required=True)
    parser_passphrase.add_argument("--words", type=int, help="how many words you want.", default=4)
    parser_passphrase.add_argument("--sep", type=str, help="What separator you want to put between?", default="-")
    parser_passphrase.add_argument("--caps", action="store_true", help="Do you wanna to capitalize the words?")
    
    return parser

def main_generator(args):
        
    if args.command_gen == "password":
        print(_default_generator.generate(args.length, args.noupper, args.nolower, args.nodigits, args.nosymbols))

    elif args.command_gen == "batch":
        print(_default_generator.generate_batch(args.count ,args.length, args.noupper, args.nolower, args.nodigits, args.nosymbols))

    elif args.command_gen == "passphrase":
        print(_default_generator.generate_passphrase(args.dict, args.words, args.sep, args.caps))

def check_sep_format(argv : list):
    for i in range(1, len(argv) - 1):
        curr = argv[i]
        next = argv[i+1]
        if curr == "--sep" and next == "--":
            sys.exit(f"❌ Error: You wrote '{curr}' '{next}' which won't work!\n💡 Tip: Use '{curr}={next}' instead.\n  Example: python script.py passphrase --sep={next} --dict ...")

# --------------------- CLI of password_entry.py --------------------------
def make_parser_entry():
    parser = argparse.ArgumentParser(description="Creating PasswordEntry objects", parents=[password_chooses()])
    parser.add_argument("--website",type=str, help="website name", required=True)
    parser.add_argument("--username",type=str, help="username", required=True)

    return parser

def main_entry(args):
    return PasswordEntry.from_generated(args.website, args.username, args.length, args.noupper, args.nolower, args.nodigits, args.nosymbols)

# ---------------- CLI of password_vault.py --------------------------------
def make_parser_vault():
    parser = argparse.ArgumentParser(description="The admin to all PasswordEntry objects")
    parser.add_argument("--file", type=str, default="vault.json", help="Path to vault file")
    parser.add_argument("--storage",type=str, choices=[cls.__name__ for cls in VaultStorage.__subclasses__()], default="JSONStorage", help="The storage type")
    subparsers = parser.add_subparsers(help="For vault.py", dest="command_vault", required=True)

    parser_add = subparsers.add_parser("add", description="Adding a entry to the vault", parents=[make_parser_entry()], add_help=False)
    group = parser_add.add_mutually_exclusive_group(required=True)
    group.add_argument("--password",type=str, help="Enter password manually")
    group.add_argument("--generate", help="Auto-generate a password", action="store_true")

    parser_get = subparsers.add_parser("get", description="Searching an entry by its website name")
    parser_get.add_argument("--website", type=str, help="The website you want to search", required=True)

    parser_list = subparsers.add_parser("list", help="Listing all entries")

    parser_delete = subparsers.add_parser("delete", help="Deleting an entry by its website")
    parser_delete.add_argument("--website", type=str, help="The website you want to delete", required=True)

    parser_search = subparsers.add_parser("search", help="Searching all entries by its name or username")
    parser_search.add_argument("--query", help="The thing you want to search in name or username", required=True)

    parser_expired = subparsers.add_parser("expired", help="Search entries for expired ones")
    parser_expired.add_argument("--days", type=int, help="The number of days you want to search", default=90)

    parser_backup = subparsers.add_parser("backup", help="Backing up vault file")
    parser_backup.add_argument("--dir",type=str , help="The directory you want to save the backup", required=True)

    parser_open = subparsers.add_parser("open", help="Opening a website in your default browser")
    parser_open.add_argument("--website", required=True ,help="The website you want to open")

    return parser

def main_vault(args):
    main_vault = PasswordVault.from_file(args.file, [cls for cls in VaultStorage.__subclasses__() if cls.__name__ == args.storage][0])
    MODIFYING_COMMANDS = {"add", "delete"}

    if args.command_vault == "add":
        try:
            if args.generate:
                main_vault.add(main_entry(args))
            else:
                    main_vault.add(PasswordEntry(args.website, args.username, args.password))
        except ValueError:
            print("Weak Password!")
            sys.exit(3)
        print("Added successfully!")

    elif args.command_vault == "get":
        get_output = main_vault.get(args.website)
        if get_output is not None:
            print(get_output)
        else:
            print(f"{args.website} is not found in any entry website name")

    elif args.command_vault == "list":
        print(main_vault.list_all())

    elif args.command_vault == "delete":
        if main_vault.delete(args.website):
            print("Deleted successfully!")
        else:
            print(f"{args.website} is not found")

    elif args.command_vault == "search":
        search_output = main_vault.search(args.query)
        if search_output:
            print(search_output)
        else:
            print(f"{args.query} is not found")

    elif args.command_vault == "expired":
        expired_output = main_vault.get_expired(args.days)
        if expired_output:
            print(expired_output)
        else:
            print("No entry is expired !!")

    elif args.command_vault == "backup":
        main_vault.backup(args.dir)

    elif args.command_vault == "open":
        main_vault.open_browser(args.website)

    if args.command_vault in MODIFYING_COMMANDS:
        main_vault.save()

def main():
    parser = argparse.ArgumentParser(description="My PS2 Project")
    subparsers = parser.add_subparsers(dest="command", required=True)

    password_parser = subparsers.add_parser("generate", add_help=False, parents=[make_parser_generator()])
    password_parser.set_defaults(main=main_generator)

    vault_parser = subparsers.add_parser("vault", add_help=False, parents=[make_parser_vault()])
    vault_parser.set_defaults(main=main_vault)

    check_sep_format(sys.argv)

    args = parser.parse_args()
    args.main(args)

if __name__ == "__main__":
    main()
    