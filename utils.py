import fnmatch
import os
import re


def filter_for_annotations(root, files, image_filename):
    file_types = ['*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    basename_no_extension = os.path.splitext(os.path.basename(image_filename))[0]
    file_name_prefix = basename_no_extension + '.*'
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    files = [f for f in files if re.match(file_name_prefix, os.path.splitext(os.path.basename(f))[0])]

    return files

def filter_for_xml(files):
    file_types = ['*.xml']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    files = [f for f in files if re.match(file_types, f)]

    return files

def filter_for_jpeg(files):
    file_types = ['*.jpg']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    files = [f for f in files if re.match(file_types, f)]

    return files

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)

    num_sep = some_dir.count(os.path.sep)

    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]
