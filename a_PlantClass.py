class Plant:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class Flower(
    Plant
):  # flower is a specialized version from a plant #inheriting attributes from the plant class
    # can't create a subclass without first creating the superclass #can't create flower without creating plant first
    def __init__(self, color, petals):
        Plant.__init__(self, color)

        self.__petals = petals  # petals belongs only to the flower subclass

    def get_petals(self):  # method only available to the flower
        return self.__petals
