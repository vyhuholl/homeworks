import re
import os
import csv

def open_file(xml):
    with open(xml, 'r', encoding = 'cp1251') as f:
        text = f.readlines()
    return text

def open_file_as_string(xml):
    with open(xml, 'r', encoding = 'cp1251') as f:
        text = f.read()
    return text

def count_words(text):
    text_as_string = open_file_as_string(text)
    return str(text_as_string.count('<w>'))

def find_author(text):
    text_as_string = open_file_as_string(text)
    author = re.search('<meta content=".*" name="author"/>')
    author = auth.lstrip('<meta content="')
    author = auth.rstrip('" name="author"/>')
    return author

def find_created(text):
    text_as_string = open_file_as_string(text)
    created = re.search('<meta content=".*" name="created"/>')
    created = auth.lstrip('<meta content="')
    created = auth.rstrip('" name="created"/>')
    return created

def main():
    filetree = os.walk('news')
    task1 = open('task1.txt', 'w', encoding = 'cp1251')
    for root, dirs, files in filetree:
        for f in files:
            task1.write(f + '\t' + count_words(f) + '\n')
    task1.close()
    task2 = open('task2.csv', 'w', encoding = 'cp1251')
    writer = csv.writer(task2.csv, delimiter = '|', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for root, dirs, files in filetree:
        for f in files:
            f.writerow([f] + [find_author(f)] + [find_created(f)])

if __name__ == '__main__':
    main()
