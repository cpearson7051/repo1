import random
import re

def shuffle(input):
  output = []
  shuffle = []
  output = re.sub("[^\w]", " ", input).split()
  
  while len(output) > 0:
    a = random.choice(output)
    shuffle.append(a)
    output.remove(a)
    
  print ' '.join(shuffle)  

def main():
  print "hello"
  shuffle("a e i o u")
  shuffle("apple blackberry cherry dragonfruit grapefruit kumquat mango nectarine persimmon raspberry raspberry")
  
if __name__ == "__main__":
  main()