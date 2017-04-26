import os

def create_letters_list():
  file_tree = os.walk('.')
  letters = {}
  for d in file_tree:
    folder_name = d[0].strip('.\/')
    letter = folder_name[0]
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1
   return letters


def main():
  letters = create_letters_list
  letter = ''
  n = 0
  for i in letters:
    if letters[i] > n:
      letter = i
      n = letters[i]
  print(letter)


main()
