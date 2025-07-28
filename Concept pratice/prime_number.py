while True:
    try:
        input1 = int(input('Check if a number is a prime number: '))
        if input1 < 2:
            print('Not prime')
        elif input1 == 2:
            print('prime')
        else:
            for number in range(2,input1):
                if input1 % number == 0:
                    print('Not prime')
                    break
            else:
                print('prime')
    except ValueError:
        print("Invalid input. Please enter a valid number.")