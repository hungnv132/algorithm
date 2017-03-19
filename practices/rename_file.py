"""
    remove prefix number in file's name.
    '00 text.txt' --> 'text.txt'
    '99 text1.txt' --> 'text1.txt'
"""
import os

BASE_DIR = os.path.abspath('C:\\Users\\hungnv132\\Google Drive\\English\\3000')
DIR_TEST = './test_folder'
print(BASE_DIR)


def _get_new_name(old_file_name):
    """
    Get a new file's name from old file's name
    """
    try:
        first_space_index = old_file_name.index(' ')
        return old_file_name[first_space_index:].strip()
    except ValueError as error:
        print('There are no spaces in file\'s name')
        return old_file_name


def _rename(base_dir, old_name, new_name):
    os.rename(os.path.join(base_dir, old_name), os.path.join(base_dir, new_name))


def rename_file(base_dir):
    for filename in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, filename)):
            rename_file(os.path.join(base_dir, filename))       # recursion
        else:
            if ' ' in filename:
                new_name = _get_new_name(filename)
                _rename(base_dir, filename, new_name)
            else:
                print('\'%s\' has no spaces in file\'s name' % filename)

if __name__ == '__main__':
    rename_file(DIR_TEST)