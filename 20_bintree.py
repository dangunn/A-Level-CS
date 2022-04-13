class node:

    def __init__(self, value):
        """ Constructor """
        self.__leftP = None
        self.__rightP = None
        self.__data = value
    
    def insert(self, value):
        if self.__data:
            if value == self.__data:
                print("error: already exists", value)
            elif value < self.__data:
                if self.__leftP == None:
                    self.__leftP = node(value)
                else:
                    self.__leftP.insert(value)
            else:
                if self.__rightP == None:
                    self.__rightP = node(value)
                else:
                    self.__rightP.insert(value)
        else:
            print("error no value on node")

    def search(self, value):
        if self.__data:
            if value == self.__data:
                return self
            elif value < self.__data:
                if self.__leftP == None:
                    print("Error: value not found", value)
                    return None
                else:
                    return self.__leftP.search(value)
            else:
                if self.__rightP == None:
                    print("Error: value not found", value)
                else:
                    return self.__rightP.search(value)
        else:
            print("Error: empty tree")

    def printInOrder(self):
        if self.__leftP != None:
            self.__leftP.printInOrder()

        print(self.__data)

        if self.__rightP != None:
            self.__rightP.printInOrder()

    def printPreOrder(self):
        print(self.__data)

        if self.__leftP != None:
            self.__leftP.printPreOrder()

        if self.__rightP != None:
            self.__rightP.printPreOrder()

    def printPostOrder(self):
        if self.__leftP != None:
            self.__leftP.printPostOrder()

        if self.__rightP != None:
            self.__rightP.printPostOrder()

        print(self.__data)

a = node(25)
for x in [15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]:
    a.insert(x)

print("In order:")
a.printInOrder()

print("Pre Order:")
a.printPreOrder()

print("Post Order:")
a.printPostOrder()



