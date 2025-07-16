while True:
    try:
        input1 = int(input('輸入一個數字，判斷是否為質數。'))
        if input1 < 2:
            print('非質數')
        elif input1 == 2:
            print('質數')
        else:
            for number in range(2,input1):
                if input1 % number == 0:
                    print('非質數')
                    break
            else:
                print('質數')
    except ValueError:
        print("Invalid input. Please enter a valid number.")