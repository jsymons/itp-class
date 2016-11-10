# Refactored Animals

Expand the previous assignment so the classes `Cat`, `Dog` and `Human` receive a parameter when created `what_i_say_when_talk` (and store it as an attribute). The `talk` method should be now in the `Animal` class. The `talk` method should use the `what_i_say_when_talk` attribute . Example:

```python
cat = Cat('Meow!')
dog = Dog('Ruff!')
human1 = Human('Hello!')
human2 = Human('World!')

cat.talk()     # 'Meow!'
dog.talk()     # 'Ruff!'
human1.talk()  # 'Hello!'
human2.talk()  # 'World!'
```
