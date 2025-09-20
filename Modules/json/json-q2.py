'''Q2. JSON Log Analyzer**

Suppose you have a JSON log file logs.json:
Write a program that:

Reads the log file.

Extracts all logs with level = ERROR.

Prints them neatly.'''

import json

try:
    with open("logs.json", "r") as f:
        logs = json.load(f)
except FileNotFoundError:
    print("Log file is not found!")
    logs = []
except json.JSONDecodeError:
    print("Logs are not in JSON format!")
    logs = []
except Exception as e:
    print(f"Something went wrong! Error: {e}")
    logs = []

error_logs = [log for log in logs if log["level"] == "ERROR"]

if error_logs:
    print("Error Logs:")
    for log in error_logs:
        print(f'{log["time"]} -> {log["message"]}')
else:
    print("No error logs found.")
