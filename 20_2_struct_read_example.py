import struct

format = "15s20si?" # NAME, subject, num classes, fulltime

size = struct.calcsize(format)

f = open("20_teachers.bin", "rb")
d = f.read(size)
d = f.read(size)
td = struct.unpack(format,d)
l = list(td)
print(l[0].decode('ascii').replace('\0',''))
print(l[1].decode('ascii').replace('\0',''))
print(l[3])
f.close()

