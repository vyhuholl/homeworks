import urllib.request
import html
import os
import re
import csv
from pymystem3 import Mystem

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        return text
    except:
        return('Error')

commonUrl = 'http://www.marpravda.ru/'
regPostTitle = re.compile('<div class=\"news_name\"><a href=\"(.*?)\">(.*?)</a></div>', flags= re.DOTALL)
regPostTopic = re.compile('<span class=\"rubric\"><a href=\"(.*?)\">(.*?)</a>', flags= re.DOTALL)
regPostAuthor = re.compile('<a href=\"javascript:void\(0\);\">(.*?)</a>', flags= re.DOTALL)
regAuthor1 = re.compile('<a href=\"javascript:void\(0\);\">', flags= re.DOTALL)
regAuthor2 = re.compile('</a>', flags= re.DOTALL)
regArticle = re.compile('<article>(.*?)</article>', flags= re.DOTALL)
regTag = re.compile('<.*?>', flags= re.DOTALL)
m = Mystem()

for year in range(2016, 2018):
    for month in range(1, 13):
        for day in range(1, 32):
            date = str(day) + '.' + str(month) + '.' + str(year)
            pageUrl = commonUrl + 'news/?day=' + date
            page = download_page(pageUrl)
            path = 'C:\homework' + os.sep + str(year) + os.sep + str(month) + os.sep + str(day) + os.sep
            if page != 'Error' and os.path.exists(path + 'not_mystem') == False:
                os.makedirs(path + 'not_mystem')
                os.makedirs(path + 'mystem_plain_text')
                os.makedirs(path + 'mystem_XML')
                csv_table = open(path + 'csv_table.csv', 'w')
                writer = csv.DictWriter(csv_table, fieldnames = ['path', 'author', 'sex', 'birthday', 'header', 'created', 'sphere', 'genre_fi', 'type', 'topic', 'chronotop', 'style', 'audience_age', 'audience_level', 'audience_size', 'source', 'publication', 'publisher', 'publ_year', 'medium', 'country', 'region', 'language'], delimiter = '\t')
                writer.writeheader()
                t = regPostTitle.findall(page)
                links = []
                titles = []
                for i in t:
                    links.append(i[0])
                    title = re.sub('[\\\\/:*?"<>|-]', '', i[1])
                    title = title.replace('\ufeff', '')
                    title = title.replace('\u2212', '')
                    title = title.replace('\u0301', '')
                    title = title.replace('\u200b', '')
                    title = title.replace('\u04f0', '')
                    title = title.replace('\u04f1', '')
                    title = title.replace('\xff', '')
                    titles.append(title)
                t1 = regPostTopic.findall(page)
                topics = []
                for i in t1:
                    topics.append(i[1])
                for i in range(len(titles)):
                    header = titles[i]
                    header = header.replace('\t', '')
                    header = header.replace('\u04e7', '')
                    if len(header) > 200:
                        header = header[:200]
                    link = links[i]
                    topic = topics[i]
                    text = download_page(commonUrl + link)
                    try:
                        author = (regPostAuthor.search(text)).group()
                        author = regAuthor1.sub('', author)
                        author = regAuthor2.sub('', author)
                    except:
                        author = 'no author'
                    try:
                        text = (regArticle.search(text)).group()
                        text = regTag.sub('', text)
                        text = text.replace('\u2212', '')
                        text = text.replace(';', '')
                        text = text.replace('&nbsp', '')
                        text1 = m.lemmatize(text)
                        file_path = path + 'not_mystem' + os.sep + str(i) + '.txt'
                        file_path_plain_text = path + 'mystem_plain_text' + os.sep + str(i) + '.txt'
                        file_path_xml = path + 'mystem_XML' + os.sep + str(i) + '.xml'
                        file = open(file_path, 'w')
                        file.write('@au ' + author + '\n')
                        file.write('@ti ' + header + '\n')
                        file.write('@da ' + date + '\n')
                        file.write('@topic ' + topic + '\n')
                        file.write('@url ' + commonUrl + link + '\n')
                        try:
                            file.write(text)
                            writer.writerow({'path': file_path, 'author': author, 'sex': '', 'birthday': '', 'header': header, 'created': date, 'sphere': 'публицистика', 'genre_fi': '', 'type': '', 'topic': topic, 'chronotop': '', 'style': 'нейтральный', 'audience_age': 'н-возраст', 'audience_level': 'н-уровень', 'audience_size': 'республиканская', 'source': link, 'publication': 'Марийская правда', 'publisher': '', 'publ_year': year, 'medium': 'газета', 'country': 'Россия', 'region': 'республика Марий-Эл', 'language': 'ru'})
                        except:
                            print('Error')
                        file_plain_text = open(file_path_plain_text, 'w')
                        file_plain_text.write(' '.join(text1))
                        file_plain_text.close()
                        file_xml = open(file_path_xml, 'w')
                        file_xml.write(' '.join(text1))
                        file_xml.close()
