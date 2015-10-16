import random

class streamCipher():
  def __init__(self, const):
    #self.msg = msg
   
    self.a = const

  def lcg(self, key):
    X = key
    #use linear congruential formula X_(n+1) = (aX_n) mod m
    #a = self.const #random.randint(0, 9999999999)
    m = 2 ** 32
    while True:
      X = (X*self.a + 12345) % m
      yield int(X/(2**24))
  
  def encode(self, msg, key):
    rand = self.lcg(key)
    return "".join(chr(ord(c) ^ next(rand)) for c in msg)
    

  def decode(self, msg, key):
    return self.encode(msg, key)
    
def main():

  print '---------------------------'
  print '------TEST-----------------'
  a = streamCipher(100000)
  tstmsg = 'test message'
  b = a.encode(tstmsg, 20000)
  print b
  c = a.decode(b, 20000)
  print c
  print '----------------------------'
  run = True
  const = 110351524577878656
  g = streamCipher(const)
  while run:
    choice = int(raw_input("Encrypt 1, Decrypt 2, Quit 3: "))
  
  
    #msg = 'Attack at Dawn'
     #random.randint(0, 9999999999)
    
    print '-------------------------------'
    if choice == 1:
      key = int(raw_input("Enter the key (default is 31337): "))
      msg = str(raw_input("Enter your message to encode: "))
    
      h = g.encode(msg, key)
  
      print "Encoded Message: " + h 
  
    #print '--------------------------------------'
    elif choice == 2:
      key = int(raw_input("Enter the key (default is 31337): "))
      msg = str(raw_input("enter the cipher to decrypt: "))
      i = g.decode(msg, key)
      print 'the message is: ' + i
    
    elif choice == 3:
      run = False
      break
 

if __name__ == '__main__':
  main()
  
#need key number to encode /decode
#encode

#decode

