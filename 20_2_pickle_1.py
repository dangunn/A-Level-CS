import pickle

t1 = {'name': 'Mr. Gunn',
      'subject': 'Computer Science',
      'numStudents': 20,
      'fullTime': True}

t2 = {'name': 'Mrs. Cecilia',
      'subject': 'IT',
      'numStudents': 24,
      'fullTime': True}

db = [t1, t2]

f = open("20_teachers2.bin", 'wb')
pickle.dump(db, f)
f.close()