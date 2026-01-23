while True:
    try:
        num = int(input("Enter an integer number: "))

        if num == 0:
            print("The number is Zero")
        elif num % 2 == 0:
            print("The number is Even")
        else:
            print("The number is Odd")
        break  

    except ValueError:
        pass    

