import random

def main():
    totals = [0,0]
    current = 0
    mode = input("Play against bot (b) or two players (h)? ")
    while True:
        print(f"\n--- Player {current}'s turn ---")
        is_bot = (mode == "b" and current == 1)
        totals[current] += play_turn(is_bot)
        print(f"Player {current} total: {totals[current]}")
        if totals[current] >= 100:
            winner = "Bot" if is_bot else "Player"
            print(f"{winner} {current} won!")
            break
        current = 1-current

def play_turn(is_bot):
    turn_score = 0
    while True:
        die = roll_die()
        if die == 1:
            print("Rolled 1 Bust!")
            return 0
        turn_score += die
        print(f"Rolled {die}, turn score: {turn_score}")

        if is_bot:
            choice = bot_decision(turn_score)
            print(f"Bot {'holds' if choice == 'h' else 'rolls again'}")
        else:
            choice = input("roll again? (r/h)")

        if choice == "h":
            return turn_score

def roll_die():
    return random.randint(1,6)

def bot_decision(turn_score):
    return "h" if turn_score >= 20 else "r"
if __name__ == "__main__":
    main()