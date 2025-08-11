import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("Welcome!")

    while True:
        roll = input(
            "Press Enter to roll or type 'q' to quit: ").strip().lower()

        if roll == "q":
            print("End")
            break

        result = roll_dice()
        print(f"You rolled a {result}!\n")


if __name__ == "__main__":
    main()
