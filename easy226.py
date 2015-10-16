import re
class Fractions:
  def __init__(self, num):
    self.numerator = 0
    self.denominator = 0
    self.total = num
    self.fraction = None
    self.a = None
    self.sumnum = 0
    self.sumden = 0
  def split(self, frac):
    self.fraction = frac
    self.a = re.search('([0-9]+)([/])([0-9]+)', frac)
    if self.a.group(0) is not None:
      self.numerator = self.a.group(1)
      self.denominator = self.a.group(3)
      self.addtosum(int(self.numerator), int(self.denominator))
    else:
      return "didnt work"
      
  def addtosum(self, num, den):
    if self.sumnum == 0:
      self.sumnum = num
      self.sumden = den
      print 'adding new sum' + str(self.sumnum) + '/' + str(self.sumden)
    else: 
      self.sumnum = self.sumnum * den + num * self.sumden
      self.sumden = self.sumden * den
      print 'adding to the sum'
    self.reduce()
  def reduce(self):
    reduced = False
    while reduced == False:
      if self.sumnum % 2 == 0 and self.sumden % 2 == 0:
        self.sumnum = self.sumnum / 2
        self.sumden = self.sumden / 2
      elif self.sumnum % 3 == 0 and self.sumden % 3 == 0:
        self.sumnum = self.sumnum / 3
        self.sumden = self.sumden / 3
      elif self.sumnum % 5 == 0 and self.sumden % 5 == 0:
        self.sumnum = self.sumnum / 5
        self.sumden = self.sumden / 5
      elif self.sumnum % 7 == 0 and self.sumden % 7 == 0:
        self.sumnum = self.sumnum / 7
        self.sumden = self.sumden / 7
      else:
        reduced = True
    
    
def main():
#print Fractions(1).split('1/3')
  howmany = raw_input("How many fractions are being added? ")
  howmany = int(howmany)
  f = Fractions(howmany)
  c = howmany
  n = 0
  a = []
  while howmany > 0:
    b = raw_input("Enter fraction: ")
    a.append(b)
    n += 1
    howmany -= 1
  
  print a
  
  while n > 0:
    n -= 1
    #Fractions(c).split(a[n])
    f.split(a[n])
    howmany += 1
  #print str(Fractions(c).sumnum) + '/' + str(Fractions(c).sumden)
  print str(f.sumnum) + '/' + str(f.sumden)

  
if __name__ == "__main__":
  main()