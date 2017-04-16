import os

def symbols(s):
  ans = True
  for i in s:
    if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
      ans = False
  return ans

def main():
  n = 0
  for f in os.listdir('.'):
    if symbols(f) = True:
      n += 1
      print (f)
    print (n)

main()
