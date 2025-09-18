'''Q3. Log File Analyzer (File Handling + os + Exception Handling)

Problem:

Given a folder containing multiple log files (.log), write a program to:

Read all .log files.

Count occurrences of “ERROR”, “WARNING”, and “INFO”.

Write a summary report into summary.txt.

Handle: missing log files, empty files, and encoding errors.'''


import os


def analyze_log_files(log_folder_path):
    error_count = 0
    warning_count = 0
    info_count = 0

    if not os.path.isdir(log_folder_path):
        print("Log folder does not exist.")
        return

    log_files = [f for f in os.listdir(log_folder_path) if f.endswith('.log')]

    if not log_files:
        print("No .log files found in the specified folder.")
        return

    for log_file in log_files:
        log_file_path = os.path.join(log_folder_path, log_file)

        try:
            with open(log_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                for line in lines:
                    line = line.strip()

                    if 'ERROR' in line:
                        error_count += 1
                    elif 'WARNING' in line:
                        warning_count += 1
                    elif 'INFO' in line:
                        info_count += 1

        except FileNotFoundError:
            print(f"File {log_file} not found.")
        except UnicodeDecodeError:
            print(f"Encoding error in file: {log_file}")
        except Exception as e:
            print(f"An error occurred while processing {log_file}: {e}")

    summary_path = os.path.join(log_folder_path, 'summary.txt')
    with open(summary_path, 'w') as summary_file:
        summary_file.write(f"Log Analysis Summary\n")
        summary_file.write(f"====================\n")
        summary_file.write(f"ERROR count: {error_count}\n")
        summary_file.write(f"WARNING count: {warning_count}\n")
        summary_file.write(f"INFO count: {info_count}\n")

    print(f"Summary report has been written to {summary_path}")


log_folder = os.path.join(os.getcwd(), "Modules", "os", "log files")
analyze_log_files(log_folder)
