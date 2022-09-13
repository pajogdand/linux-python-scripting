class Employee():
    no_of_leaves = 8
    def __init__(self,name="None",sal=0.0,role="Nothing"):
        self.name = name
        self.sal = sal
        self.role = role

    def print_details(self):
        print('name : {} , sal : {} , role : {}'.format(self.name, self.sal,self.role))

    #if we wish to change the variable values which belongs to class and not instnace
    # then we can create the class method and change the class variable
    @classmethod
    def change_leaves(cls, new_no_of_leaves):
        cls.no_of_leaves = new_no_of_leaves

pravin = Employee("Pravin" , 25000.0, "Software Engineer")
kiran = Employee("Kiran" ,10000.0 , "Admin")

# We can change the value class variable using instance
pravin.change_leaves(35)
print(kiran.no_of_leaves)
print(pravin.no_of_leaves)

# We can change the value class variable using class name itself
Employee.change_leaves(40)
print(kiran.no_of_leaves)
print(pravin.no_of_leaves)