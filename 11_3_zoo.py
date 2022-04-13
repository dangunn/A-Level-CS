animals = []

def read_data():
    f = open("11_zoo_db.csv", "r")
    eof = False

    word = ""
    row = []
    while(not eof):
        data = f.read(1)
        if data == "":
            eof = True
        elif data == ",":
            row.append(word)
            word = ""
        elif data == "\n":
            row.append(word)
            animals.append(row)
            row = []
            word = ""
        else:
            word = word + data
    f.close()

def choose_animal():
    print("Animals:")
    for i in range(len(animals)):
        print(i," --- ",animals[i][0])
    a = int(input("Which animal do you want to choose?"))
    return a

def choose_name(animal):
    print("what", animal, "name do you want to know?")
    print("1 - Child")
    print("2 - Female")
    print("3 - Male")
    n = int(input("Choice:"))
    return n

read_data()
a = choose_animal()
n = choose_name(animals[a][0])
print("the name is",animals[a][n])


