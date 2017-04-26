class Animal(object):
    def __init__(self, what_i_say_when_talk):
        self.what_i_say_when_talk = what_i_say_when_talk

    def talk(self):
        return self.what_i_say_when_talk


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Human(Animal):
    pass
