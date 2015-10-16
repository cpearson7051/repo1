import random
import re

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
 # shuffleDeck(deck, players)
  return deck
  
def shuffleDeck(deck):
    newDeck = []
    while len(deck) > 0:
      card = random.choice(deck)
      index = deck.index(card)
      deck.pop(index)
      newDeck.append(card)
      
    return newDeck
    #dealCards(newDeck, players)
    
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
    
  #dealFlop(newDeck, AIplayer)
  return AIplayer
  
def dealFlop(deck):
  a = deck.pop()
  b = deck.pop()
  c = deck.pop()
  print "Flop is: " + a + " " + b + " " + c
  print " "
  flop = [a, b, c]
  #dealTurn(deck, players, flop)
  return flop
  
def dealTurn(deck):
  a = deck.pop()
  print "turn card is: " + a
  print " "
  #flop.append(a)
  #print flop
  return a
  #dealRiver(deck, players, flop)
  
def dealRiver(deck):
  a = deck.pop()
  print "River card is: " + a
  print " "
  #community.append(a)
  #print "Community cards are: " + str(community)  
  print " "
  print " "
   
  return a
  
def checkHand(hand, community):
  cards = list(hand) 
  #print 'the hand i got is ' + str(hand[:])
 # print 'the community i got is ' + str(community)
  #print cards
  #print "Check hands"
  for i in xrange(len(community)):
    cards.append(community[i])
  royalFlush(cards)
  pair(cards)
  
def pair(hand):
  best = []
  for card in hand:
    cur = re.search(r'([A-Za-z]+)(.of.)(.*)', card)
    if cur is not None:
      if cur.group(1) == "Ace":
        best.append('14' + cur.group(2) + cur.group(3))
      elif cur.group(1) == "King":
        best.append('13' + cur.group(2) + cur.group(3))
      elif cur.group(1) == "Queen":
        best.append('12' + cur.group(2) + cur.group(3))
      elif cur.group(1) == "Jack":
        best.append('11' + cur.group(2) + cur.group(3))
    cur = re.search(r'([1-9]+)(.of.)(.*)', card)
    if cur is not None:
      best.append(cur.group(1) + cur.group(2) + cur.group(3))
    cur = None  
    
  print sorted(best)
    
def royalFlush(hand):
  theking = None
  theace = None
  thequeen = None
  thejack = None
  theten = None  
  for card in hand:
    ace = re.search(r'(Ace)(.of.)(.*)', card)
    if ace is not None:
      theace = ace
      
    king = re.search(r'(King)(.of.)(.*)', card)
    if king is not None:
      theking = king 
      
    queen = re.search(r'(Queen)(.of.)(.*)', card)
    if queen is not None:
      thequeen = queen 
    
    jack = re.search(r'(Jack)(.of.)(.*)', card)
    if jack is not None:
      thejack = jack 
    
    ten = re.search(r'(10)(.of.)(.*)', card)
    if ten is not None:
      theten = ten 

  if theking is not None and theace is not None and thequeen is not None and thejack is not None and theten is not None:
    if theking.group(3) == theace.group(3) == thequeen.group(3) == thejack.group(3) == theten.group(3):
      print " "
      print " "
      print "royal flush"
      print theace, theking, thequeen, thejack, theten
    else:
      print "straight"
      theking = None
      theace = None
      thequeen = None
      thejack = None
      theten = None
  



def main():
  print "Welcome to Christopher's Texas Hold'em"
  players = getAI()
  deck = buildDeck(players)
  shuffledDeck = shuffleDeck(deck)
  playerHands = dealCards(shuffledDeck, players)
  flop = dealFlop(shuffledDeck)
  communityCards = flop
  turn = dealTurn(shuffledDeck)
  communityCards.append(turn)  
  river = dealRiver(shuffledDeck)
  communityCards.append(river)
  print "Community Cards: "
  print " "
  print communityCards
  print ' '
  print "Show Hands"
  print " "
  
  for i in range(len(playerHands)):
    print playerHands[i][:]
  
  for i in range(len(playerHands)):
    checkHand(playerHands[i], communityCards)
  
  
if __name__ == "__main__":
  main()