from Deck import Deck
from scipy.stats.stats import pearsonr

class DeckBuilder(object):

    def __init__(self, decks, database):
        self.decks = decks
        self.database = database
        self.wantedCoefficients = {}
        self.averageCoefficients()
        self.deck = Deck()
        self.buildDeck()

    def buildDeck(self):

        nbCardsMax = 50
        self.deck.addCard("70781052", self.database)
        tempDeck = self.deck

        # This is going to be a big query. Fingers crossed
        allCards = self.database.fetchAllCards()
        for card in allCards:
            if (len(self.deck.cards) > nbCardsMax):
                break
            else:
                tempDeck.addCard2(card)
                if (self.determineCoefficientDifference(tempDeck.determineCoefficients()) >
                        self.determineCoefficientDifference(self.deck.determineCoefficients())):
                    self.deck.addCard2(card)
                else:
                    tempDeck = self.deck

        self.deck.writeDeck()
        print self.determineCoefficientDifference(self.deck.determineCoefficients())

    def determineAverageNumberOfCards(self):
        totalCards = 0
        for deck in self.decks:
            totalCards += len(deck.cards)
        return totalCards/len(self.decks)

    def determineCoefficientDifference(self, coefficients):
        targetList = []
        comparisionList = []
        for key in self.wantedCoefficients:
            targetList.append(self.wantedCoefficients[key])
            if key in coefficients:
                comparisionList.append(coefficients[key])
            else:
                comparisionList.append(0)
        for key in coefficients:
            if key in self.wantedCoefficients:
                continue
            else:
                targetList.append(0)
                comparisionList.append(coefficients[key])
        return pearsonr(targetList, comparisionList)


    def averageCoefficients(self):
        for deck in self.decks:
            deckCoefficients = deck.determineCoefficients()
            self.addDeckCoefsToAvg(deckCoefficients)

        for coefficientKey in self.wantedCoefficients:
            self.wantedCoefficients[coefficientKey] = self.wantedCoefficients[coefficientKey] / len(self.decks)

    def addDeckCoefsToAvg(self, deckCoefficients):
        for coefficientKey in deckCoefficients:
            if coefficientKey in self.wantedCoefficients:
                self.wantedCoefficients[coefficientKey] += deckCoefficients[coefficientKey]
            else:
                self.wantedCoefficients[coefficientKey] = deckCoefficients[coefficientKey]

