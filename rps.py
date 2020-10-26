#!/usr/bin/env python3
import random


moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):
        self.score = 0

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


# RandomPlayer class chooses their move randomly by overriding the move method.
class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


# HumanPlayer class allows the user to enter their move.
class HumanPlayer(Player):

    def move(self):
        m = input("Rock, paper, scissors? > ").strip().lower()

        if m in moves:
            return m
        else:
            self.move()


# ReflectPlayer plays their opponents last move from the previous round,
# but starts off by choosing the first move randmonly.
class ReflectPlayer(Player):

    def __init__(self):
        super().__init__()
        self.last_move = random.choice(moves)

    def move(self):
        return self.last_move

    def learn(self, my_move, their_move):
        self.last_move = their_move


# CyclePlayer cycles through the valid moves based on their last move.
class CyclePlayer(Player):

    def __init__(self):
        super().__init__()
        self.next_move = "rock"

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):

        if my_move == "rock":
            self.next_move = "paper"
        elif my_move == "paper":
            self.next_move = "scissors"
        elif my_move == "scissors":
            self.next_move = "rock"


# Determines who won the round.
def beats(one, two):
    if one == 'rock' and two == 'scissors':
        print("\n>>> Rock SMASHES Scissors <<<\n")
    elif one == 'scissors' and two == 'paper':
        print("\n>>> Scissors CUT paper <<<\n")
    else:
        print("\n>>> Paper COVERS Rock <<<\n")

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Game class plays the game.
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # Prompt the user to play again.
    def play_again(self):
        again = input("\nDo you want to play again? (Y or N) > ")

        if again.strip().lower() in ["y", "n"]:
            return again.strip().lower() == "y"

    # Prompt the user how many rounds they want to play.
    def how_many_rounds(self):
        rounds = input("How many rounds do you want to play? (1, 3 or 5) > ")

        if rounds in ["1", "3", "5"]:
            return rounds
        else:
            self.how_many_rounds()

    # Plays the round and declars a winner (or a tie).
    def play_round(self):
        move1 = self.p1.move()
        print(f"You played {move1}.")

        move2 = self.p2.move()
        print(f"Your oppenent played {move2}.")

        if move1 != move2:
            if beats(move1, move2):
                self.p1.score += 1
                print("** PLAYER ONE WINS THE ROUND **")
            else:
                self.p2.score += 1
                print("** PLAYER TWO WINS THE ROUND **")
        else:
            print("** TIE **")

        print(f"Score: Player One {self.p1.score}, Player Two {self.p2.score}")

        # Set the next move for either the Reflect or Cycle player classes.
        self.p2.learn(move2, move1)

    # Plays the game based on the number of rounds the player enters.
    def play_game(self):
        print("Rock Paper Scissors, Go!")

        # Play 1, 3 or 5 rounds.
        for round in range(int(self.how_many_rounds())):
            print(f"\nRound {round + 1} --")
            self.play_round()

        # Display the final score and who the winner was.
        print(f"\nFinal Score: Player One {self.p1.score}, " +
              f"Player Two: {self.p2.score}")

        if self.p1.score > self.p2.score:
            print("-- PLAYER ONE WINS THE GAME! --")
        elif self.p2.score > self.p1.score:
            print("-- PLAYER TWO WINS THE GAME! --")
        else:
            print("-- TIE GAME --")

        # Ask the user if they want to play agin.
        if self.play_again():
            start_game()
        else:
            print("\nGame over")


# Starts the game by determining if they playing Random, Reflect or Cycle
# player.
def start_game():

    who_to_play = random.choice(range(3))

    # Random player
    if who_to_play == 0:
        game = Game(HumanPlayer(), RandomPlayer())
    # Reflect player
    elif who_to_play == 1:
        game = Game(HumanPlayer(), ReflectPlayer())
    # Cycle player
    else:
        game = Game(HumanPlayer(), CyclePlayer())

    game.play_game()


if __name__ == '__main__':

    start_game()
