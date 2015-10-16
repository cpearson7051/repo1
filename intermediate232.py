import re
from math import sqrt
import time

class Cartesian:
  
  def __init__(self, file):
    self.f = open(file, 'r')
    self.coords = self.f.readlines()
    self.f.close()
    self.coordlist = []
    self.shortlist = []
    self.shortest = ((0,0), (0,0), 1000)
    self.parse()
    
  
  def parse(self):
    numoflines = float(self.coords[0])
    p = re.compile(self.coords[1])
    m = re.search(r'(\d+.\d+)(\W\s)(\d+.\d+)', str(self.coords[1]))
   
    a = (m.group(1), m.group(3))
   
    
    for line in self.coords[1:]:
      #print line
      m = re.search(r'(\d+.\d+)(\W\s)(\d+.\d+)', line)
      a = (float(m.group(1)), float(m.group(3)))
      self.coordlist.append(a)
      self.shortlist.append(a)
      
    for coord in self.shortlist:
      self.coordlist.pop(0)
      for elem in self.coordlist:
        self.calc(coord, elem)
       
    print self.shortest
    
    
    
  def calc(self, a, b):
  #can calculate faster and just compare squares, without rooting
    dist =  sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
   # print str(dist)
    if dist <= self.shortest[2]:
      self.shortest = (a, b, dist)
      
    
def main():
  time1 = time.time()
  print 'find closest coords'
  c = Cartesian('coords.txt')
  time2 = time.time()
  print time2 - time1
  
if __name__ == '__main__':
  main()