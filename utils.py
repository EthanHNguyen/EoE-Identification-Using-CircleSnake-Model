"""
utils files for class_to_coco.py
​
author: Yilin Liu
"""
import re
import fnmatch
import os

def filter_for_jpeg(root, files):
    file_types = ["*.jpeg", "*.jpg"]
    file_types = r"|".join([fnmatch.translate(x) for x in file_types])
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    return files

def filter_for_annotations(root, files, image_filename):
    annotations = []
    for file in files:
        if file.startswith(image_filename.split('.')[0]) and file.endswith('png'):
            annotations.append(file)
    return annotations

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]