import sys
import os 
import random

"""
Firstname: Aakib Kibria 
Lastname: Khan
Username: akkhan9
StudentID: 157802224
Email: akkhan9@myseneca.ca
"""

# This is my TicTacToe Class 
class TicTacToe:
    # Declare class variables 
    # players is a list of players (this game will have 2 players)
    # Winninggames is a list of all winning possibilities 
    # Player1entry is a list of entries of first players 
    # Player2 entry is a list of entries of second player 
    players = []
    winninggames = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    player1entry = []
    player2entry = []
    board = [1,2,3,4,5,6,7,8,9] #Based on infromation given in the Final Exam Problem Statement


    # This is a constructor 
    """
    This is a constructor that prints an initialization statement
    Then call the getplayernames method to get the names and configure the list of players 
    Also call the printboard method to print the board, since this is a constructor the printboard is called first time here 
    Therefore printboard in this constructor will print initial brand new board ready to be played.
    """
    def __init__(self) -> None:
        print("Initializing a 3X3 TicTacToe") # Printing initializing a 3x3 TicTacToe game
        self.getplayernames() # Get player names by calling the getplayernames method
        self.printboard() # Print the initial game board by calling the printboard method

        
    """
    This is getplayernames method 
    This method asks user to enter the name of the player 1 and 2 one by one and append the names to the players class variable
    """
    def getplayernames(self): 
        player1 = input("What is the name of the player 1: ") # Printing message for user name input for Player 1 
        player2 = input("What is the name of the player 2: ") # Printing message for user name input for Player 2 
        self.players = {player1: 'X', player2: 'O'} # Assigning the symbol for player 1 and 2
        
    """
    This is a printboard method 
    This method prints current state of the board 
    """
    def printboard(self):
        for i in range(0, 9, 3): 
            print(f"|{self.board[i]}|{self.board[i + 1]}|{self.board[i + 2]}|") # Prints the current state of the TicTacToe board
        print(end='')    # No new line after printing the board for a cleaner display
    
        
    
    """
    This method gets all available numbers to be played at the time this method is called 
    It returns these available numbers 
    :return availablenumbers 
    """
    def getavailablenumbers(self):
        return [num for num in self.board if isinstance(num, int)]  # Returns a list of available numbers on the TicTacToe board that can be played
    
        
    
    """
    This function goes through all the winning games and compare them against the each individual players entries
    By comparing the entries against winning game this method identifies the winner if there is one 
    If there is a winner this method returns the winner otherwise return None
    """
    def getwinner(self):
        for player, symbol in self.players.items():
            checking_entry = [i for i, x in enumerate(self.board) if x == symbol] # Get the positions where the current player has marked on the board
            checking_entry.sort() # Sorts the list of positions where the current player has marked on the board for consistent comparison

            for win in self.winninggames:
                win.sort()  # Sort the winning combinations for comparison

                if all(entry in checking_entry for entry in win): # Check if the player's marked positions match any winning combination
                    return player



    """
    This is rungame method 
    This method continue to run a loop asking the user to enter the number to play and shows the available numbers as well
    If the user enter something otherthan the available number the prompt will continue to ask the same user to enter the correct values 
    This method assembles all the relevant method we have together, so that 
    First player one is asked to enter the number and then the second and then the first and it keep alternates 
    Until one player wins or the game finishes where there is no further numbers to enter. 
    Ultimately, if there is a winner it prints the winner. If ther eis no winner it prints No Winner. 
    """
    def rungame(self):
        current_player = 0 # Initialize the player turn, starting with player 1 (index 0)
        while True:  # Infinite loop to continue the game until a winner or no available numbers
            player_name = list(self.players.keys())[current_player]  # Get the current player's name for the turn
            player_symbol = list(self.players.values())[current_player] # Get the current player's symbol for the turn


            available_numbers = self.getavailablenumbers() # Get a list of available numbers to play on the board

            if not available_numbers: # Check if there are no available numbers left on the board
                print("No one win!\nEnd of the game",end='') # Print end-of-game message and break out of the loop
                break

            try: # Prompt the current player to enter a number to play
                player_choice = int(input(
                    f"{player_name} Enter the number to play your symbol {player_symbol} "
                    f"(Available Numbers {','.join(map(str, available_numbers))}): "))
            except ValueError: # Handle the case where the entered value is not a valid integer
                print("Enter available Number") # Print an error message and continue to the next iteration
                continue

            if player_choice not in available_numbers: # Check if the entered number is already played or invalid
                print(f"Number already played, choose a different number from available numbers. "
                    f"(Available Numbers %s) {','.join(map(str, available_numbers))}") # Print an error message
                continue

            self.board[player_choice - 1] = player_symbol # Mark the chosen position on the board with the current player's symbol

            winner = self.getwinner() # Check if the current player has won after making a move
            if winner: # If there is a winner, print the winner and end the game
                print(f"Player {winner} is the winner")
                break

            self.printboard() # Print the updated board after the current player's move

            current_player = 1 - current_player # Switch to the next player for the next turn
        
        

# My main method to test this code locally
if __name__ == "__main__":
    game = TicTacToe()
    game.rungame()