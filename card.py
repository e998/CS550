# 11/1/2018

class Card: 
	
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		# create local variable rank, don't want to permanently change the number of the rank
		rank = self.rank
		suit = self.suit
		if rank == 1:
			rank = "Ace"
		elif rank == 11:
			rank = "Jack"
		elif rank == 12:
			rank = "Queen"
		elif rank == 13:
			rank = "King"
		else:
			rank = str(self.rank)
		if suit == "h":
			suit = "Hearts"
		elif suit == "d":
			suit = "Diamonds"
		elif suit == "c":
			suit = "Clubs"
		elif suit == "s":
			suit = "Spades"

		return str(rank) + " of " + str(suit)

# suit: h, d, c, s
# rank: 2-10, J, Q, K, A - 1-13
#__string__

