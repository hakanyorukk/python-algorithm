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

    def decide(self,turn_score):
        while True:
            decision = input(f"Current score: {turn_score} hold(h) or roll again(r)").strip().lower()
            if decision in ("h", "r"):

                return decision
            print("Invalid input. Please enter 'h' or 'r'.")

class BotPlayer(Player):

    def __init__(self,name):
        super().__init__(name)
        self.total=0

    def decide(self, turn_score, hold_at=20):
        decision = "h" if turn_score >=hold_at else "r"
        print(f"{self.name} {decision} turn score: {turn_score}")
        return decision

class Game:
    def __init__(self, players, target=100):
        self.players=players
        self.target=target
        self.current=0

    def play_turn(self, player):
        turn_score = 0

        while True:
            die = random.randint(1,6)

            if die == 1:
                print("Rolled - 1")
                return 0
            turn_score+=die
            print(f"Rolled {die}, turn score: {turn_score}")

            if player.decide(turn_score) == "h":
                return turn_score

    def play(self):
        while True:
            player = self.players[self.current]
            print(f"\n--- {player.name} turn ---")
            player.total += self.play_turn(player)
            print(f"{player.name} total score: {player.total}")

            if player.total >= 100:
                print(f"{player.name} won!")
                break
            self.current = 1-self.current

def main():
    while True:
        mode = input("Play against player(p) or bot(b)").strip().lower()
        if mode in ("p","b"):
            if mode == "b":
                game = Game([HumanPlayer("You"), BotPlayer("Bot")])
            else:
                game = Game([HumanPlayer("Player 1"), HumanPlayer("Player 2")])
            break
        print("Invalid input. Please enter 'p' or 'b'.")

    game.play()

if __name__ == "__main__":
    main()