# This program demonstrates polymorphism.

import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog() # we already hardcoded the word dog in the class so no argument
    cat = animals.Cat()


    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    mammal.show_species()
    mammal.make_sound() # generic sound

    print()

    dog.show_species()
    dog.make_sound() # switches to woof # know to use the method from subclass

    print()

    cat.show_species()
    cat.make_sound()

# Call the main function.
main()
