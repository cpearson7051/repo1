import sys

itemlist = []

def addItem(item):
  
  itemlist.append(item)
  print itemlist

def removeItem(item):
  if item in itemlist:
    itemlist.remove(item)
  else:
    print "that item is not in list, here is a view of what is in: " + str(itemlist)

def viewList():
  print itemlist


def main():
  
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