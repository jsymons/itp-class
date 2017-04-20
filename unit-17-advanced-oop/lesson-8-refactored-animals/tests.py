import unittest


class AnimalTestCase(unittest.TestCase):
    def test_animal_talk(self):
        cat = Cat('Meow!')
        dog = Dog('Ruff!')
        human1 = Human('Hello!')
        human2 = Human('World!')

        self.assertTrue(isinstance(cat, Animal))
        self.assertTrue(isinstance(dog, Animal))
        self.assertTrue(isinstance(human1, Animal))
        self.assertTrue(isinstance(human2, Animal))

        self.assertEqual(cat.talk(), 'Meow!')
        self.assertEqual(dog.talk(), 'Ruff!')
        self.assertEqual(human1.talk(), 'Hello!')
        self.assertEqual(human2.talk(), 'World!')
