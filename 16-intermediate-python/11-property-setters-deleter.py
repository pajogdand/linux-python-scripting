class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.email = f'{self.fname}.{self.lname}@gmail.com'

    def print_email(self):
        print(f'email : {self.email}')

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return  f"email id is invalid"
        return f'{self.fname}.{self.lname}@gamil.com'

    @email.setter
    def email(self, in_email_string):
        print('Setting now...')
        names=in_email_string.split('@')[0]
        self.fname=names.split('.')[0]
        self.lname=names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


def main():
    pj=Employee("pravin", "jogdand")
    pj.print_email()
    pj.fname = "pa"
    pj.print_email()
    pj.email = "pa.jog@gmail.com"
    pj.print_email()

    del pj.email
    pj.print_email()


if __name__ == "__main__":
    main()

