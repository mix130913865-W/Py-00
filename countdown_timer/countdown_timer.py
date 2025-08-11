import time


def countdown(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")


def main():
    try:
        user_input = int(input("Enter countdown time in seconds: "))
        countdown(user_input)
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
