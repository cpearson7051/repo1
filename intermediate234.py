

class spellCheck:

  def __init__(self, testWord):
    testDict = open('/usr/share/dict/words/', 'r')
    self.dictWords = testDict.read()
    testDict.close()
    self.check(testWord)
    
  def check(self,testWord):
    errWord = ''
    for i in xrange(len(testWord)):
      if testWord[:i] in self.dictWords:
        errWord = testWord[:i+1] + '<' + testWord[i+1:]
      else:
        continue
    print errWord
    
    
    
def main():
  spellCheck('accomodate')
  spellCheck('acknowlegement')
  spellCheck('arguemint')
  spellCheck('comitmment')
  spellCheck('deductabel')
  spellCheck('depindant')
  spellCheck('existanse')
  spellCheck('forworde')
  spellCheck('herrass')
  spellCheck('inadvartent')
  spellCheck('judgement')
  spellCheck('occurrance')
  spellCheck('parogative')
  spellCheck('suparseed')

if __name__ == '__main__':
  main()