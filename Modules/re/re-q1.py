'''Q1. Log File Analyzer (Find Errors)

Suppose you are given a server log file server.log containing lines like:
Write a program that:

Reads the log file.

Uses regex to extract all ERROR messages.

Prints them along with the timestamps.
'''

import re


def analyze_log_file(file_path):
    error_pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] ERROR: (.*)"

    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                match = re.search(error_pattern, line)
                if match:
                    timestamp = match.group(1)
                    error_message = match.group(2).strip()
                    print(f"Timestamp: {timestamp} | ERROR: {error_message}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


analyze_log_file("example.log")
