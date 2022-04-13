import pickle

class Teachers:

    def __init__(self, name, subject):
        self.__name = name
        self.__subject = subject
        self.numStudents = 0

    def introduce(self):
        print("Hello",self.__subject,"class. My name is", self.__name)

t1 = Teachers("Mr. Gunn","Computer Science")
t1.numStudents = 10
t1.numStudents = 20
t2 = Teachers("Mrs. Cecilia", "IT")
t2.numStudents = 40

allTeachers = [t1, t2]

f = open("20_teachers3.bin", "wb")
pickle.dump(allTeachers,f)
f.close()
