a=[6,3,0,5,1,2,5,-1,4]
n=int(input("enter the number:"))

found = -1

for i in range(0,len(a)):
    if a[i] == n:
        found = i
        print("Found at", found)

if found == -1:
    print("Not found")