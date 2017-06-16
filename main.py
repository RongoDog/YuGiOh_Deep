from Classes.DatabaseInterface import DatabaseInterface
from Classes.Deck import Deck
from Classes.DeckBuilder import DeckBuilder
from os import listdir

def main():
    databaseConnection = DatabaseInterface("./cards.cdb")

    availableDecks = listdir("./Decks")
    loadedDecks = []
    for availableDeck in availableDecks:
        newDeck = Deck()
        newDeckString = open("./Decks/%s" % availableDeck)
        readMainDeck = False
        readExtraDeck = False
        for line in newDeckString.readlines():

            if line.strip() == "#main":
                readMainDeck = True

            elif line.strip() == "#extra":
                readMainDeck = False
                readExtraDeck = False

            elif readMainDeck == True:
                if (newDeck.addCard(line, databaseConnection) == False):
                    continue

            elif readExtraDeck == True:
                newDeck.addCard(line, databaseConnection)
        loadedDecks.append(newDeck)

    deckBuilder = DeckBuilder(loadedDecks, databaseConnection)

if __name__ == '__main__':
    main()


