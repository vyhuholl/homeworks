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

commonUrl = 'http://www.marpravda.ru/news/?day='
regPostTitle = re.compile('<div class=\"news_name\"><a href=\".*\">.*</a></div>', flags= re.DOTALL)
regTitle1 = re.compile('<div class=\"news_name\"><a href=\".*\">', flags= re.DOTALL)
regTitle2 = re.compile('</a></div>', flags= re.DOTALL)
regPostLink = re.compile('<a class=\"left\" href=\".*\">Читать далее</a>', flags= re.DOTALL)
regLink1 = re.compile('<a class="left" href="', flags= re.DOTALL)
regLink2 = re.compile('\">Читать далее</a>', flags= re.DOTALL)
regPostTopic = re.compile('<span class=\"rubric\"><a href=\".*\">.*</a>', flags= re.DOTALL)
regTopic1 = re.compile('<span class=\"rubric\"><a href=\".*\">', flags= re.DOTALL)
regTopic2 = re.compile('</a>', flags= re.DOTALL)
regPostAuthor = re.compile('Автор статьи: <br /> <a href=\"javascript:void(0);\">.*</a>', flags= re.DOTALL)
regAuthor1 = re.compile('Автор статьи: <br /> <a href=\"javascript:void(0);\">', flags= re.DOTALL)
regAuthor2 = re.compile('</a>', flags= re.DOTALL)
regTag = re.compile('<.*?>', re.DOTALL)
regScript = re.compile('<script>.*?</script>', re.DOTALL)
regComment = re.compile('<!--.*?-->', re.DOTALL)

