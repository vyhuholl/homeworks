import matplotlib.pyplot as plt
import sqlite3

conn1 = sqlite3.connect('hittite.db')
conn2 = sqlite3.connect('newdb.db')
c1 = conn1.cursor()
c2 = conn2.cursor()
wordforms = []
glosses = []
c1.execute('SELECT Lemma FROM wordforms')
lemmas = c1.fetchall()
c1.execute('SELECT Wordform FROM wordforms')
wordforms = c1.fetchall()
c1.execute('SELECT Glosses FROM wordforms')
glosses = c1.fetchall()
glosses_splitted = []
for i in glosses:
    glosses_splitted.append(i.split('.'))
for i in glosses_splitted:
    for j in i:
        if j not in glosses_numbered and j.isupper = True:
            glosses_numbered.append(j)
c2.execute('CREATE TABLE words(id integer, Lemma text, Wordform text, Glosses text)')
c2.execute('CREATE TABLE glosses(id integer, Gloss text, Meaning text)')
c2.execute('CREATE TABLE glossed_words(word_id integer, glosse_id integer)')
for i in len(lemmas):
    lemma = lemmas[i]
    wordform = wordforms[i]
    gloss = glosses[i]
    c2.execute('INSERT INTO words VALUES(i, lemma, wordform, gloss)')
for i in len(glosses_list):
    gloss = glosses_list(i)
    c2.execute('INSERT INTO glosses VALUES(i, gloss)')
for i in len(wordforms):
    gloss = glosses_splitted[i]
    for g in gloss:
        j = glosses_numbered.index(g)
        c2.execute('INSERT INTO glosses_words(i, j)')
conn1.close()
conn2.close()
glosses_list = []
for i in glosses_splitted:
    glosses_list += i
numbers_list = []
for i in glosses_numbered:
    numbers_list.append(glosses_list.count(i))
    plt.plot(glosses_numbered, numbers_list)
    plt.show()
