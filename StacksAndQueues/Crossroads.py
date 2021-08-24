import sys
green_time = int(input())
extra_time = int(input())
time_available = green_time + extra_time
passed_cars = 0
data = input()
remaining_green = green_time
lights = 0

while not data == "green":
    car = data
    if remaining_green > 0:
        if len(car) < remaining_green:
            remaining_green -= len(car)
            passed_cars += 1
            data = input()
            continue
        elif len(car) == remaining_green:
            passed_cars += 1
            break
        elif len(car) > remaining_green and len(car) <= (extra_time + remaining_green):
            passed_cars += 1
            break
        else:
            print("A crash happened!")
            print(f"{car} was hit at {car[remaining_green+extra_time]}.")
            sys.exit()


    data = input()
while not data == "END":
    if data == "green":
        data = input()
        if data == "END":
            print("Everyone is safe.")
            print(f"{passed_cars} total cars passed the crossroads.")
            sys.exit()
        remaining_green = green_time
        while not data == "green":
            if data == "END":
                print("Everyone is safe.")
                print(f"{passed_cars} total cars passed the crossroads.")
                sys.exit()
            car = data
            if remaining_green > 0:
                if len(car) < remaining_green:
                    remaining_green -= len(car)
                    passed_cars += 1
                    data = input()
                    continue
                elif len(car) == remaining_green:
                    passed_cars += 1
                    data = input()
                    break
                elif len(car) > remaining_green and len(car) <= (extra_time + remaining_green):
                    passed_cars += 1
                    data = input()
                    break
                else:
                    print("A crash happened!")
                    print(f"{car} was hit at {car[remaining_green + extra_time]}.")
                    sys.exit()

            data = input()
    else:
        data = input()
print("Everyone is safe.")
print(f"{passed_cars} total cars passed the crossroads.")

