class Deck:
    def __init__(self, nbOfCards):
        self.deck = list(range(0, nbOfCards))

    def dealIntoNewStack(self):
        self.deck.reverse()
    

    # Takes positive and negative input
    def cut(self, nbToCut):
        cut = self.deck[ :nbToCut]
        newDeck = self.deck[nbToCut:: ]
        self.deck = newDeck + cut
    

    def dealWithIncrement(self, increment):
        deckSize = len(self.deck)
        dealt = [None] * deckSize
        i = 0

        while self.deck:
            if dealt[i] is None:
                dealt[i] = self.topCard()
            i += increment

            if i > deckSize:
                i = i - deckSize
        
        self.deck = dealt

    def topCard(self):
        return self.deck.pop(0)

    def cards(self):
        return self.deck

if __name__ == "__main__":
    # TODO: parse input and execute it :D


    






     