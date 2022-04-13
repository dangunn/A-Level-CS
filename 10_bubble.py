a = [5, 3, 7, 2, 1, 8, 4, 6]
# hello
p = 0
swapped = True
while (p < len(a) and swapped):
    swapped = False
    for i in range(0, len(a)-1-p):
        if a[i] > a[i+1]:
            temp = a[i+1]
            a[i+1] = a[i]
            a[i] = temp
            swapped = True
    p = p + 1
print(a)