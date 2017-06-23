import os

filetree = os.walk('news')
for root, dirs, files in filetree:
    for f in files:
        print(f)
