#challenge 228[easy]
#program should intake a word and emit if all letters are in order
#ex. almost IN ORDER

def listize(word):
  #put each letter into a list
  wordlist = []
  for i in word:
    wordlist.append(i)
  alphabetical = sortlist(wordlist)
  if alphabetical:
    return word + ' IN ORDER'
  else:
    return word + ' NOT IN ORDER'
  
def sortlist(wordlist):
  alphabetical = True
  tempsort = []
  for i in wordlist:
    tempsort.append(i)
  print tempsort
  sortedlist = ''.join(sorted(tempsort))
  
  for i, char in enumerate(wordlist):
    if char != sortedlist[i]:
      alphabetical = False
  return alphabetical
      
def main():
  print listize('almost')
  print listize('billowy')
  print listize('biopsy')
  print listize('chinos')
  print listize('defaced')
  print listize('chintz')
  print listize('sponged')
  print listize('bijoux')
  print listize('abhors')
  print listize('fiddle')
  print listize('begins')
  print listize('chimps')
  print listize('wronged')



if __name__ == "__main__":
  main()
      
