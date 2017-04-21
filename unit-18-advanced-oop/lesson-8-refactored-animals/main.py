class Animal(object):
    def talk(self):
        pass


class Cat(Animal):
    def __init__(self, what_i_say_when_talk):
        self.what_i_say_when_talk = what_i_say_when_talk
