import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow", 12)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


# print(primrose.get_petals())
# error because get_petals is only defined in the subclass and the superclass doesn't have access to that method
