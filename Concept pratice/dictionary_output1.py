digit_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
while True:
    input_number = input("Enter a number: ")
    result = " ".join(digit_dict[digit] for digit in input_number)
    print(result)