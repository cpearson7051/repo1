import sys
import os
itemlist = []

def addItem(item):
  #write to saved list
  with open('todo.txt', 'a+') as f:
    f.write(item)
  
  itemlist.append(item)
  print itemlist

def removeItem(item):
  if item in itemlist:
    itemlist.remove(item)
  else:
    print "that item is not in list, here is a view of what is in: " + str(itemlist)
  with open('todo.txt', 'w+') as f:
    for line in itemlist:
      f.write(line)
  f.close()
def viewList():
  #view from saved txt file
  with open('todo.txt', 'r') as f:
    for line in f:
      print line
  f.close()    
  #print itemlist
  

def main():
  #check if the todo list has been created and append 
  #file = open('todo.txt', 'a+')
  with open('todo.txt', 'r') as f:
    d = f.readlines()
    for line in d:
      itemlist.append(line)
    f.close()
  #cmd = sys.argv[1]
  quit = 0
  
  while quit < 1:
    cmd = raw_input('Enter command: add, remove, view, quit: ')
    if str(cmd) == "add":
      entry = raw_input('Enter item to add: ')
      addItem(entry)  
    if str(cmd) == "quit":
      quit = 1
    if str(cmd) == "remove":
      entry = raw_input('Enter what to remove: ')
      removeItem(entry)
    if str(cmd) == "view":
      viewList()



if __name__ == "__main__":
  main()