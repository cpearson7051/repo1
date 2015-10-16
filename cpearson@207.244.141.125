import random


def getAI():
  players = raw_input("How many AI will be playing: ")
  if int(players) > 7:
    print "too many, choose again"
    getAI()
  return players

def buildDeck(players):
  Hearts = []
  Diamonds = []
  Clubs = []
  Spades = []
  suits = [Hearts, Diamonds, Clubs, Spades]
  cards = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
  
  for i, value in enumerate(cards):
    Hearts.append(str(value) + " of Hearts")
    
    Diamonds.append(str(value) + " of Diamonds")
    Clubs.append(str(value) + " of Clubs")
    Spades.append(str(value) + " of Spades")
  #print suits
  deck = []
  for i,value in enumerate(suits):
    for j, value in enumerate(suits[i]):
      deck.append(suits[i][j])
  shuffleDeck(deck, players)

def shuffleDeck(deck, players):
    newDeck = []
    while len(deck) > 0:
      card = random.choice(deck)
      index = deck.index(card)
      deck.pop(index)
      newDeck.append(card)
      
    
    dealCards(newDeck, players)
    
def dealCards(newDeck, players):
  burncard = newDeck[0]

  newDeck.remove(burncard)

  AIplayer = []
  AIplayer.append("Human Player")
  for player in xrange(int(players)):
    AIplayer.append("player " + str(player))
  for index, value in enumerate(AIplayer):
    card = newDeck.pop()
   # AIplayer[index] += " " +card
    AIplayer[index] = value, card
  for index, value in enumerate(AIplayer):
    card = newDeck.pop()
    a = AIplayer[index][0]
    b = AIplayer[index][1]
    AIplayer[index] = a, b, card
    
  dealFlop(newDeck, AIplayer)
  
  
def dealFlop(deck, players):
  a = deck.pop()
  b = deck.pop()
  c = deck.pop()
  print "Flop is: " + a + " " + b + " " + c
  print " "
  flop = [a, b, c]
  dealTurn(deck, players, flop)
  
def dealTurn(deck, players, flop):
  a = deck.pop()
  print "turn card is: " + a
  print " "
  flop.append(a)
  print flop
  dealRiver(deck, players, flop)
  
def dealRiver(deck, players, community):
  a = deck.pop()
  print "River card is: " + a
  print " "
  community.append(a)
  print "Community cards are: " + str(community)  
  print " "
  print " "
  print players  



def main():
  print "Welcome to Christopher's Texas Hold'em"
  players = getAI()
  buildDeck(players)
 
  
  
  
if __name__ == "__main__":
  main()