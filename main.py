import random


class Cards:
    def __init__(self):
        self.market = []
        self.marketClone = [] # Constant
        self.CommitCard = ''
        self.CommitList = []
    
    def create_deck(self):
        self.deck = []
        for i in range(5):
            self.shape_list = []
            self.exception = [0, 6, 9, 15, 16, 17, 18, 19]
            for j in range(21):
                if j in self.exception:
                    pass
                else:
                    self.shape_list.append(j)
            self.deck.append(self.shape_list)
        return self.deck

    def print_deck(self):
        print(self.deck)
    
    def gen_market(self):
        self.shape_name = ["Circles", "Cross", "Triangle", "Rectangle", "Star"]
        for y in range(len(self.deck)):
            for z in self.deck[y]:
                self.market.append(self.shape_name[y] + str(z))
                self.marketClone.append(self.shape_name[y] + str(z))
        return self.market, self.marketClone

    def shuffle_market(self):
        random.shuffle(self.market)
        return self.market

    def assign_firstCard(self):
        randomInt = random.randint(0, (len(self.market) - 1))
        self.CommitCard = self.market[randomInt]
        self.market.pop(randomInt)
        self.CommitList.append(self.CommitCard)
        return self.CommitCard

    def print_market(self):
        for i in self.market:
            print(i)

    def tender(self, gameObj):
        lenOfCards = []
        add = 0
        for i in range(gameObj.numOfPlayers):
            for j in gameObj.newPlayerList[i].playerCards:
                testSum = gameObj.newPlayerList[i].check_for_digit(j)
                add += testSum
            lenOfCards.append(add)
        smallest = 0
        smallestIndex = 0
        extra = 0
        extraIndex = 0
        for k in lenOfCards:
            for l in lenOfCards:
                if lenOfCards.index(l) == lenOfCards.index(k):
                    pass
                else:
                    if k < l:
                        smallest = k
                        smallestIndex = lenOfCards.index(k)
                    elif k == l:
                        smallest, extra = k, l
                        smallestIndex, extraIndex = lenOfCards.index(k), lenOfCards.index(l)
        
        if extra == 0:
            print("Ran out of market, Winner upon tender is", gameObj.newPlayerList[smallestIndex].alias)
        else:
            print("Ran out of market, Winners upon tender are", gameObj.newPlayerList[smallestIndex].alias, "and", gameObj.newPlayerList[extraIndex].alias)
        raise SystemExit("The End... Quiting game!!!")

    def goto_market(self, playerObj):
        if len(self.market) > 0:
            playerObj.playerCards.append(self.market[0])
            playerObj.playerCardsIndex = playerObj.stack_index(self)
            self.market.pop(0)
        else:
            self.tender(gameloop)
        #playerObj.print_playerDetails()
        return playerObj.playerCards
        return playerObj.playerCardsIndex


class Player:
    def __init__(self):
        self.playerCards = []
        self.playerCardsIndex = []
        self.name = ''
        self.alias = ''
        self.cardIndex = 0
        self.chosenIndex = 0
        self.chosenCard = ''
        self.cardDigit = 0
        self.commitDigit = 0


    def create_profile(self):
        self.name = input("Enter your alias(Avatar_name)>>> ")
        self.alias = self.name[0].upper()
        return self.alias

    def create_stack(self, cardObj):
        print(self.alias)
        for i in range(5):
            randomNum = random.randint(0, (len(cardObj.market) - 1))
            self.playerCards.append(cardObj.market[randomNum])
            cardObj.market.pop(randomNum)
        return self.playerCards
        
    def stack_index(self, cardObj):
        self.playerCardsIndex.clear()
        for item in self.playerCards:
            for obj in cardObj.marketClone:
                if obj == item:
                    self.cardIndex = cardObj.marketClone.index(obj)
            self.playerCardsIndex.append(self.cardIndex)
        return self.playerCardsIndex

    def player_stack(self, cardObj):
        self.create_stack(cardObj)
        self.stack_index(cardObj)

    def print_playerDetails(self):
        print(self.alias)
        print(self.playerCards)

    def check_for_digit(self, cardName):
        num = ''
        for item in cardName:
            if item.isdigit():
                num += item
        cardNum = int(num)
        return cardNum

    def card_selection(self, cardObj):
        self.print_playerDetails()
        print("\nThe presently committed card is", cardObj.CommitCard, "\n")
        self.chosenIndex = int(input("Enter the order of the card you want to play, e.g if 1st enter 1 | Press 0 to go to Market>>> "))

    def commit_card(self, cardObj):
        self.card_selection(cardObj)
        self.chosenCard = self.playerCards[self.chosenIndex - 1]
        self.cardDigit = self.check_for_digit(self.chosenCard)
        self.commitDigit = self.check_for_digit(cardObj.CommitCard)
        conditions = (cardObj.CommitCard[:4] == self.chosenCard[:4]) or (self.commitDigit == 20) or (self.cardDigit == self.commitDigit) or (self.cardDigit == 20)
        if conditions and self.chosenIndex != 0:
            cardObj.CommitCard = self.chosenCard
            print(self.alias, "played", self.chosenCard)
            self.playerCards.pop(self.chosenIndex - 1)
            self.playerCardsIndex.pop(self.chosenIndex - 1)
            cardObj.CommitList.append(cardObj.CommitCard)
        elif self.chosenIndex == 0:
            cardObj.goto_market(self)
            print(self.alias, "went to Market")
        else:
            print("Your card is not acceptable. Commit a valid card | Press 0 to Go to Market")
            self.commit_card(cardObj)
        return cardObj.CommitCard


class AIPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = 'AI'
        self.alias = 'AI'
        self.playerCards = []
        self.playerCardsIndex = []

    def ai_stack(self, cardObj):
        self.playerCards = self.create_stack(cardObj)
        self.playerCardsIndex = self.stack_index(cardObj)
        #print(self.playerCards)
    
    def ai_decision(self, cardObj):
        random.shuffle(self.playerCards)
        for j in self.playerCards:
            self.chosenCard = j
            self.cardDigit = self.check_for_digit(self.chosenCard)
            self.commitDigit = self.check_for_digit(cardObj.CommitCard)
            conditions = (cardObj.CommitCard[:4] == self.chosenCard[:4]) or (self.commitDigit == 20) or (self.cardDigit == self.commitDigit) or (self.cardDigit == 20)
            if conditions:
                cardObj.CommitCard = self.chosenCard
                cardObj.CommitList.append(cardObj.CommitCard)
                print(self.alias, "played", self.chosenCard)
                self.playerCardsIndex.pop(self.playerCards.index(self.chosenCard))
                self.playerCards.remove(self.chosenCard)
                break
        else:
            cardObj.goto_market(self)
            print(self.alias, "went to Market")
        return cardObj.CommitCard


class Gameplay:
    def __init__(self):
        self.testcase = 0
        self.playerList = []
        self.numOfaiPlayers = 0
        self.numOfPlayers = 0
        self.newPlayerList = []
        self.firstPlayerIndex = 0
        self.winner = ''
        self.runGame = True
        self.initialRoundGuide = 0
        self.newRoundGuide = 1

    def num_ai(self):
            self.numOfaiPlayers = int(input("Choose Number of AI opponents | cannot be greater than 4>>> "))
            if self.numOfaiPlayers <= 4:
                self.numOfPlayers = 1 + self.numOfaiPlayers
            else:
                self.num_ai()
            return self.numOfPlayers, self.numOfaiPlayers

    def select_first_player(self, cardObj):
        print("The Default commited card is", cardObj.CommitCard)
        for i in range(self.numOfPlayers):
            self.newPlayerList.append(self.playerList[i])
        randomDieOutput = random.randint(0, (self.numOfaiPlayers))
        self.firstPlayerIndex = randomDieOutput
        print("First player is", self.newPlayerList[self.firstPlayerIndex].alias)
        j = self.firstPlayerIndex
        return self.firstPlayerIndex

    def play(self, runIndex, cardObj):
        self.initialRoundGuide = len(cardObj.CommitList)
        print(self.initialRoundGuide)
        if runIndex == 0:
            self.newPlayerList[runIndex].commit_card(cardObj)
        else:
            self.newPlayerList[runIndex].ai_decision(cardObj)
        self.newRoundGuide = len(cardObj.CommitList)
        self.initialRoundGuide = self.newRoundGuide
        print(self.newRoundGuide)

    def hold_on(self, runIndex, playerObj, cardObj):
        if runIndex == 0:
            runIndex = self.numOfaiPlayers
        else:
            runIndex -= 1
        print(f"Hold on | Sorry, {self.newPlayerList[runIndex].alias} gets to play | It will be the next players turn sooner...")
        initialCardLength = len(self.newPlayerList[runIndex].playerCards)
        self.play(runIndex, cardObj)
        newCardLength = len(self.newPlayerList[runIndex].playerCards)
        visitedMarket = newCardLength > initialCardLength
        if (playerObj.check_for_digit(cardObj.CommitCard) == 1) and (not(visitedMarket)):
            if runIndex == self.numOfaiPlayers:
                runIndex = 0
                self.hold_on(runIndex, playerObj, cardObj)
            else:
                runIndex += 1
                self.hold_on(runIndex, playerObj, cardObj)
        else:
            print("Next player can now play...")
    
    def pick_two(self, playerObj, cardObj):
        print(playerObj.alias, "picked 2")
        for i in range(2):
            cardObj.goto_market(playerObj)
    
    def pick_three(self, playerObj, cardObj):
        print(playerObj.alias, "picked 3")
        for i in range(3):
            cardObj.goto_market(playerObj)

    def skip(self, runIndex, playerObj):
        print(playerObj.alias, "skipped")
        if runIndex < self.numOfaiPlayers:
            runIndex += 1
        else:
            runIndex = 0

    def general_market(self, runIndex, playerObj, cardObj):
        print("General Market >>>|<<<")
        if runIndex == 0:
            runIndex = self.numOfaiPlayers
        else:
            runIndex -= 1
        for i in range(self.numOfPlayers):
            if runIndex == i:
                pass
            else:
                cardObj.goto_market(self.newPlayerList[i])
        print(f"General Market | Now, {self.newPlayerList[runIndex].alias} should play...")
        initialCardLength = len(self.newPlayerList[runIndex].playerCards)
        self.play(runIndex, cardObj)
        newCardLength = len(self.newPlayerList[runIndex].playerCards)
        visitedMarket = newCardLength > initialCardLength
        if (playerObj.check_for_digit(cardObj.CommitCard) == 14) and (not(visitedMarket)):
            if runIndex == self.numOfaiPlayers:
                runIndex = 0
                self.general_market(runIndex, playerObj, cardObj)
            else:
                runIndex += 1
                self.general_market(runIndex, playerObj, cardObj)
        else:
            print("Next player can go ahead and play...")

    def card_test(self, runIndex, playerObj, cardObj):
        self.testcase = playerObj.check_for_digit(cardObj.CommitCard)
        if self.testcase == 1:
            self.hold_on(runIndex, playerObj, cardObj)
        elif self.testcase == 2:
            self.pick_two(playerObj, cardObj)
        elif self.testcase == 5:
            self.pick_three(playerObj, cardObj)
        elif self.testcase == 8:
            self.skip(runIndex, playerObj)
        elif self.testcase == 14:
            self.general_market(runIndex, playerObj, cardObj)
        else:
            self.play(runIndex, cardObj)
        

    def winner_test(self, playerObj):
        if len(playerObj.playerCards) == 0:
            self.winner = playerObj.alias
            self.runGame = False
            print(self.winner, "is the Champion!!!")
        elif len(playerObj.playerCards) == 1:
            print(playerObj.alias, "has one more card left")
        return self.winner, self.runGame

    def run(self):
        c = Cards()
        c.create_deck()
        c.gen_market()

        p1 = Player()
        a1 = AIPlayer()
        a2 = AIPlayer()
        a3 = AIPlayer()
        a4 = AIPlayer()
        self.playerList = [p1, a1, a2, a3, a4]
        a1.alias = "AI_1"
        a2.alias = "AI_2"
        a3.alias = "AI_3"
        a4.alias = "AI_4"

        p1.create_profile()
        p1Cards = self.playerList[0].player_stack(c)

        self.num_ai()
        for i in range(self.numOfaiPlayers):
            self.playerList[i + 1].ai_stack(c)

        c.shuffle_market()

        c.assign_firstCard()

        self.select_first_player(c)

        while self.runGame == True:
            k = self.firstPlayerIndex
            while (k < self.numOfPlayers) and (self.winner == ''):
                #if self.newRoundGuide > self.initialRoundGuide:
                self.card_test(k, self.newPlayerList[k], c)
                #else:
                #self.play(k, c)
                self.winner_test(self.newPlayerList[k])
                if k == self.numOfaiPlayers:
                    k = 0
                else:
                    k += 1
        else:
            print(f"There is a winner already!: {self.winner}")
        

if __name__ == '__main__':
    gameloop = Gameplay()
    gameloop.run()
    