class Person:
    def __init__(self, name , occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"My name is {self.name}, and I am a {self.occ}")

a = Person("Ankur Singh", "Web Developer")
a.info()