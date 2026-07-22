"""
main.py -- MiniSOC CLI entry point.

Ties together PasswordVault, LogAnalyzer, and IncidentTracker. Three
pieces of state stay alive for the whole session, held as local
variables inside main() and passed into handlers as parameters
(no globals):
    vault              -- a PasswordVault instance
    incident_log       -- an IncidentLog instance
    loaded_log_entries -- the (timestamp, level, message) tuples from
                          the last file loaded with option 3

Each menu option is its own small function -- keeps main() itself to
just "loop, read a choice, dispatch." Fill in the TODOs; the loop
below is already complete since it's just plumbing.
"""
from pathlib import Path
from password_vault import *
from log_analyzer import *
from incident_tracker import *


MENU = """
=== MiniSOC ===
1) Add a password entry
2) List vault (sorted by date)
3) Load a log file
4) Auto-create incidents from the loaded log
5) List incidents (sorted by priority)
6) Save everything to JSON
7) Load everything from JSON
8) Exit
Choose an option: """


def handle_add_password(vault : PasswordVault):
    """
    Prompts for website/username/password, builds a PasswordEntry,
    and adds it to vault. Catch ValueError from a weak password (see
    PasswordEntry.set_password / validate) and print a message
    instead of crashing -- don't add the entry if it's rejected.
    """
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")
    entery = PasswordEntry(website, username, password)
    if entery.validate():
        vault.add_entry(entery)
        print("Password added successfully.")
    else:
        print("Week password!")


def handle_list_vault(vault : PasswordVault):
    """Prints every entry in vault.sorted_by_date(), one per line."""
    for i, entery in enumerate(vault.sorted_by_date()):
        print(f"{i}. {entery}")


def handle_load_log():
    """
    Prompts for a filename. Reads it with read_log_lines, parses each
    line with parse_log_line -- if a line raises LogFormatError, print
    which line was bad and skip it, don't crash the whole load.
    Filters the parsed lines down to WARNING/ERROR with
    filter_by_level. Catches FileNotFoundError for a bad filename and
    returns [] in that case.
    Returns: the list of (timestamp, level, message) tuples.
    """
    file_name = Path.absolute(Path(input("File name : ")))
    
    parsed_lines = []
    try:
        for line in read_log_lines(file_name):
            parsed_lines.append(parse_log_line(line))
    except LogFormatError:
        print("An error here ", line)
    except FileNotFoundError:
        print("The file is not found.")
        return []
            
    return filter_by_level(parsed_lines)

def handle_create_incidents(loaded_log_entries, incident_log: IncidentLog):
    """
    Runs open_incident_from_log over every entry in
    loaded_log_entries, calling incident_log.add_incident(...) for
    every non-None result. Prints how many incidents were created
    versus how many log lines were skipped (no keyword match).
    """
    created = 0
    skipped = 0
    for entery in loaded_log_entries:
        open_incident_entery = open_incident_from_log(entery)
        if open_incident_entery != None:
            incident_log.add_incident(open_incident_entery)
            created += 1
        else:
            skipped += 1
    print(f"Incidents Created : {created}")
    print(f"Incidents skipped : {skipped}")


def handle_list_incidents(incident_log : IncidentLog):
    """Prints sort_incidents_by_priority(incident_log.incidents), one per line."""
    for i, incident in enumerate(sort_incidents_by_priority(incident_log.incidents)):
        print(f"{i}. {incident}")

def make_dir(file_path):
    file_path.parent.mkdir(parents=True, exist_ok=True)

def handle_save(vault : PasswordVault, incident_log: IncidentLog):
    """Prompts for two paths (or use fixed data/vault.json, data/incidents.json)
    and calls vault.save_results(...) and incident_log.save_results(...)."""
    vault_path = Path.absolute(Path("data/vault.json"))
    incident_path = Path.absolute(Path("data/incidents.json"))
    make_dir(vault_path)
    make_dir(incident_path)
    # vault_path = path.abspath(Path(input("Vault path: ")))
    # incident_path = path.abspath(Path(input("Incident path: ")))
    vault.save_results(vault_path)
    incident_log.save_results(incident_path)


def handle_load(vault : PasswordVault, incident_log: IncidentLog):
    """Same idea as handle_save, but calling load_results on both."""
    # vault_path = path.abspath(Path(input("Vault path: ")))
    # incident_path = path.abspath(Path(input("Incident path: ")))
    vault_path = Path.absolute(Path("data/vault.json"))
    incident_path = Path.absolute(Path("data/incidents.json"))
    vault.load_results(vault_path)
    incident_log.load_results(incident_path)


def main():
    vault = PasswordVault()
    incident_log = IncidentLog()
    loaded_log_entries = []

    while True:
        choice = input(MENU).strip()
        print()

        if choice == "1":
            handle_add_password(vault)
        elif choice == "2":
            handle_list_vault(vault)
        elif choice == "3":
            loaded_log_entries = handle_load_log()
        elif choice == "4":
            handle_create_incidents(loaded_log_entries, incident_log)
        elif choice == "5":
            handle_list_incidents(incident_log)
        elif choice == "6":
            handle_save(vault, incident_log)
        elif choice == "7":
            handle_load(vault, incident_log)
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Not a valid option, try again.")


if __name__ == "__main__":
    main()