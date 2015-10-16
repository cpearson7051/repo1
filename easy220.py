"""In this challenge, we are going to take a sentence and mangle it up 
by sorting the letters in each word. So, for instance, if you take the 
word "hello" and sort the letters in it, you get "ehllo". If you take the 
two words "hello world", and sort the letters in each word, you get "ehllo dlorw"."""

import re
import string

def mixedword(word):

 #if single word
  sortedword = sorted(word)
  #sorted returns a list so make it a string again using join
  sortedstring = ''.join(sortedword)
 # print sortedstring
  
  #use re to find wordchars but not spaces
  multistring = re.findall(r'([\S]+)', word)
  #print multistring
  print ' '.join(multistring)
  
  #jumble each index and add to a list
  jumbled = []
  for index, words in enumerate(multistring):
    
    #check for punctuation and apostrophes
    checked = re.search(r'([\W])', words)
    #check for capitalizations
    caps = re.search(r'([A-Z])', words)
    if caps:
      #swap to lowercase
      capchar = str(caps.group())
      lowered = words.lower()
      words = lowered
     
       
    if checked:
      specialchar = str(checked.group())
      #at index
      tmplist = list(words)
      charindex = tmplist.index(specialchar)
      jumblelist = sorted(words)
      jumblelist.remove(specialchar)
      jumblelist.insert(charindex, specialchar)
      jumbleword = ''.join(jumblelist)
      if caps: #bring back the cap if there was one
        jumbleword = jumbleword.title()
        
    
    else:
      jumbleword = ''.join(sorted(words)) #turn the list of letters back into a string  
      if caps:
        jumbleword = jumbleword.title()
    jumbled.append(jumbleword)
    
      
    
  print ' '.join(jumbled)
   
  

def main():
  mixedword("This challenge doesn't seem so hard.")
  mixedword("There are more things between heaven and earth, Horatio, than are dreamt of in your philosophy.")
  mixedword("Eye of Newt, and Toe of Frog, Wool of Bat, and Tongue of Dog.")
if __name__ == "__main__":
  main()