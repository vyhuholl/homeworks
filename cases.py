word = input()
if not (word.endswith('а') or word.endswith('я') or word.endswith('у') or word.endswith('ю') or word.endswith('ы') or word.endswith('и') or word.endswith('э')):
    print('Nominative singular')
    print('Accusative singular')
if word.endswith('а') or word.endswith('я'):
    print('Genitive singular')
    print('Accusative singular')
    print('Nominative plural')
if word.endswith('у') or word.endswith('ю'):
    print('Dative singular')
if word.endswith('ом') or word.endswith('ем'):
    print('Instrumentalis singular')
if word.endswith('е'):
    print('Prepositive singular')
if word.endswith('ы'):
    print('Nominative plural')
    print('Accusative plural')
if word.endswith('ов') or word.endswith('ев'):
    print('Genitive plural')
    print('Accusative plural')
if word.endswith('ам') or word.endswith('ям'):
    print('Dative plural')
if word.endswith('ами') or word.endswith('ями'):
    print('Instrumentalis plural')
if word.endswith('ах') or word.endswith('ях'):
    print('Prepositive plural')
