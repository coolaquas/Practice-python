try:

    number = int(input("enter a number : "))
    test = 10/0
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
