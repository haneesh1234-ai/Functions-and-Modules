valid = False
while not valid :
    try:
        n = int(input("enter any munber : "))
        while n % 2 == 0:

            print("bye")
            valid = True
    except ValueError :
        print("invalid")