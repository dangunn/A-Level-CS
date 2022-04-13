import pickle

f = open("20_teachers2.bin", 'rb')
db = pickle.load(f)
print(db[0]['subject'])
f.close()