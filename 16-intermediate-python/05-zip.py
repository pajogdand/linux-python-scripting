x = [1 ,2, 3, 4]
y = [10 ,20, 30, 40]
z = ["first" , "second" , "third" , "forth"]


for i,j,k in zip(x,y,z):
    print(i,j,k)

for d in zip(x,y,z):
    print(d)

yz_dict = dict(zip(y,z))
print(yz_dict)

out = [(i,j,k) for i,j,k in zip(x,y,z)]
print(out)

out = ((i,j,k) for i,j,k in zip(x,y,z))
for i in out:
    print(i)

