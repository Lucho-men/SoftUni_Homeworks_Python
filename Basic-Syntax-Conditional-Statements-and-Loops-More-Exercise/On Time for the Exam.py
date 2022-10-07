hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())


if (hour_of_exam * 60 + minutes_of_exam) >= (hour_of_arrival * 60 + minutes_of_arrival):
    if (hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival) > 30:
        print("Early")
        if ((hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival)) < 60:
            print(f"{((hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival))} minutes before the start")
        else:
            if ((hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival)) % 60 < 10:
                print(f"{((hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival))//60}:0{((hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival)) % 60} hours before the start")
            else: print(f"{((hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival))//60}:{((hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival)) % 60} hours before the start")

    elif 0 <= (hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival) <= 30:
        print("On time")

        if (hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival) > 0:
            print(f"{((hour_of_exam * 60 + minutes_of_exam) - (hour_of_arrival * 60 + minutes_of_arrival)) % 60} minutes before the start")

else:
    print("Late")
    hours = 0
    minutes = 0
    if ((hour_of_arrival * 60 + minutes_of_arrival) - (hour_of_exam * 60 + minutes_of_exam)) < 60:
            print(f"{((hour_of_arrival * 60 + minutes_of_arrival) - (hour_of_exam * 60 + minutes_of_exam))} minutes after the start")
    else:
        if ((hour_of_arrival * 60 + minutes_of_arrival) - (hour_of_exam * 60 + minutes_of_exam)) % 60 < 10:
            print(f"{((hour_of_arrival * 60 + minutes_of_arrival) - (hour_of_exam * 60 + minutes_of_exam))//60}:0{((hour_of_arrival * 60 + minutes_of_arrival) - (hour_of_exam * 60 + minutes_of_exam))%60} hours after the start")
        else:
            print(
                f"{((hour_of_arrival * 60 + minutes_of_arrival) - (hour_of_exam * 60 + minutes_of_exam)) // 60}:{((hour_of_arrival * 60 + minutes_of_arrival) - (hour_of_exam * 60 + minutes_of_exam)) % 60} hours after the start")