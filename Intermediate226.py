import numpy
import random
class GameBoard:
  def __init__(self):
    self.pieceCounter = 0
    self.Win = False
    self.Winner = None
    self.winx = None
    self.winy = None
    # initialize gameboard
    self.gameboard = numpy.ndarray(shape = (6, 6))
    for i in xrange(6):
      for j in xrange(6):
        self.gameboard[i][j] = 0
    
    
        
  def addPiece(self, player, column):
    found = False
    count = 5
    self.pieceCounter += 1
    if player == 'X':
      player = 1
    else:
      player = 2
      
    for i in xrange(6):
      if self.gameboard[count][column] == 0 and not found:
        self.gameboard[count][column] = player
        found = True
        self.checkWin(player, count, column)
      else:
        count -= 1
    
  def checkSlot(self, slot):
    if self.gameboard[0][slot] == 0:
      return True
    else:
      return False
  
  def checkWin(self,player, atRow, atCol):
    #look from 3 to left to 3 to right
    
    count = 0
   
    for i in xrange(6):
      if self.gameboard[atRow][i] == player and not self.Win:
        count += 1
        if count == 4:
          self.Win = True
          self.Winner = player
          self.winx = str(atRow)
          self.winy = str(atCol)
          i = 6
          break
      else:
        count = 0

    
    #look 3 up to 3 down
    count = 0
   
    for i in xrange(6):
      if self.gameboard[i][atCol] == player and not self.Win:
        count += 1
        if count == 4:
          self.Win = True
          self.Winner = player
          self.winx = str(atRow)
          self.winy = str(atCol)
          i = 6
          break
      else:
        count = 0
  
    
    #look 3diag down to right and 3diag up left
    count = 0
    
    for i in range(-6, 6, 1):
      if (atRow - i) < 0 or (atRow - i) > 5 or (atCol - i) > 5 or (atCol - i) < 0:
        break
      elif self.gameboard[atRow - i][atCol-i] is not None and self.gameboard[atRow - i][atCol - i] == player and not self.Win:
        count += 1
        if count == 4:
          self.Win = True
          self.Winner = player
          self.winx = str(atRow)
          self.winy = str(atCol)
          i = 6
          j = 6
          break
      else:
          count = 0
    
    #look 3diag up to right and 3diag down left
    count = 0
    
    for i in range(-6, 6, 1):
      
      if (atRow + i) < 0 or (atRow + i) > 5 or (atCol - i) > 5 or (atCol - i) < 0:
        continue
        
      elif self.gameboard[atRow + i][atCol-i] is not None and self.gameboard[atRow + i][atCol - i] == player and not self.Win:
        
        count += 1
        if count == 4:
          self.Win = True
          self.Winner = player
          self.winx = str(atRow)
          self.winy = str(atCol)
          i = 6
          j = 6
          break
      else:
          count = 0   
   

def main():
  playblind = True  
  a = GameBoard()
  x = 'X'
  o = 'O'
  turn = x
  good = False
  winner = None
  while not good:
    humans = raw_input("How many human players? (0-2): ")
    if humans.isdigit():
      humans = int(humans)
      if humans >= 0 and humans < 3:
        good = True
        break
      else:
        continue
  good = False
  while not good:
    blind = raw_input("Would you like to play blind? (y/n): ")
    if blind == 'y':
      print "you will play blind"
      playblind = True
      good = True
    elif blind == 'n':
      print "you will see the board each play"
      playblind = False
      good = True    
    else:
      print "press y or n"
  if humans == 2:
    while not a.Win and a.pieceCounter < 36:
      
      slot = raw_input("Player " +turn+ "'s move: ")
      if slot.isdigit():
        slot = int(slot)
        
        if slot >= 0 and slot < 6:
          if a.checkSlot(slot) == True:
            a.addPiece(turn, slot)
            if not playblind:
              print a.gameboard
            if turn == x:
              turn = o
            else:
              turn = x
          else:
            print "slot " + str(slot) + " full choose another"  
        else:
          print "out of bounds choose again (0-5): "
      else:
        print "out of bounds choose again : "
  
  #if 1 AI
  if humans == 1:
    print "Human player will play first as 'X' "
    while not a.Win and a.pieceCounter < 36:
      
      if turn == x:
        slot = raw_input("Player " +turn+ "'s move: ")
        if slot.isdigit():
          slot = int(slot)
        
          if slot >= 0 and slot < 6:
            if a.checkSlot(slot) == True:
              a.addPiece(turn, slot)
              if not playblind:
                print a.gameboard
              turn = o
                
             
            else:
              print "slot " + str(slot) + " full choose another"  
          else:
            print "out of bounds choose again (0-5): "
        else:
          print "out of bounds choose again : "  
      else:
        slot = random.randrange(0,6)
        if a.checkSlot(slot) == True:
          a.addPiece(turn, slot)
          print "Player 'O' plays " + str(slot)
          if not playblind:
            print a.gameboard
          turn = x
          
  #if 2 AI
  if humans == 0:
    while not a.Win and a.pieceCounter < 36:
      slot = random.randrange(0,6)
      if a.checkSlot(slot) == True:
        a.addPiece(turn, slot)
        if not playblind:
          print a.gameboard
        if turn == x:
          turn = o
        else:
          turn = x
  
  if a.Winner != None:
    winner = 'X'
    print a.gameboard
    print "Player " + winner + " wins the game with his last piece at: " + str(a.winy) + ',' + str((6 - int(a.winx)))
    print str(a.pieceCounter) + " pieces were played"
 # elif a.Winner == 2:
 #   winner = 'O'
 #   print a.gameboard
 #   print "Player " + winner + " wins the game with his last piece at: " + str(a.winy) + ',' + str((6 - int(a.winx)))
 #   print str(a.pieceCounter) + " pieces were played"
  else:
    print a.gameboard
    print "game ends with no winner"
if __name__ == "__main__":
  main()