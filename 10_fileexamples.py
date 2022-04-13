f = open("10_somefile.txt", "w")
f.write("hello everyone")
f.write("\nMy name is Mr. Gunn")
f.close()

f2 = open("10_somefile.txt", "r")
lines = f2.readlines()
for line in lines:
    print(line, end="")
f2.close()

f3 = open("10_somefile.txt", "a")
f3.write("\nAnother line")
f3.close()