# list comprehension
xyz = [i  for i in range(5)]
print(xyz)

# Generator (this is faster since no need to create memory)
abc = (i for i in range(5))
print(abc)

# Example of list comprehension Vs generator

# Generator
A = [1,2,3,45,7,65]
def is_div_by_5(num):
    if num%5 == 0:
        return  True
    else:
        return  False
out = (i for i in A if is_div_by_5(i))

# for i in out:
#     print(i)
# OR
[print(i) for i in out]

# list comprehension
out_list_comp = [i for i in A if is_div_by_5(i)]
print(out_list_comp)
[print(i) for i in out_list_comp]

# complex list comprehension

# for i in range(5):
#     for ii in range(5):
#         print(i,ii)

[[print(i,ii) for ii in range(5)]    for i in range(5)]
    