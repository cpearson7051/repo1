#easy 232, decide if palindromic

def pal():
  f = open('palindrome.txt', 'r')
  pal = f.readlines()
  f.close()
  p = ''
  i = 0
  spaces = []
  for line in pal[1:]:
    for char in line:
      if char.isalpha():
        p += char
        i += 1
      else:
        spaces.append((char, i))
        i += 1
  print spaces
  p = p.lower()
  bool = True
  for index, element in enumerate(p):
    if p[index] == p[-index - 1]:
      bool = True
    else:
      bool = False
      break
  if bool == True:
    print "Palindrome"
  else:
    print "Not a Palindrome"
    
def main():
  pal()
  
if __name__ == '__main__':
  main()
      