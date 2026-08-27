import random
from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, name):
        self.name = name
        self.total = 0
    @abstractmethod
    def decide(self, turn_score):
        pass

class HumanPlayer(Player):

    def decide(self, turn_score):
        return input("Roll again(r) or hold(h)")

class BotPlayer(Player):

    def __init__(self, name, hold_at=20):
        super().__init__(name)
        self.hold_at = hold_at


    def decide(self, turn_score):
        choice = "h" if turn_score >= self.hold_at else "r"
        print(f"{self.name} {'holds' if choice == 'h' else 'rolls again'}")
        return choice

class Game():

    def __init__(self, players, targe=100):
        self.players = players
        self.target = 100
        self.current = 0

    def play_turn(self, player):
        turn_score = 0
        while True:
            die = random.randint(1,6)

            if die == 1:
                print("Rolled 1 - Bust!")
                return 0
            turn_score+=die
            print(f"Rolled: {die}, score: {turn_score}")

            if player.decide(turn_score) == "h":
                return turn_score

    def play(self):
        while True:
            player = self.players[self.current]
            print(f"\n--- {player.name} turns ---")
            player.total += self.play_turn(player)
            print(f"{player.name} total: {player.total}")
            if player.total >= self.target:
                print(f"\n{player.name} won!")
                break
            self.current = 1 - self.current

def main():
    mode = input("Play against bot(b) or human(h)")
    if mode == "b":
        game = Game([HumanPlayer("You"), BotPlayer("Bot")])
    else:
        game = Game([HumanPlayer("Player 1"), BotPlayer("Player 2")])
    game.play()
if __name__ == "__main__":
    main()