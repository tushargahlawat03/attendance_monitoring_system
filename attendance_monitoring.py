present = 0
late = 0
short_day = 0
half_day = 0
absent = 0
for i in range(1, 3):
    print(" person", i)
  
   

    for j in range(1, 8):
        print("day", j)
        a = int(input("enter in time: "))
        b = int(input("enter out time: "))

        if a <= 8 and b >= 17:
            print("present")
            present += 1

        elif a <= 10 and b >= 17  :
            print("late")
            late += 1

        elif a >=8 and b <=12 or a <= 9 and b <= 13:
            print("short day")
            short_day += 1


        elif a <= 8 and b <= 14 or a >= 11 and b <= 18 or a <= 10 or b <= 15:
            print("half day")
            half_day += 1

        else:
            print("absent")
            absent += 1

print("\nPerson", i)
print("present:", present)
print("late:", late)
print("half day:", half_day)
print("short_day:",short_day)
print("absent:", absent)
