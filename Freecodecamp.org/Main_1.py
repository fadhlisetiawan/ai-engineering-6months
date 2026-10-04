#Build a Travel Weather Planner
#https://www.freecodecamp.org/learn/python-v9/lab-travel-weather-planner/build-a-travel-weather-planner

#Variable Global
#ganti nilai variable dibawah untuk check hasil run
distance_mi = 5
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False

#cara panjang

def cara_panjang():
    print('---Hasil Cara Panjang---')

    if not distance_mi:
        print(False)

    elif distance_mi <= 1 and not is_raining:
        print(True)

    elif distance_mi <= 1 and is_raining:
        print(False)

    elif 1 < distance_mi <= 6 and is_raining and not has_bike:
        print(False)

    elif 1 < distance_mi <= 6 and not is_raining and not has_bike:
        print(False)

    elif 1 < distance_mi <= 6 and has_bike and not is_raining:
        print(True)

    elif distance_mi > 6 and has_ride_share_app:
        print(True)

    elif distance_mi > 6 and has_car:
        print(True)

    elif distance_mi > 6 and not has_car and not has_ride_share_app:
        print(False)




#cara singkat

def cara_singkat():
    print("--- Hasil Cara Singkat ---")

    if not distance_mi:
        print(False)
    elif distance_mi <= 1:
        print(not is_raining)
    elif distance_mi <= 6:
        print(has_bike and not is_raining)
    else:
        print(has_car or has_ride_share_app)


cara_panjang()
cara_singkat()