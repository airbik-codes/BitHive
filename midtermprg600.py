
"""
Firstname: Aakib Kibria
Lastname: Khan
Username: akkhan9
StudentID: 157802224
Email: akkhan9@senecacollege.ca
"""
# 1 Marks
import sys
from random import randint

def rolldice():
    """
    function: rolldice prints two random numbers between 1 and 6 simulate two dices rolling. 
    The function should also print output of the numbers generated (Eg: 6 and 6) 
    return: int:total (total of two random numbers) 
    """
    # Generate two random numbers between 1 and 6 (inclusive) and store them in 'random_number1' and 'random_number2'.
    random_number1 = randint(1, 6)
    random_number2 = randint(1, 6)
    # Print the values of 'random_number1' and 'random_number2' to the console.
    print(f"{random_number1} and {random_number2}")
    # Calculate the sum of 'random_number1' and 'random_number2' and store it in the 'total' variable.
    total = random_number1 + random_number2
    # Convert the 'total' to an integer (in case it isn't already) and return it from the function.
    return int(total)
# 1 Marks 
def getplayers():
    """
    function:This functions asks user to provide an input of number of players. 
    Based on the number of players asks player names and create a list of player names and return player names
    If user entered invalid input for number of players (eg: string (a)) it throws an error and asks to retry 
    :return list:players (list of playernames entered by user)
    """
    # Start an indefinite loop that will run until a valid number of players is provided.
    while True:
        # Prompt the user to enter the number of players and store their input in 'user_input'.
        user_input = input("Please enter the number of players: ")
        # Check if the user input consists only of digits.
        if user_input.isdigit():
            # If it starts with a minus sign, it is considered an invalid input.
            if user_input.startswith('-'):
                print("Invalid input please try again")
            # Convert the valid user input to an integer and assign it to 'number_of_players'.
            else:
                number_of_players = int(user_input)
                break # Break out of the loop since a valid input has been provided.
        else:
            print("Invalid input please try again") # If the user input is not composed of digits, prompt them to try again.
    # Initialize variables for player tracking.
    player_number = 1 
    counter = 0
    players = []
    while counter < number_of_players:
        # Prompt the user to enter the name for each player, using 'player_number' for reference.
        player = input(f"Please enter player #{player_number} name: ")
        player_number += 1
        counter += 1
        players.append(player) # Append each player's name to the 'players' list.
    return players # Return the list of player names to the calling code
# 1 Marks
def getrounds():
    """
    function: This function asks user to enter the number of rounds they going to play 
    Based on the number of rounds entered as long it is valid return the number of rounds otherwise keep asking until a valid number entered. 
    :return int:roundcount (number of rounds)
    """
    # Implement your function here
    # Start an indefinite loop to repeatedly prompt the user for input.
    while True:
        # Prompt the user to enter the number of rounds and store their input in 'user_input'.
        user_input = input("Please enter how many rounds the players wish to play: ")
        if user_input.isdigit():   # Check if the user input consists only of digits.
            if user_input.startswith('-'): # If it starts with a minus sign, it is considered an invalid input.
                print("Invalid input please try again")
            else:
                roundcount = int(user_input) # Convert the valid user input to an integer and assign it to 'roundcount'.
                break # Break out of the loop since a valid input has been provided.
        else: # If the user input is not composed of digits, prompt them to try again.
            print("Invalid input please try again")

    return roundcount # Return the number of rounds to the calling code
# 4 Marks
def setgame():
    """
    function: This functions use the getplayers() function and getrounds() function to get player list and round count
    Using the above values setup a two dimensional (2D) list called game. The game list will have lists elements for each round and player 
    Eg: [[score1_1, score1_2, score1_3], [score2_1, score2_2, score2_3], [score3_1, score3_2, score3_3]]
    In this above example score1_1 is player1's score for round 1. Score3_1 is player 3's score for round 1. Score 2_3 is player 2's score for round3 
    Hence each list element in game will represent a player
    Each score (int) element in the nested list element will represent a round for that player
    Finally return a gameset list which has the game list, players list, and number of rounds
    return: list:gameset (Eg gameset returned will be a list [game, players, roundcount]. In the gameset list game is lit, players is list and roundcount is integer)
    """ 

    players = getplayers() # Calling getplayers and getting player list 
    roundcount = getrounds() # Calling getrounds and getting roundcount 
    # Implement your function here
    game = [] # Create a 'game' list to store scores for each player in each round.
    for i in range(len(players)):
        # Initialize a list of zeros for each player to track their scores over 'roundcount' rounds.
        player_scores = [0] * roundcount
        game.append(player_scores)
    gameset = [game, players, roundcount] # Create a 'gameset' that bundles the game state, player list, and the total round count.

    return gameset # Return the 'gameset' to the calling code.

# 1 Marks 
def asktoroll(player):
    """
    function: This function takes player name and asks player to hit enter to roll the dice. 
    When user hit enter calls the rolldice function and returns a score 
    :param string:player (player input is string called player name)
    :return int:score (Returns score from roll dice)
    """
    # Implement your function here 
    # Prompt the 'player' to hit Enter when they are ready to roll their dice.
    input(f"{player}! Hit enter once you are ready to roll your dices!")
    score = rolldice() # Roll the dice and store the result in the 'score' variable by calling the 'rolldice' function.

    return score # Return the 'score' from this function.
