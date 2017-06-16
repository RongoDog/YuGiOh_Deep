from DatabaseInterface import DatabaseInterface, Card

class Deck(object):

    TYPE_IDENTIFIER = 0
    TYPE_COUNT = 1

    def __init__(self):
        self.cards = []
        self.types = []

    def addCard2(self, card):
        self.cards.append(card)
        self.determineType(card[Card.TYPE])
        return

    def addCard(self, id, database):
        card = database.fetchCard(id)
        if card is None:
            return False
        self.cards.append(card)
        self.determineType(card[Card.TYPE])
        return True

    def determineType(self, type):
        for currentType in self.types:
            if (currentType[Deck.TYPE_IDENTIFIER] == type):
                currentType[Deck.TYPE_COUNT] = currentType[Deck.TYPE_COUNT] + 1
                return
        self.types.append([type, 1])
        return

    def determineCoefficients(self):
        typeCoefs = {}
        for type in self.types:
            typeCoefs['%d' % type[Deck.TYPE_IDENTIFIER]] = float(type[Deck.TYPE_COUNT])/len(self.cards)
        return typeCoefs

    def printDeck(self):
        print "Deck"
        for card in self.cards:
            print(card)
        return

    def printTypes(self):
        print "Deck Types"
        for card in self.types:
            print(card)
        return

    def writeDeck(self):
        target = open("./Decks/ComputerBuiltDeck.ydk", 'w')
        target.write("#main\n")
        for card in self.cards:
            target.write(str(card[Card.ID]) + "\n")
        target.write("#extra\n")
        target.write("!side\n")






