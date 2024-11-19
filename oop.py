class DummyClass:
    dummy_variable = "I am dumb"

    def dummy_function(self):
        print("hh")
        print(self.dummy_variable)

#dummy_object = DummyClass()
#dummy_object.dummy_variable

class Person:
    species = "Homo sapiens sapiens"
    def __init__(self,name):
        self.name = name

class SuperHero(Person):
    def __init__(self,name,superpower):
        self.superpower = superpower
        super().__init__(name) #vracia nadradenu triedu a definuje ake atributy sa dedia z init funkcie