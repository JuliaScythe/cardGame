import json

class Card:
    def __init__(self, cardId):
        self.cardId = cardId

    def onDraw(self):
        print("boom")

class Creature(Card):
    def onDraw(self):
        print("bing")

def loadCard(cardId):
    # Try to open the file with the card
    try:
        cardFile = open(f"cards/{cardId}.json")
    except FileNotFoundError as e:
        print(f"Card {cardId} not found!")
        raise e

    # Now, try to parse the card
    try:
        cardStruct = json.load(cardFile)
        # First, check the ID is equal to what we expect
        if cardStruct[id] != cardId:
            raise BaseException("CardID did not match what we expect!")

        # If the card is a creature, make a creature with it
        if cardStruct.type == "creature":
            return loadCreature(cardStruct)

    except Exception as e:
        print(f"Could not parse card {cardId}!")
        raise e


def loadCreature(cardStruct):
    
