import pickle

class Teachers:

    def __init__(self, name, subject):
        self.__name = name
        self.__subject = subject
        self.numStudents = 0

    def introduce(self):
        print("Hello",self.__subject,"class. My name is", self.__name)

f = open("20_teachers3.bin", 'rb')
teachers = pickle.load(f)
f.close()

print(teachers[0].numStudents)