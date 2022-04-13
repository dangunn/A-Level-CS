import struct

# name, subject, number of classes, fulltime/partime
format = "15s20si?" # string of 15 chars, string of 20 chars, int, bool

t1 = struct.pack(format,
                 "Mr. Gunn".encode("ascii"),
                 "Computer Science".encode("ascii"),
                 20,
                 True)
t2 = struct.pack(format,
                 "Mrs. Cecilia".encode("ascii"),
                 "IT".encode("ascii"),
                 24,
                 True)

f = open("20_teachers.bin", "wb")
f.write(t1)
f.write(t2)
f.close()



