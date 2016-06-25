class Person(object):
    """docstring for Person"""
    def __init__(self, name, age, favorite_foods):
        self.name = name
        self.age = age
        self.favorite_foods = favorite_foods

    def __str__(self):
        return "Name: {} Age: {} Favorite food: {}".format(
            self.name, self.age, self.favorite_foods[0])

    def birth_year(self):
        return 2015 - self.age