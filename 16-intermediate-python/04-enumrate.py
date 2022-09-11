names = ["pravin" , "achyutrao" , "jogdand"]

for i in range(len(names)):
    print(i, names[i])

for i,j in enumerate(names):
    print(i,j)

names_dict = dict(enumerate(names))
print(names_dict)

[print(i,j) for i,j in enumerate(names_dict)]

