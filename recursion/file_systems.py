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
if __name__ == '__main__':
    path = 'E:/test1'
    print(total_disk_usage(path))