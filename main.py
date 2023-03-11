def speed_check(speed, raining):
    speed = int(speed)
    if raining.lower() == "y" and speed > 75:
        return "Issue fine"
    elif raining.lower() =="n" and speed > 100:
        return "Issue fine"
    else:
        return "Safe driving"

speed = input("Enter the speed (km/h) ")
raining = input("Raining Y/N ")
result = speed_check(speed, raining)
print(result)


	
