import random


class Cards: # The card object is defined here
    def __init__(self):
        self.market = [] # Container for all cards
        self.marketClone = [] # Constant
        self.CommitCard = '' # Last Played card
        self.CommitList = [] # All played cards are stored here
    
    def create_deck(self):
        self.deck = []
        for _ in range(5):
            self.shape_list = []
            self.exception = [0, 6, 9, 15, 16, 17, 18, 19]
            for j in range(21):
                if j in self.exception:
                    pass
                else:
                    self.shape_list.append(j) # Adds the list of valid numbers for a whot game to the shapes list
            self.deck.append(self.shape_list) # Appending all five to a parent list called deck
        return self.deck # return deck upon call 

    def print_deck(self):
        print(self.deck)
    
    def generate_market(self):
        self.shape_name = ["Circles", "Cross", "Triangle", "Rectangle", "Star"] # An initialization of all the shape names
        for y in range(len(self.deck)):
            for z in self.deck[y]:
                self.market.append(self.shape_name[y] + str(z)) # This creates the list of all the cards with thee shape name appended to the beginning e.g Circle10
                self.marketClone.append(self.shape_name[y] + str(z)) # Stores a duplicate of the above step in another list
        return self.market, self.marketClone

    def shuffle_market(self):
        random.shuffle(self.market) # Shuffles Market... Market is the list containing all the card deck
        return self.market

    def assign_firstCard(self): # This method assigns the initial card that decides what the first player is to play
        randomInt = random.randint(0, (len(self.market) - 1)) # Generate a random int between O and the number of cards in the market
        self.CommitCard = self.market[randomInt] # Picks the card at the randompositionn deduced earlier and stores it in the commit variacble
        self.market.pop(randomInt) # This card cannot exist twice so since it is already in commit, it is removed from market.
        self.CommitList.append(self.CommitCard) # This list stores all the commits i.e all played cards but it is initially empty and now we add commit into it
        return self.CommitCard

    def print_market(self):
        for i in self.market:
            print(i)

    def tender(self, gameObj):
        lenOfCards = []
        add = 0
        for i in range(gameObj.numOfPlayers): # Loop through the list of players and select theindex of each player
            for j in gameObj.newPlayerList[i].playerCards: # For each player access the list containing their unplayed cards
                testSum = gameObj.newPlayerList[i].check_for_digit(j) # Pick the numeric values from all the cards
                add += testSum # sum those numeric values
            lenOfCards.append(add) # store the numeric sums of cards for all players in List called lenOfCards 
        
        smallest = lenOfCards[0] # Set the first element of the list as the smallest
        j = len(lenOfCards) 
        for l in range(1, j): # loop through the rest of the other players
            if smallest > lenOfCards[l]: # Compare the smallest element with the present element
                smallest = lenOfCards[l] # store the new smallest value in smallest
        smallestIndex = lenOfCards.index(smallest) # Select the index of the overall smallest element and store in smallestIndex
        
        print("Ran out of market, Winner upon tender is", gameObj.newPlayerList[smallestIndex].alias) # Declare the winner upon tender
        raise SystemExit("The End... Quiting game!!!") # quit the game

    def goto_market(self, playerObj): # An option for player to pick a card if non of its cards matches commit. 
        if len(self.market) > 0: # This can only be done when market is not empty 
            playerObj.playerCards.append(self.market[0]) # Append the first card in market to the players card list
            playerObj.playerCardsIndex = playerObj.stack_index(self) # Go to the PlayerClass and execute stack_index which refreshes list of indices of all player cards and store it in this variable 
            self.market.pop(0) # Remove the card selected away from market
        else: # This means market is empty
            self.tender(gameloop) # We choose to tender our cards then... call tender method.
        return playerObj.playerCards, playerObj.playerCardsIndex


