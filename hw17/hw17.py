import os

file_tree = os.walk('.')
l = []
for f in file_tree:
  l.append(f)
