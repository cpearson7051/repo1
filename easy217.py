"""initialize a matrix by adding to first list

"""




def buildmatrix(n, logs):
  matrix = [[0]*n for x in range(n)]
  i = 0
  j = 0
  for i in xrange(n):
    for j in xrange(n):
      print matrix[i][j], 
    print ''
   
  fillmatrix(n, logs, matrix)

def oldmatrix(n, logs):
  matrix = [[0]*n for x in range(n)]
  matrix[0][0] = 15
  matrix[0][1] = 12
  matrix[0][2] = 13
  matrix[0][3] = 11
  matrix[1][0] = 19
  matrix[1][1] = 14
  matrix[1][2] = 8
  matrix[1][3] = 18
  matrix[2][0] = 13
  matrix[2][1] = 14
  matrix[2][2] = 17
  matrix[2][3] = 15
  matrix[3][0] = 7
  matrix[3][1] = 14
  matrix[3][2] = 20
  matrix[3][3] = 7
  
  fillmatrix(n, logs, matrix)

def fillmatrix(n,logs, matrix):
  smallest = min(matrix)
  print smallest
  smallest = min(smallest)
  print smallest
  while logs > 0:
    for k in xrange(n):
      smallest = min(min(matrix))
      for l in xrange(n):
        smallest = min(min(matrix))
        if int(matrix[k][l]) <= smallest:
          smallest = min(min(matrix))
          print "min = " + str(smallest)
          matrix[k][l] = matrix[k][l]+1
          logs -= 1
          print "moving a log at smallest" + str(smallest)
          print logs
          break
          
      if logs == 0:
        break
    if k == n and l == n:
      k = 0
      l = 0      
  i = 0
  j = 0
  for i in xrange(n):
    for j in xrange(n):
      print matrix[i][j], 
    print ''
    
  print str(matrix[0][0]) 
  
  
def main():
    n = raw_input('dimensions of array: ')
    n = int(n)
    logs = raw_input('logs to add: ')
    logs = int(logs)
    #buildmatrix(n, logs)
    
    print "-"*10
    
    oldmatrix(n, logs)
  
  
if __name__ == "__main__":
  main()  