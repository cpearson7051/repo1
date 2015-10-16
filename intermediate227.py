import re

class contiguousChains():
  def __init__(self, sample):
    self.sampleobj = open(sample, 'r')
    
    
  def chainParser(self):
    contig = 0
    num = 0
    for line in self.sampleobj.readlines():
      for char in line:
        if char != ' ':
          contig += 1
        #elif char == ' ':
        else:
          if contig >= 2:
            num += 1
          contig = 0
    return num


def main():
  a = contiguousChains('sample.txt')
  print a.chainParser()
 
#boilerplate 
if __name__ == '__main__':
  main()