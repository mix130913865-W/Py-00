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
    input1 = input("num:")
    out_put = ""
    for n in input1:
        out_put += digit_dict[n] + " "
    print(out_put)