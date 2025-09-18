'''Q2.Backup and Restore Utility (OOP + os + shutil)

Problem:
Design a backup tool:

Class BackupManager:

backup(source_dir, backup_dir) → copies all files.

restore(backup_dir, restore_dir) → restores files.

Use os.walk() to handle nested folders.

Add error handling for:

Missing source directory.

Permission issues.

Maintain a log file of operations.'''

import os
import shutil


class BackupManager:
    def __init__(self, log_file="backup_restore.log"):
        self.log_file = log_file

    def _log(self, message):
        with open(self.log_file, "a") as log:
            log.write(message + "\n")

    def backup(self, source_dir, backup_dir):
        if not os.path.exists(source_dir):
            print(f"Error: Source directory {source_dir} does not exist.")
            self._log(f"Error: Source directory {source_dir} does not exist.")
            return

        if not os.path.isdir(source_dir):
            print(f"Error: {source_dir} is not a directory.")
            self._log(f"Error: {source_dir} is not a directory.")
            return

        for dirpath, dirnames, filenames in os.walk(source_dir):
            for file in filenames:
                try:
                    src_file = os.path.join(dirpath, file)
                    dst_file = src_file.replace(source_dir, backup_dir, 1)
                    os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                    shutil.copy2(src_file, dst_file)
                    print(f"Backed up: {src_file} to {dst_file}")
                    self._log(f"Backed up: {src_file} to {dst_file}")
                except PermissionError:
                    print(f"Permission error when copying {src_file}.")
                    self._log(f"Permission error when copying {src_file}.")
                except Exception as e:
                    print(f"Error: {str(e)}")
                    self._log(f"Error: {str(e)}")

    def restore(self, backup_dir, destination_dir):
        if not os.path.exists(backup_dir):
            print(f"Error: Backup directory {backup_dir} does not exist.")
            self._log(f"Error: Backup directory {backup_dir} does not exist.")
            return

        if not os.path.isdir(backup_dir):
            print(f"Error: {backup_dir} is not a directory.")
            self._log(f"Error: {backup_dir} is not a directory.")
            return

        for dirpath, dirnames, filenames in os.walk(backup_dir):
            for file in filenames:
                try:
                    src_file = os.path.join(dirpath, file)
                    dst_file = src_file.replace(backup_dir, destination_dir, 1)
                    os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                    shutil.copy2(src_file, dst_file)
                    print(f"Restored: {src_file} to {dst_file}")
                    self._log(f"Restored: {src_file} to {dst_file}")
                except PermissionError:
                    print(f"Permission error when restoring {src_file}.")
                    self._log(f"Permission error when restoring {src_file}.")
                except Exception as e:
                    print(f"Error: {str(e)}")
                    self._log(f"Error: {str(e)}")


b = BackupManager()

source_directory = os.getcwd()
backup_directory = os.path.join(os.getcwd(), "backup")
restore_directory = os.path.join(os.getcwd(), "restore")

b.backup(source_directory, backup_directory)

b.restore(backup_directory, restore_directory)
