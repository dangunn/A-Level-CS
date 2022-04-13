f1 = open("20_file1.txt", "r")
f2 = open("20_file2.txt", 'w')
lines = f1.readlines()
for line in lines:
    f2.write(line)
f1.close()
f2.close()