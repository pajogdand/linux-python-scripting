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

    # #With the help of class method we can declare initt
    # # variables of the class method
    # @classmethod
    # def from_dash(cls,string):
    #     params= string.split("-")
    #     return cls(params[0] ,params[1] , params[2])

    #With the help of class method we can declare initt
    # variables of the class method
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

pravin = Employee("Pravin" , 25000.0, "Software Engineer")
kiran = Employee("Kiran" ,10000.0 , "Admin")

arvind = Employee.from_dash("arvind-10000-teacher")
print(arvind.print_details())