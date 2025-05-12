#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed="Beagle"):
        if name is not None:
            if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
                print("Name must be string between 1 and 25 characters.")
            else:
                self.name = name
                if breed not in APPROVED_BREEDS:
                    print("Breed must be in list of approved breeds.")
                else:
                    self.breed = breed
        else:
            if breed not in APPROVED_BREEDS:
                print("Breed must be in list of approved breeds.")
            else:
                self.breed = breed
    
    def bark(self):
        print("Woof!")
    
    def sit(self):
        print("The dog is sitting.")