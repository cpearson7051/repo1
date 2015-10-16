#Easy Challenge 223
#Garland words. 
#by Christopher Pearson





def isGarland(word):
  check = False
  for i in xrange(len(word)):
    if word[:i] == word[-i:]:
      check = True
      print 'match at ' + str(i)
      degree = i
  if check:
    print "Degree: " + str(degree)
    print word[:degree] + word[degree:]*100
  else:
    print "Degree 0"
    print word

def main():
  print "hi"

if __name__ == "__main__":
  main()
  isGarland('onion')
  isGarland('programmer')
  isGarland('ceramic')
  isGarland('alfalfa')