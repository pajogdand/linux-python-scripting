first_name = "pravin"
middle_name = "achyutrao"
last_name = "jogdand"

title="Mr."
def print_name_args(title,*args):
    print(title)
    for name in args:
        print(name)

print_name_args(title, first_name,middle_name,last_name)

def print_name_kargs(title,**kwargs):
    print(title)
    for which_name, name in kwargs.items():
        print(which_name, name)

print_name_kargs(title,first_name="pravin",middle_name="achyutrao" ,last_name="jogadnd")


def print_name_args_kargs(title,*args, **kwargs):
    for i in args:
        print(f'{i}')
    print(title)
    for which_name, name in kwargs.items():
        print(which_name, name)

print_name_args_kargs(title,
                      "printing" , "your" , "name",
                      first_name="pravin",middle_name="achyutrao" ,last_name="jogadnd")