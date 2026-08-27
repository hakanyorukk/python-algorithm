import random

def main():
    totals = [0, 0]
    current = 0
    mode = input("Play against player(p) or bot(b)")

    while True:
        print(f"\n--- Player {current} rolls ---")
        is_bot = True if mode == "b" and current == 1 else False
        totals[current]+=play(is_bot)
        print(f"Player: {current}, score: {totals[current]}")

        if totals[current] >= 100:
            winner = "Bot" if is_bot else "Player"
            print(f"{winner} won!")
            break

        current = 1 - current

def play(is_bot):
    turn_score = 0

    while True:
        die = roll_dice()
        if die == 1:
            print("Rolled 1 - bust!")
            return 0
        turn_score+=die
        print(f"Rolled {die}, turn score: {turn_score}")
        if is_bot:
            decision = bot_decision(turn_score)
        else:
            decision = input("Roll(r) again or hold(h)")
        if decision == "h":
            return turn_score


def roll_dice():
    return random.randint(1,6)

def bot_decision(turn_score):
    return "h" if turn_score >= 20 else "r"

if __name__ == "__main__":
    main()