class Player: # Defines the Players behaviors and characteristics
    def __init__(self): # Initializing the different characteristics of the player object
        self.playerCards = [] # this contains the players cards 
        self.playerCardsIndex = [] # this contains the list of the indicecs of this cards in the MarketClone(Constant market)
        self.name = '' # The name of the Player Obj
        self.alias = '' # The alias of the player obj
        self.cardIndex = 0 # Used to store the index of a card
        self.chosenIndex = 0 # Stores the index of the card the player wish to commit 
        self.chosenCard = '' # the card identifier that the player wants to commit
        self.cardDigit = 0 # The digit of the card that the player wants to commit 
        self.commitDigit = 0 # The digit of the card that is in commit
        self.cardShape = '' # The shape of the card that the player wants to commit 
        self.commitShape = '' # The shape of the card that is in commit 

    def create_profile(self): # creates a profile for the player
        self.name = input("Enter your alias(Avatar_name)>>> ") # Asks input for Human players choice name
        self.alias = self.name[0].upper() # Picks the first letter converts it to Uppercase and sets it as the alias
        return self.alias 

    def create_stack(self, cardObj): # create players cards
        print(self.alias)
        for _ in range(5): # Create 5 cards for the player
            randomNum = random.randint(0, (len(cardObj.market) - 1)) # pick randomly from market
            self.playerCards.append(cardObj.market[randomNum]) # adds it to player cards list
            cardObj.market.pop(randomNum) # removes the cards from market
        return self.playerCards # return the list of all of the current players cards
        
    def stack_index(self, cardObj): 
        self.playerCardsIndex.clear() # Clears Player Cards Indices list
        for item in self.playerCards: # loop through all player cards
            for obj in cardObj.marketClone: # Check through the constant clone of market
                if obj == item: # confirm if the players cards are in market clone
                    self.cardIndex = cardObj.marketClone.index(obj) # Then select the index of each card from market clone
            self.playerCardsIndex.append(self.cardIndex) # Put those indices in a list
        return self.playerCardsIndex

    def player_stack(self, cardObj): # Work on distribution of cards to players
        self.create_stack(cardObj) # calls the method that creates card 
        self.stack_index(cardObj) # calls the method that store the indices the cards created above

    def print_playerDetails(self): # Prints player details
        print(self.alias)
        print(self.playerCards)

    def check_for_digit(self, cardName): # Finds numeric value is a Card identifier/name
        num = '' # an empty string to capture the digits
        for item in cardName: # in card name, loop through all characters
            if item.isdigit(): # if item is a digit
                num += item # append to num e.g Star21 => '2' + '1' = '21'
        cardNum = int(num) # convert num to an integer and store it cardNum
        return cardNum # return that integer

    def check_for_shape(self, cardName): # checks for the name of the shape in the card name
        for item in cardName: # in card name, loop through all characters
            if item.isalpha() == True: # if item is a string
                shape += item # add item to shape e.g Star21 => 'S' + 't' + 'a' + 'r' = 'Star'
        return shape # return shape

    def card_selection(self, cardObj): # Prompts player to play its card
        self.print_playerDetails() #Prints the details of the one to play
        print("\nThe presently committed card is", cardObj.CommitCard, "\n") # Informs player about the last played card(commit)
        self.chosenIndex = int(input("Enter the order of the card you want to play, e.g if 1st enter 1 | Press 0 to go to Market>>> ")) # prompt to enter an input or go to market

    def commit_card(self, cardObj): # Handles card validation
        self.card_selection(cardObj) # calls the prompt for player to play a card
        self.chosenCard = self.playerCards[self.chosenIndex - 1] # stores the chosen card in a container for validation
        self.cardShape = self.check_for_shape(self.chosenCard) # Check for the shape of the card player played and store the shape for validattion
        self.cardDigit = self.check_for_digit(self.chosenCard) # Check for the digit of the card player played and store the digit for validattion
        self.commitShape = self.check_for_shape(cardObj.CommitCard) # Check for the shape of last played card
        self.commitDigit = self.check_for_digit(cardObj.CommitCard) # Check for the digit of last played card
        conditions = (self.commitShape == self.cardShape) or (self.commitDigit == 20) or (self.cardDigit == self.commitDigit) or (self.cardDigit == 20) # conditions for validation
        if conditions and self.chosenIndex != 0: # If condition is met and player did not decide to pick a card from market
            cardObj.CommitCard = self.chosenCard # Accept the card and make it the new last played card
            print(self.alias, "played", self.chosenCard) # Inform all players about current players card choice
            self.playerCards.pop(self.chosenIndex - 1) # Upon accepting the card from the user, remove it from the list of cards the player can play
            self.playerCardsIndex.pop(self.chosenIndex - 1) # remove its index from the list of player card indices
            cardObj.CommitList.append(cardObj.CommitCard) # add the card to list of previously played cards
        elif self.chosenIndex == 0: # If player decided to go to market to pick a card
            cardObj.goto_market(self) # call the method that does that in the card Object class
            print(self.alias, "went to Market") # Tell the players that current player decided to visit the market
        else: # if none of the conditions are met,
            print("Your card is not acceptable. Commit a valid card | Press 0 to Go to Market") # Reject the card and prompt the user for another input
            self.commit_card(cardObj) # rerun current method
        return cardObj.CommitCard # return Commited Card


class AIPlayer(Player): # AI players special behavior and characteristics are defined here, it  inherits frfom Player class
    def __init__(self):
        super().__init__() # Inheritance in Python
        self.name = 'AI'
        self.alias = 'AI'
        self.playerCards = []
        self.playerCardsIndex = []

    def ai_stack(self, cardObj): # distributes cards to the ai players
        self.playerCards = self.create_stack(cardObj)
        self.playerCardsIndex = self.stack_index(cardObj)
    
    def ai_decision(self, cardObj): # The ai's logic for selecting the best card... No future prediction, just a simple thought process
        random.shuffle(self.playerCards) # Shuffle ai's cards
        for j in self.playerCards: # Run a test on all cards
            self.chosenCard = j # The current chosen card
            self.cardShape = self.check_for_shape(self.chosenCard) # Check for the shape of the ai's card 
            self.commitShape = self.check_for_shape(cardObj.CommitCard) # Check for the shape of the last played card
            self.cardDigit = self.check_for_digit(self.chosenCard) # Check for the digit of the ai's card
            self.commitDigit = self.check_for_digit(cardObj.CommitCard) # Check for the digit of the last played card
            conditions = (self.commitShape == self.cardShape) or (self.commitDigit == 20) or (self.cardDigit == self.commitDigit) or (self.cardDigit == 20) # conditions for validation
            if conditions: # if condition is met
                cardObj.CommitCard = self.chosenCard # Accept card
                cardObj.CommitList.append(cardObj.CommitCard) # Add card to list of last played cards 
                print(self.alias, "played", self.chosenCard) # Inform players about ai's choice
                self.playerCardsIndex.pop(self.playerCards.index(self.chosenCard)) # Remove card index from list of ai cards indices 
                self.playerCards.remove(self.chosenCard) # remove card from list of cards ai can play
                break # stop looking for other acceptable cards
        else: # If condition is not met
            cardObj.goto_market(self) # ai should pick a card from market
            print(self.alias, "went to Market") # Inform all about ai's decision to visit the market
        return cardObj.CommitCard


