
import os
import shutil
from pathlib import Path

BASE_DIR = os.path.abspath('C:\\Users\\hungnv132\\Google Drive\\English\\3000')
DIR_TEST = './test_folder'

COPY_SRC_DIR = 'C:\\Users\\Hp\\Google Drive\\English\\Newwords'
COPY_DIST_DIR = 'C:\\Users\\Hp\\Google Drive\\English\\Life'

copy_src = Path(COPY_SRC_DIR)
copy_dist = Path(COPY_DIST_DIR)


def _get_new_name(old_file_name):
    """
    Get a new file's name from old file's name
    eg:
        old_file_name = '88 machine leaning.mp3'
        -> part_number = 88
        -> the_other = machine leaning.mp3
    """
    try:
        first_space_index = old_file_name.index(' ')
        part_number = old_file_name[:first_space_index].strip()
        the_other = old_file_name[first_space_index:].strip()
        try:
            int(part_number)
            return the_other
        except ValueError as error:
            print('INFO: The part_number is not a number')
            return old_file_name

    except ValueError as error:
        print('INFO: There are no spaces in file\'s name')
        return old_file_name


def _rename(base_dir, old_name, new_name):
    if not os.path.exists(os.path.join(base_dir, new_name)):
        os.rename(os.path.join(base_dir, old_name), os.path.join(base_dir, new_name))
    else:
        print("REMOVE: '%s' is removed" % old_name )
        os.remove(os.path.join(base_dir, old_name))


def rename_file(base_dir):
    """
    Remove prefix number in file's name.
    '00 text.txt' --> 'text.txt'
    '99 text1.txt' --> 'text1.txt'
    """
    if os.path.exists(base_dir):
        for filename in os.listdir(base_dir):
            if os.path.isdir(os.path.join(base_dir, filename)):
                rename_file(os.path.join(base_dir, filename))       # recursion
            else:
                if ' ' in filename:
                    new_name = _get_new_name(filename)
                    if new_name.strip() != filename.strip():
                        _rename(base_dir, filename, new_name)
                else:
                    print('\'%s\' has no spaces in file\'s name' % filename)
    else:
        print('INFO: The path doesn\'t exist.')


def _copy(src, dist):
    """
    Copy file all files in the src to the dist
    """
    for filename in os.listdir(src):
        print('- %s' % src)
        # file = os.path.join(src, filename)
        if os.path.isdir(os.path.join(src, filename)):
            print('--- %s' % os.path.join(src, filename))
            _copy(os.path.join(src, filename), dist)        # recursion
        else:
            shutil.copy(os.path.join(src, filename), dist)


def copy_all_file(src, dist):
    """
     Check whether src and dist exists
    """
    print('Running...')
    if not os.path.exists(src):
        return print("INFO: The path of 'src' doesn't exist.")
    if not os.path.exists(dist):
        return print("INFO: The path of 'dist' doesn't exist.")
    _copy(src, dist)

    print('Finished!')



if __name__ == '__main__':
    print(_get_new_name('fsfs machine learning.mp3'))
    # copy_all_file(COPY_SRC_DIR, COPY_DIST_DIR)
    # rename_file(COPY_DIST_DIR)



