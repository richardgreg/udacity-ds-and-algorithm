import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    paths_list = []

    def traverse(path):
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path, item)):
                if item.endswith(suffix):
                    paths_list.append(os.path.join(path, item))
            elif os.path.isdir(os.path.join(path, item)):
                traverse(os.path.join(path, item))

    if os.path.isdir(path):
        traverse(path)

    return paths_list

print(find_files('.c', './testdir1')) # should return a files in folder ending with .c
# ['./testdir1/subdir3/subsubdir1/b.c', './testdir1/t1.c', './testdir1/subdir5/a.c', './testdir1/subdir1/a.c']

print(find_files('.h', './testdir1')) # should return a files in folder ending with .h
# ['./testdir1/subdir3/subsubdir1/b.h', './testdir1/subdir5/a.h', './testdir1/t1.h', './testdir1/subdir1/a.h']

print(find_files('.h', './testdir2')) # An empty folder should return an empty list
# []

print(find_files('.h', './testdir3')) # A nested folder with no entry should return an empty list
# []

print(find_files('.h', './testdir3/abc')) # A non-existent path should return an empty list
# []
