finished = False
while not finished:
    try:
        num = int(input("Give a number to inverse:"))
        print("The inverse is",1/num)
        finished = True
    except ZeroDivisionError:
        print("zero is not allowed")
    except ValueError:
        print("please use integers only")