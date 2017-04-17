import os

def remove_tree(folder):
    for root, dirs, files in os.walk(folder):
        for f in files:
            os.remove(os.path.join(root, f))
        for d in dirs:
            os.rmdir(os.path.join(root, d))
        os.rmdir(folder)

remove_tree('folder')
