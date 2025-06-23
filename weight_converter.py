while True:
    try:
        Weight = int(input("weight: "))
        if Weight < 0:
            print("Weight must be a positive number.")    
    except ValueError:
        print("Invalid input. Please enter a valid number for weight.")
        continue
    while True:
            Options = input("Lbs or Kg: ")
            if Options.lower() == "l":
                print("Weight in Kg:", Weight * 0.453592)
            elif Options.lower() == "k":
                print("Weight in Lbs:", Weight * 2.20462)
            else:
                print("Invalid option. Please enter 'L' for pounds or 'K' for kilograms.")
                continue