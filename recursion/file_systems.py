"""
 + Describe: computing the total disk usage for all files and directories nested within a particular directory.
 + Input: A String designating a path to a file-system entry
 + Output: The cumulative disk space used by that entry and any nested entries
 + References: Data structures and Algorithms in Python by Goodrich, Michael T., Tamassia, Roberto, Goldwasser, Michael
"""

import os


def total_disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        file_list = os.listdir(path)
        for file in file_list:
            child_path = os.path.join(path, file)
            total = total + total_disk_usage(child_path)
    return total


def file_system_tree(path, lines='', recursive = 0):

    if os.path.isdir(path):
        print("|%s %s [Dir] " % (lines * recursive, os.path.basename(path)))
        recursive += 1
        for file in os.listdir(path):
            file_system_tree(os.path.join(path, file),'--', recursive)
    else:
        print("|%s %s [File]" % (lines * recursive, os.path.basename(path)))

if __name__ == '__main__':
    path = 'E:\\test'
    print(file_system_tree(path))
    print(os.path.basename(path))