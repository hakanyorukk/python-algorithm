import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    @abstractmethod
    def decide(self, current_score):
        pass

class HumanPlayer(Player):

    def decide(self, current_score):
        while True:
            decision = input("Roll again (r) or hold (h): ").lower()

            if decision in ("r", "h"):
                return decision

            print("Invalid input. Enter 'r' or 'h'.")

class BotPlayer(Player):
    def __init__(self, name, hold_at=20):
        super().__init__(name)
        self.hold_at=hold_at

    def decide(self,current_score,):
        return "h" if current_score>=self.hold_at else "r"

class Game:

    def __init__(self, players, target=100):
        self.players = players
        self.target = target
        self.current = 0

    def play_turn(self, player):
        turn_score = 0
        while True:
            die = random.randint(1, 6)

            if die == 1:
                print("Rolled 1 - Bust!")
                return 0

            turn_score+=die
            print(f"Rolled {die}, turn score: {turn_score}")

            decision = player.decide(turn_score)

            if decision == "h":
                return turn_score

    def play(self):

        while True:
            player = self.players[self.current]
            print(f"\n---{player.name} turns ---")
            player.total_score += self.play_turn(player)
            print(f"{player.name}, score = {player.total_score}")

            if player.total_score >= self.target:
                print(f"{player.name} won!")
                break
            self.current = 1 - self.current



def main():

    mode = input("Play against another player(p) or bot(b)")
    if mode == "b":
        players = [HumanPlayer("You"), BotPlayer("Bot")]
    else:
        players = [HumanPlayer("Player 1"), HumanPlayer("Player 2")]
    game = Game(players)
    game.play()

if __name__ == "__main__":
    main()