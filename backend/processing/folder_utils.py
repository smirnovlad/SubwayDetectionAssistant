import os
import shutil
from pathlib import Path
import re


def clear_folders(folders):
    for folder in folders:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


def copy_folder(src_folder: Path, dest_folder: Path):
    for filename in os.listdir(src_folder):
        src_file_path = os.path.join(src_folder, filename)
        dest_file_path = os.path.join(dest_folder, filename)
        shutil.copy(src_file_path, dest_file_path)


def numerical_sort(value):
    numbers = re.compile(r"(\d+)")
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
