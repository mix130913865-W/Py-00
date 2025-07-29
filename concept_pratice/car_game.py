moving = False
while True:
    car_status = input("Enter the car status (moving/stopped): ").lower()
    if car_status == "moving":
        if moving:
            print("The car is already in motion.")
        else:
            moving = True
            print("The car is in motion.")
    elif car_status == "stopped":
        if moving:
            moving = False
            print("The car has stopped.")
        else:
            print("The car is already stopped.")
    else:
        print("Invalid status.")