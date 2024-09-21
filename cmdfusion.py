#!/usr/bin/env python3
import argparse
import subprocess

# Define command aliases
ALIASES = {
    "list_files": "ls -la",
    "search_logs": "grep 'ERROR' /var/log/syslog",
}

def run_command(command):
    """Execute a command in the shell."""
    subprocess.run(command, shell=True, check=True)

def main():
    parser = argparse.ArgumentParser(description="Shorten complex CLI commands into single commands.")
    parser.add_argument("alias", help="The alias for the command.")
    parser.add_argument("params", nargs='*', help="Parameters for the command.")
    
    args = parser.parse_args()
    
    command = ALIASES.get(args.alias)
    
    if not command:
        print(f"No alias found for '{args.alias}'")
        return
    
    # Simple parameter replacement
    for i, param in enumerate(args.params):
        command = command.replace(f"{{param{i}}}", param)
    
    print(f"Running command: {command}")
    run_command(command)

if __name__ == "__main__":
    main()
