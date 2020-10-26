#!/usr/bin/env python3
import random


moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}\nPlayer 2: {move2}")

        if move1 != move2:
            if beats(move1, move2):
                self.p1.score += 1
                print("Player 1 wins this round!")
            else:
                self.p2.score += 1
                print("Player 2 wins this round!")
        else:
            print("*** TIE ***")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"\nRound {round + 1}:")
            self.play_round()

        print(f"\nFinal score:\nPlayer 1: {self.p1.score}" +
              "\nPlayer 2: {self.p2.score}")

        if self.p1.score > self.p2.score:
            print("Player 1 wins the game!")
        elif self.p2.score > self.p1.score:
            print("Player 2 wins the game!")
        else:
            print("*** Tie game ***")

        print("\nGame over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
