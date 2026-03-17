time = int(input("enter the time"))

if time < 12:
   print("good morning")

elif time < 18:
    print("good afternoon")

else:
     print("good evening")

student = int(input("enter the marks"))

if student >= 90:
   print("grade A")

elif student >= 70 and student < 90:
    print("grade B") 

    if student >= 50 and student < 70:
        print("grade C")

    elif student >= 33 and student < 50:
        print("grade D")
else:
    print("grade F")  

        