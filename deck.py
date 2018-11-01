# Deck
# list of card/empty list

# draw a card
# shuffle
# play a card
#__str__

import card
from card import Card

class Deck:

	### CONSTRUCTOR

	def __init__(self):
		self.fulldeck = []
		for i in range(1,14):
			self.fulldeck.append(Card("h", i))
			self.fulldeck.append(Card("d", i))
			self.fulldeck.append(Card("c", i))
			self.fulldeck.append(Card("s", i))


	def __str__(self):
		deck = ''
		for j in range(52):
			deck = deck + str(self.fulldeck[j]) + "\n"
		return deck




dealer_deck = Deck()
print(dealer_deck)
# self.fulldeck




	### METHODS / FUNCTIONS

