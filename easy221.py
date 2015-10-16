



def printsnake(wordlist):
  #choose direction 0 = right 1 = down
  direction = 0
  #length of first whitespace is length of first word - 1
  whitespace = len(wordlist[0]) 
  #print first word
  print wordlist[0]
  #set toggle to down
  direction = 1
  #remember last word
  lastword = "last"
  #loop the rest of words down and right starting with index 1
  for word in wordlist[1:]:
    if direction == 1:   #if direction down
      for letter in word[1:-1]: #first letter in use
        print " "*(whitespace-1) + str(letter)
      direction = 0
      lastword = str(word)
    elif direction == 0:
      print " "*(whitespace-1) + word[:]
      whitespace += (len(word) - 1)
      direction = 1
      lastword = str(word)
   #tack on last letter if the last word is verticle
  if direction == 0:
    print  " "*(whitespace-1) + lastword[-1]
  






def main():
  List1 = ['CAN', 'NINCOMPOOP', 'PANTS', 'SCRIMSHAW', 'WASTELAND', 'DIRK', 'KOMBAT', "TEMP", 'PLUNGE', 'ESTER', 'REGRET', 'TOMBOY']
  List2 = ['NICKEL', 'LEDERHOSEN', 'NARCOTRAFFICANTE', 'EAT', 'TO', 'OATS', 'SOUP', 'PAST', 'TELEMARKETER', 'RUST', 'THINGAMAJIG', 'GROSS', 'SALTPETER', 'REISSUE', 'ELEPHANTITIS']
  printsnake(List1)
  printsnake(List2)


if __name__ == "__main__":
  main()