class Gameplay: # Game Manager
    def __init__(self): 
        self.testcase = 0
        self.playerList = []
        self.numOfaiPlayers = 0
        self.numOfPlayers = 0
        self.newPlayerList = []
        self.firstPlayerIndex = 0
        self.winner = ''
        self.runGame = True
        self.k = 0

    def num_ai(self):
            self.numOfaiPlayers = int(input("Choose Number of AI opponents | cannot be greater than 4>>> "))
            if self.numOfaiPlayers <= 4:
                self.numOfPlayers = 1 + self.numOfaiPlayers
            else:
                print("...Try Again...")
                self.num_ai()
            return self.numOfPlayers, self.numOfaiPlayers

    def select_first_player(self, cardObj):
        print("The Default commited card is", cardObj.CommitCard)
        for i in range(self.numOfPlayers):
            self.newPlayerList.append(self.playerList[i])
        randomDieOutput = random.randint(0, (self.numOfaiPlayers))
        self.firstPlayerIndex = randomDieOutput
        print("First player is", self.newPlayerList[self.firstPlayerIndex].alias)
        return self.firstPlayerIndex

    def play(self, runIndex, cardObj):
        if runIndex == 0:
            self.newPlayerList[runIndex].commit_card(cardObj)
        else:
            self.newPlayerList[runIndex].ai_decision(cardObj)  

    def hold_on(self, runIndex, playerObj, cardObj):
        print("Hold on Fella's...", playerObj, "has another chance to play")
        self.play(runIndex, cardObj)
        self.card_test(runIndex, playerObj, cardObj)
        
    def pick(self, playerObj, cardObj, num):
        if self.k == self.numOfaiPlayers:
            playerObj = self.newPlayerList[0]
        else:
            playerObj = self.newPlayerList[self.k + 1]

        print(playerObj, "is gifted", num, "cards")
        for _ in range(num):
            cardObj.goto_market(playerObj)
        self.skip()

    def pick_two(self, playerObj, cardObj, num):
        self.pick(playerObj, cardObj, num)

    def pick_three(self, playerObj, cardObj, num):
        self.pick(playerObj, cardObj, num)

    def skip(self):
        if self.k == self.numOfaiPlayers:
            self.k = 0
        else:
            self.k += 1
        print("---Skipped One Player---")

    def general_market(self, runIndex, playerObj, cardObj):
        print("...General Market... | All players are gifted a card except for current player")
        while True:
            if runIndex == self.numOfaiPlayers and  runIndex != self.k:
                runIndex = 0
            elif runIndex < self.numOfaiPlayers and  runIndex != self.k:
                runIndex += 1
            else:
                break
            playerObj = self.newPlayerList[runIndex]
            cardObj.goto_market(playerObj)
        self.play(runIndex, cardObj)
        self.card_test(runIndex, playerObj, cardObj)   

    def card_test(self, runIndex, playerObj, cardObj):
        self.testcase = playerObj.check_for_digit(cardObj.CommitCard)
        if self.testcase == 1:
            self.hold_on(runIndex, playerObj, cardObj)
        elif self.testcase == 2:
            self.pick_two(playerObj, cardObj, 2)
        elif self.testcase == 5:
            self.pick_three(playerObj, cardObj, 3)
        elif self.testcase == 8:
            self.skip()
        elif self.testcase == 14:
            self.general_market(runIndex, playerObj, cardObj)
        else:
            pass        

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
        c.generate_market()

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
        self.playerList[0].player_stack(c)

        self.num_ai()
        for i in range(self.numOfaiPlayers):
            self.playerList[i + 1].ai_stack(c)

        c.shuffle_market()

        c.assign_firstCard()

        self.select_first_player(c)

        self.k = self.firstPlayerIndex
        while (self.winner == '') and (self.runGame == True):
            self.play(self.k, c)
            self.card_test(self.k, self.newPlayerList[self.k], c)
            self.winner_test(self.newPlayerList[self.k])
            if self.k == self.numOfaiPlayers:
                self.k = 0
            else:
                self.k += 1
        
        print(f"There is a winner already!: {self.winner}")
        

if __name__ == '__main__':
    gameloop = Gameplay()
    gameloop.run()
    