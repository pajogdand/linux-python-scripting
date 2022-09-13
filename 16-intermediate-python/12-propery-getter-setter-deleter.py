# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self,name):
#         self.name = name
#
#     def det_name(self):
#         print('deleting name')
#         self.name =  None

class Person:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        print("getter")
        return self._name

    @name.setter
    def name(self,in_name):
        print("in setter")
        self._name = in_name

    @name.deleter
    def name(self):
        print('deleter')
        self.name =  None

def main():
    p = Person("Pravin")
    p.name = "Anshul"
    print(p.name)
    del p.name

if __name__ == "__main__":
    main()