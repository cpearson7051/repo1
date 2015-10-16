

class bowlingScore:

  def __init__(self, scorecard):
    self.scorecard = scorecard.split()
    self.scoreTotal = 0
    self.calcScore(self.scorecard)
    
  def calcScore(self, scorecard):
    
    if len(scorecard[-1]) >= 2:
      scorecard.append(scorecard[-1][-1])
      scorecard[-2] = scorecard[-2][:2]
    print str(len(scorecard))
    print scorecard   
    
    
    for i, char in enumerate(scorecard):
      if 'X' in scorecard[i]:
        self.scoreTotal += 10
        if (i+1) < len(scorecard):
          if 'X' in scorecard[i+1]:
            self.scoreTotal += 10
            if (i+2) < len(scorecard):
              if 'X' in scorecard[i+2]:
                self.scoreTotal += 10
              elif scorecard[i+2][0].isdigit():
                self.scoreTotal += int(scorecard[i+2][0])
          elif '/' in scorecard[i+1]:
            self.scoreTotal += 10
          
          else:   
            
            if scorecard[i+1][0].isdigit():
              self.scoreTotal += int(scorecard[i+1][0])
            if scorecard[i+1][1].isdigit():
              self.scoreTotal += int(scorecard[i+1][1])
            
      elif '/' in scorecard[i]:
        self.scoreTotal += 10
        if(i+1) <= len(scorecard):
          if 'X' in scorecard[i+1]:
            self.scoreTotal += 10
          else:
            self.scoreTotal += int(scorecard[i+1][0])
     
      else:
        
        if scorecard[i][0].isdigit():
          self.scoreTotal += int(scorecard[i][0])
        if i+1 < len(scorecard) and scorecard[i+1][0].isdigit():
          self.scoreTotal += int(scorecard[i+1][0])
       
      print 'calculating frame ' + str(i) 
    print self.scoreTotal
          
  
   
  
  
  
def main():
  score = 'X -/ X 5- 8/ 9- X 81 1- 4/X'
  bowlingScore(score)
  score = '62 71 X 9- 8/ X X 35 72 5/8'
  bowlingScore(score)
  score = 'X X X X X X X X X XXX'
  bowlingScore(score)
  
if __name__ == '__main__':
  main()