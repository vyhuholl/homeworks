import urllib.request
import html
import time
import os
import re
import csv

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        time.sleep(2)
        return text
    except:
        return('Error')

regPostAuthor = re.compile('<a href=\"javascript:void\(0\);\">(.*?)</a>', flags= re.DOTALL)
regAuthor1 = re.compile('<a href=\"javascript:void\(0\);\">', flags= re.DOTALL)
regAuthor2 = re.compile('</a>', flags= re.DOTALL)
text = download_page('http://www.marpravda.ru/news/armiya/voennykh-doznavateley-uchili-raskryvat-prestupleniya/')
author = (regPostAuthor.search(text)).group()
print(author)
