from DatabaseInterface import DatabaseInterface, Card

class Deck(object):

    TYPE_IDENTIFIER = 0
    TYPE_COUNT = 1

    def __init__(self):
        self.cards = []
        self.types = []
        self.totalLevel = 0

    def addCard2(self, card):
        self.cards.append(card)
        self.determineType(card[Card.TYPE])
        if card[Card.LEVEL] > 0 or card[Card.LEVEL] < 15:
            self.incrementLevel(card[Card.LEVEL])
        return

    def addCard(self, id, database):
        card = database.fetchCard(id)
        if card is None:
            return False
        self.cards.append(card)
        self.determineType(card[Card.TYPE])
        if card[Card.LEVEL] > 0 or card[Card.LEVEL] < 15:
            self.incrementLevel(card[Card.LEVEL])
        return True

    def incrementLevel(self, level):
        self.totalLevel += level
        return

    def determineType(self, type):
        for currentType in self.types:
            if (currentType[Deck.TYPE_IDENTIFIER] == type):
                currentType[Deck.TYPE_COUNT] = currentType[Deck.TYPE_COUNT] + 1
                return
        self.types.append([type, 1])
        return

    def determineCoefficients(self):
        coefs = {}
        for type in self.types:
            coefs['%d' % type[Deck.TYPE_IDENTIFIER]] = float(type[Deck.TYPE_COUNT])/len(self.cards)

        coefs["level"] = self.totalLevel

        return coefs

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