# 2 Marks 
def findwinner(game, players):
    """
    function: This function takes game list (2D list) and the player list as input parameters. Goes through the game and find the player that has the highest score
    Return the winning player name as string. If more than one player winning (eg: same score) return a winner string with all players comma seperated (Eg: John, Kate)
    :param list:game (Game list)
    :param list:players (Players list)
    :return string:winner (Winning players name as string)
    """ 
    # Implement your function here 
    # Initialize variables to track the highest score and the winning players
    highest_score = 0
    winning_players = []
    # Loop through the list of players to calculate and compare their scores.
    for i in range(len(players)):
        # Calculate the sum of the scores for the current player.
        players_score = sum(game[i])
        if players_score > highest_score: # Check if the player's score is higher than the current highest score.
            highest_score = players_score  # If so, update the highest score and reset the winning players list with the current player's name.
            winning_players = [players[i]]
        elif players_score == highest_score: # If the player's score matches the highest score, add their name to the winning players list.
            winning_players.append(players[i])
    if len(winning_players) == 1: # Check if there is only one winning player with the highest score.
        return winning_players[0]
    else:
        return ",".join(winning_players) # If there are multiple winning players, join their names with commas and return them.
# 5 Marks 
def rungame():
    
    """
    function: This function runs the game 
    It sets the game first using setgame() function. It gets the game, players and roundcount from setgame
    It prints the header and Round 1 begining score card first with inital scores set to 0
    It then asks use to roll dices using asktoroll function for all rounds and players 
    When the game finish it prompts for continuation and if chose to continue run the game again otherwise terminate.
    """
    
    
    
    # The next 5 lines are to get you started 
    # Implement the rest of the code    
    gameset = setgame()  # Calling the setgame to get game info
    game = gameset[0]  # Getting game list
    players = gameset[1]  # Getting player list
    roundcount = gameset[2]  # Getting round count
    # Loop through the rounds based on the 'roundcount'.
    for round_number in range(roundcount):
        if round_number==0: # If it's the first round, print the initial game state.
            printgame(game, players, 0, roundcount)
    
        for i in range(len(players)): # Iterate through the list of players to ask each player to roll the dice.
            player = players[i]
            game[i][round_number] = asktoroll(player)
        printgame(game, players, round_number+1, roundcount)  # Calling printgame to print the scorecard.

            

    winner = findwinner(game, players) # Determine the winner of the game by calling the 'findwinner' function
    print(f"Congratulations {winner}! You are our WINNER!")

    # Reset game scores for a new game
    for i in range(len(players)):
        
        for j in range(roundcount):
            game[i][j] = 0

    user_choice = input("Would you like to play another game?\n[1] Yes\n[2] No\nYour choice: ")
    user_choice = int(user_choice)
    if user_choice==1: # If the user chooses to play another game, call the 'rungame' function.
        rungame()
    elif user_choice == 2: # If the user chooses not to play another game, display a farewell message and exit the program.
        print("Thank you and see you later!")
        sys.exit()
        



# 5 Marks
def printgame(game, players, round_number, roundcount):
    
    """
    This function takes in game list, players list, round number (aka which round is active), totalround count as input parameters
    The function prints left aligned pretty table of the game with Rounds in columns and players in rows 
    Sample Output:
    ****************** End of Round 3 ******************
            Round 1   Round 2   Round 3   Total     
    Appla     8         7         4         19        
    Applb     11        5         8         24        
    Applc     9         3         5         17        
    Appld     8         8         7         23        
    ****************************************************
    The Stars and the Round title (End of Round) are calculated and aligned as number of rounds changes. 
    This function does not return anything
    """
    # Determine the title for the round based on the round number.
    if round_number==0:
        round_title="Round 1"
    elif round_number!=0:
        round_title=f"End of Round {round_number}"
    print('*'*20, round_title, '*'*18) # Print a decorative header with the round title.
    print("{:<10}".format("Round"), end=" ") # Print the column headers, including "Round" and each round number.
    for i in range(1, roundcount + 1):
        print(f"Round {i}", end="   ")
    print("Total")
    # Depending on the round number, display player scores or zeros for the first round.
    if round_number==0:
        for player in players:
            print("{:<10}".format(player), end=" ")
            for _ in range(roundcount):
                print("{:<10}".format("0"), end=" ")
            print("{:<10}".format("0"))  # For the first round total score is zero.
    else:
        for i, player in enumerate(players):
            print("{:<10}".format(player), end=" ")
            for j in range(roundcount):
                print("{:<10}".format(game[i][j]), end=" ")
            total_score = sum(game[i][:round_number])  # Calculating the total score till the current round
            print("{:<10}".format(total_score))  # Aligning the total score under the "Total" column
    print('*' * (14 + 10 * (roundcount + 1)))
    

def game():
    rungame() #Calling the rungame()

if __name__ == "__main__":
    game() #calling the game()