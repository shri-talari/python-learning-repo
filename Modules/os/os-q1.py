'''Q1.File Organizer

Problem:
Write a program that organizes files in a given directory into subfolders based on file extensions.

Example: all .txt files go into TextFiles, all .jpg files into Images.

Handle errors:

Non-existing directory (FileNotFoundError).

Permission errors.

Ensure it doesn’t move system/hidden files accidentally.
'''

import os
import shutil

categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Others': []
}

source_dir = os.getcwd()

for category in categories:
    folder_path = os.path.join(source_dir, category)
    os.makedirs(folder_path, exist_ok=True)

for item in os.listdir(source_dir):
    item_path = os.path.join(source_dir, item)

    if os.path.isdir(item_path):
        continue

    _, ext = os.path.splitext(item)
    ext = ext.lower()

    moved = False

    for category, extensions in categories.items():
        if ext in extensions:
            dest_path = os.path.join(source_dir, category, item)
            shutil.move(item_path, dest_path)
            moved = True
            break

    if not moved:
        dest_path = os.path.join(source_dir, 'Others', item)
        shutil.move(item_path, dest_path)

print("Files organized successfully.")
