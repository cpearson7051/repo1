import sys


  
def palindromer(num, step):
  palnumlist = []
  reversepalnumlist = []
  for index, value in enumerate(num):
    palnumlist.append(value)
    reversepalnumlist.insert(0, value)
  forward = ''.join(palnumlist)
  reverse = ''.join(reversepalnumlist)
  print forward + ' ' + reverse
  paladder(forward, reverse, step)
  
def paladder(forward, reverse, step):
  palbool = True
  newnum = int(forward) + int(reverse)
  newnumstring = str(newnum)
  print newnum
  if len(str(newnum)) > 2:
    for index, value in enumerate(newnumstring[0:]):
      if newnumstring[index] != newnumstring[-index-1]:
        palbool = False
        break
    
  else:
    if str(newnumstring[0]) != str(newnumstring[-1]):
      palbool = False
  print palbool
  
  if palbool:
    print forward + " + " + reverse + " = " + newnumstring
    print "became palindromic after " + str(step) + " steps"
  else:
    step += 1
    palindromer(newnumstring, step)
      
def main():
  steps = 1
  palindromer("11", steps)
  steps = 1
  palindromer("68", steps)
  palindromer("123", 1)
  palindromer("286", 1)
  palindromer("196196871", 0)



if __name__ == "__main__":
  main()