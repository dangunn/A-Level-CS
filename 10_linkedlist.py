class LinkedList:

    def __init__(self):
        self.nextP = [0]*10
        self.values = [0]*10
        self.startP = -1
        self.freeP = 0

        for i in range(10):
            self.nextP[i] = i+1

        self.nextP[9] = -1

    def append(self, newValue):
        if self.startP == -1: # first time
            self.startP = self.freeP
            self.values[self.startP] = newValue
            self.freeP = self.nextP[self.freeP]
            self.nextP[self.startP] = -1
        elif self.freeP == -1: # full
            print("Error, cannot insert value", newValue,". Its full!")
            return
        else: # normal
            endP = self.startP
            while self.nextP[endP] != -1:
                endP = self.nextP[endP]

            # put our new value here (end of list)
            self.nextP[endP] = self.freeP
            self.values[self.freeP] = newValue

            #update the free list
            self.freeP = self.nextP[self.freeP]

            # next one of the end is now NULL
            self.nextP[self.nextP[endP]] = -1

l = LinkedList()
for i in range(0,12):
    l.append(i*2)
print(l.nextP)
print(l.values)
print("free:", l.freeP, "start:", l.startP)