for year in range(2016, 2018):
    for month in range(1, 13):
        for day in range(1, 32):
            date = str(day) + '.' + str(month) + '.' + str(year)
            pageUrl = commonUrl + date
            page = download_page(pageUrl)
            if page != 'Error':
                path = 'C:/homework' + os.sep + str(year) + os.sep + str(month) + os.sep + str(day) + os.sep
                os.makedirs(path + 'not mystem/')
                os.makedirs(path + 'mystem XML')
                os.makedirs(path + 'mystem plain text')
                csv_table = open(path + 'csv_table.csv', 'w')
                writer = csv.writer(csv_table, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['path', 'author', 'sex', 'birthday', 'header', 'created', 'sphere', 'genre_fi', 'type', 'topic', 'chronotop', 'style', 'audience_age', 'audience_level', 'audience_size', 'source', 'publication', 'publisher',	'publ_year', 'medium', 'country', 'region', 'language'])
                titles = regPostTitle.findall(page)
                new_titles = []
                for t in titles:
                    clean_t = regTitle1.sub("", t)
                    clean_t = regTitle2.sub("", clean_t)
                    new_titles.append(clean_t)
                links = regPostLink.findall(page)
                new_links = []
                for l in links:
                    clean_l = regLink1.sub("", l)
                    clean_l = regLink2.sub("", clean_l)
                    new_links.append(clean_l)
                topics = regPostTopic.findall(page)
                new_topics = []
                for t in topics:
                    clean_t = regTopic1.sub("", t)
                    clean_t = regTopic2.sub("", clean_t)
                    new_topics.append(clean_t)
                for i in range(len(titles)):
                    header = new_titles[i]
                    link = new_links[i]
                    topic = new_topics[i]
                    text = download_page(link)
                    author = (regPostAuthor.search(text)).group()
                    clean_author = regAuthor1.sub('', author)
                    clean_author = regAuthor2.sub('', clean_author)
                    text = regTag.sub('', text)
                    text = regScript.sub('', text)
                    text = regComment.sub('', text)
                    file_path = path + 'not mystem/' + header + '.txt'
                    file = open(file_path, 'w')
                    file.write('@au' + author + '\n')
                    file.write('@ti' + header + '\n')
                    file.write('@da' + date + '\n')
                    file.write('@topic' + topic + '\n')
                    file.write('@url' + link + '\n')
                    file.write(text)
                    writer.writerow([file_path, clean_author, '', '', header, date, 'публицистика', '', '', topic, '', 'нейтральный', 'н-возраст', 'н-уровень', 'республиканская', link, 'Марийская правда', '', year, 'газета', 'Россия', 'республика Марий-Эл', 'ru'])
                inp = path + 'not mystem/'
                lst = os.listdir(inp)
                for fl in lst:
                    os.system(r"C:\mystem.exe " + inp + os.sep + fl + " mystem XML" + os.sep + fl + '-- xml')
                    os.system(r"C:\mystem.exe " + inp + os.sep + fl + " mystem plain text" + os.sep + fl)
                    clean_t = regTitle1.sub("", t)
                    clean_t = regTitle2.sub("", clean_t)
                    new_titles.append(clean_t)
                links = regPostLink.findall(page)
                new_links = []
                for l in links:
                    clean_l = regLink1.sub("", l)
                    clean_l = regLink2.sub("", clean_l)
                    new_links.append(clean_l)
                topics = regPostTopic.findall(page)
                new_topics = []
                for t in topics:
                    clean_t = regTopic1.sub("", t)
                    clean_t = regTopic2.sub("", clean_t)
                    new_topics.append(clean_t)
                for i in range(len(titles)):
                    header = new_titles[i]
                    link = new_links[i]
                    topic = new_topics[i]
                    text = download_page(link)
                    author = regPostAuthor(text)
                    clean_author = regAuthor1.sub('', author)
                    clean_author = regAuthor2.sub('', clean_author)
                    text = regTag.sub('', text)
                    text = regScript.sub('', text)
                    text = regComment.sub('', text)
                    file_path = path + 'not mystem/' + header + '.txt'
                    file = open(file_path, 'w')
                    file.write('@au' + author + '\n')
                    file.write('@ti' + header + '\n')
                    file.write('@da' + date + '\n')
                    file.write('@topic' + topic + '\n')
                    file.write('@url' + link + '\n')
                    file.write(text)
                    writer.writerow([file_path, clean_author, '', '', header, date, 'публицистика', '', '', topic, '', 'нейтральный', 'н-возраст', 'н-уровень', 'республиканская', link, 'Марийская правда', '', year, 'газета', 'Россия', 'республика Марий-Эл', 'ru'])
                inp = path + 'not mystem/'
                lst = os.listdir(inp)
                for fl in lst:
                    os.system(r"C:\mystem.exe " + inp + os.sep + fl + " mystem XML" + os.sep + fl + '-- xml')
                    os.system(r"C:\mystem.exe " + inp + os.sep + fl + " mystem plain text" + os.sep + fl)
                    file.write('@da' + date + '\n')
                    file.write('@topic' + topic + '\n')
                    file.write('@url' + link + '\n')
                    file.write(text)
                    writer.writerow([file_path, author, '', '', header, date, 'публицистика', '', '', topic, '', 'нейтральный', 'н-возраст', 'н-уровень', 'республиканская', link, 'Марийская правда', '', year, 'газета', 'Россия', 'республика Марий-Эл', 'ru'])
                inp = path + 'not mystem/'
                lst = os.listdir(inp)
                for fl in lst:
                    os.system(r"C:\mystem.exe " + inp + os.sep + fl + " mystem XML" + os.sep + fl + '-- xml')
                    os.system(r"C:\mystem.exe " + inp + os.sep + fl + " mystem plain text" + os.sep + fl)
                new_topics = []
                for t in topics:
                    clean_t = regTag.sub("", t)
                    new_topics.append(clean_t)
                for i in range(len(titles)):
                    header = new_titles[i]
                    link = new_links[i]
                    topic = new_topics[i]
                    text = download_page(link)
                    author = regPostAuthor(text)
                    clean_author = regTag.sub('', author)
                    text = regTag.sub('', text)
                    text = regScript.sub('', text)
                    text = regComment.sub('', text)
                    file_path = path + 'not mystem/' + header + '.txt'
                    file = open(file_path, 'w')
                    file.write('@au' + author + '\n')
                    file.write('@ti' + header + '\n')
                    file.write('@da' + date + '\n')
                    file.write('@topic' + topic + '\n')
                    file.write('@url' + link + '\n')
                    file.write(text)
                    writer.writerow(file_path, author, '', '', header, date, 'публицистика', '', '', topic, '', 'нейтральный', 'н-возраст', 'н-уровень', 'республиканская', link, 'Марийская правда', '', year, 'газета', 'Россия', 'республика Марий-Эл', 'ru')
                inp = path + 'not mystem/'
                lst = os.listdir(inp)
                for fl in lst:
                    os.system(r"C:\mystem.exe " + inp + os.sep + fl + " mystem XML" + os.sep + fl + '-- xml')
                    os.system(r"C:\mystem.exe " + inp + os.sep + fl + " mystem plain text" + os.sep + fl)
