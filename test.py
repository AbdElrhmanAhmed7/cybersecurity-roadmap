import argparse

# 1. Create a shared parent parser with add_help=False
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')
parent_parser.add_argument('--log-file', type=str, help='Path to log file')

# 2. Create a child parser that inherits the parent arguments
child_parser = argparse.ArgumentParser(
    description='A tool that inherits verbose and log-file options',
    parents=[parent_parser]  # Pass the parent(s) in a list
)
child_parser.add_argument('--custom-input', type=str, help='Child-specific input')
child_parser.set_defaults()

# Test the child parser
args = child_parser.parse_args()
