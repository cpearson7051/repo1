#stacking paper 
# color of n, placed at x,x of width x, height x

import numpy

class buildsheet:
  def __init__(self, h, w):
    self.width = w
    self.height = h
    self.color = 0
    self.sheet = numpy.ndarray(shape = (self.width, self.height), dtype=int)
    self.blanksheet()
    self.totalcolors = 1
    
  def blanksheet(self):
    for i in xrange(self.width):
      for j in xrange(self.height):
        self.sheet[i][j] = self.color
        
   
  
  def addsheet(self, color, topx, topy, h, w):
    self.totalcolors += 1
    for i in xrange(w):
      for j in xrange(h):
        self.sheet[topx+i][topy + j] = color
        
  def printsheet(self):
    print self.sheet
        
  def computeArea(self):
    tot = 0
    list = []
    for i in xrange(self.totalcolors):
      for j in xrange(self.width):
        for k in xrange(self.height):
          if self.sheet[j][k] == i:
            tot += 1
      list.append(tot)
      print str(i) + ' ' + str(tot)
      tot = 0
    
def main():
  a = buildsheet(20, 10)
  a.addsheet(1, 5, 5, 10, 3)
  a.addsheet(2, 0, 0, 7, 7)
  a.addsheet(3, 1, 10, 7, 6)
  a.printsheet()
  a.computeArea()
 
if __name__ == '__main__':
  main()