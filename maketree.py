import os

def make_tree(folder):
    n = 0
    for root, dirs, files in os.walk(folder):
        n += 1
        for d in dirs:
            print(n * '\t' + '--' + d)
            make_tree(d)
    for root, dirs, files in os.walk(folder):
        for f in files:
            print((n + 1) * '\t' + '--' + f)

make_tree('folder')
