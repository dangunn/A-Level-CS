try:
    f = open("20_fileexception.txt", "r")
    d = int(f.readline())
    print(d+1)
except FileNotFoundError:
    f = open("20_fileexception.txt", "w")
    f.write("5")
finally:
    f.close()
    print("file closed")