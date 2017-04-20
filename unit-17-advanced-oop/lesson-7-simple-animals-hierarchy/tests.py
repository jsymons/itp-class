import unittest


class AnimalTestCase(unittest.TestCase):
    def test_animal_talk(self):
        cat = Cat()
        dog = Dog()
        human = Human()

        self.assertTrue(isinstance(cat, Animal))
        self.assertTrue(isinstance(dog, Animal))
        self.assertTrue(isinstance(human, Animal))

        self.assertEqual(cat.talk(), 'Meow!')
        self.assertEqual(dog.talk(), 'Ruff!')
        self.assertEqual(human.talk(), 'Hello!')
