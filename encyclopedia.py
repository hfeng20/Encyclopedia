import random
import math

words = [
    "Aardvark",
    "Albatross",
    "Alligator",
    "Alpaca",
    "Ant",
    "Anteater",
    "Antelope",
    "Ape",
    "Armadillo",
    "Donkey",
    "Baboon",
    "Badger",
    "Barracuda",
    "Bat",
    "Bear",
    "Beaver",
    "Bee",
    "Bison",
    "Boar",
    "Buffalo",
    "Butterfly",
    "Camel",
    "Capybara",
    "Caribou",
    "Cassowary",
    "Cat",
    "Caterpillar",
    "Cattle",
    "Chamois",
    "Cheetah",
    "Chicken",
    "Chimpanzee",
    "Chinchilla",
    "Chough",
    "Clam",
    "Cobra",
    "Cockroach",
    "Cod",
    "Cormorant",
    "Coyote",
    "Crab",
    "Crane",
    "Crocodile",
    "Crow",
    "Curlew",
    "Deer",
    "Dinosaur",
    "Dog",
    "Dogfish",
    "Dolphin",
    "Dotterel",
    "Dove",
    "Dragonfly",
    "Duck",
    "Dugong",
    "Dunlin",
    "Eagle",
    "Echidna",
    "Eel",
    "Eland",
    "Elephant",
    "Elk",
    "Emu",
    "Falcon",
    "Ferret",
    "Finch",
    "Fish",
    "Flamingo",
    "Fly",
    "Fox",
    "Frog",
    "Gaur",
    "Gazelle",
    "Gerbil",
    "Giraffe",
    "Gnat",
    "Gnu",
    "Goat",
    "Goldfinch",
    "Goldfish",
    "Goose",
    "Gorilla",
    "Goshawk",
    "Grasshopper",
    "Grouse",
    "Guanaco",
    "Gull",
    "Hamster",
    "Hare",
    "Hawk",
    "Hedgehog",
    "Heron",
    "Herring",
    "Hippopotamus",
    "Hornet",
    "Horse",
    "Human",
    "Hummingbird",
    "Hyena",
    "Ibex",
    "Ibis",
    "Jackal",
    "Jaguar",
    "Jay",
    "Jellyfish",
    "Kangaroo",
    "Kingfisher",
    "Koala",
    "Kookabura",
    "Kouprey",
    "Kudu",
    "Lapwing",
    "Lark",
    "Lemur",
    "Leopard",
    "Lion",
    "Llama",
    "Lobster",
    "Locust",
    "Loris",
    "Louse",
    "Lyrebird",
    "Magpie",
    "Mallard",
    "Manatee",
    "Mandrill",
    "Mantis",
    "Marten",
    "Meerkat",
    "Mink",
    "Mole",
    "Mongoose",
    "Monkey",
    "Moose",
    "Mosquito",
    "Mouse",
    "Mule",
    "Narwhal",
    "Newt",
    "Nightingale",
    "Octopus",
    "Okapi",
    "Opossum",
    "Oryx",
    "Ostrich",
    "Otter",
    "Owl",
    "Oyster",
    "Panther",
    "Parrot",
    "Partridge",
    "Peafowl",
    "Pelican",
    "Penguin",
    "Pheasant",
    "Pig",
    "Pigeon",
    "Pony",
    "Porcupine",
    "Porpoise",
    "Quail",
    "Quelea",
    "Quetzal",
    "Rabbit",
    "Raccoon",
    "Rail",
    "Ram",
    "Rat",
    "Raven",
    "Reindeer",
    "Rhinoceros",
    "Rook",
    "Salamander",
    "Salmon",
    "Sandpiper",
    "Sardine",
    "Scorpion",
    "Seahorse",
    "Seal",
    "Shark",
    "Sheep",
    "Shrew",
    "Skunk",
    "Snail",
    "Snake",
    "Sparrow",
    "Spider",
    "Spoonbill",
    "Squid",
    "Squirrel",
    "Starling",
    "Stingray",
    "Stinkbug",
    "Stork",
    "Swallow",
    "Swan",
    "Tapir",
    "Tarsier",
    "Termite",
    "Tiger",
    "Toad",
    "Trout",
    "Turkey",
    "Turtle",
    "Viper",
    "Vulture",
    "Wallaby",
    "Walrus",
    "Wasp",
    "Weasel",
    "Whale",
    "Wildcat",
    "Wolf",
    "Wolverine",
    "Wombat",
    "Woodcock",
    "Woodpecker",
    "Worm",
    "Wren",
    "Yak",
    "Zebra"
]

# autocomplete

for i in range(len(words)):
    words[i] = words[i].lower()

class Tree:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.childValues = []
        self.isEnd = False
    
    def addChild(self, childTree):
        self.children.append(childTree)
        self.childValues.append(childTree.val)
    
    def hasChild(self, childValue):
        if childValue in self.childValues:
            return True
        return False



encyclopedia = Tree(None)
current = encyclopedia
for animal in words:
    for letter in animal:
        if letter in current.childValues:
            current = current.children[current.childValues.index(letter)]
        else:
            child = Tree(letter)
            current.addChild(child)
            current = child
    current.isEnd = True
    current = encyclopedia
inputString = input("Input a one-word animal (\"x\" to stop): ")
while inputString != "x":
    if len(inputString) < 1:
        print("Invalid entry.")
        inputString = input("Input a one-word animal (\"x\" to stop): ")
        current = encyclopedia
        continue
    inputString = inputString.lower()
    isAnimal = True
    animal = None
    for letterIndex in range(len(inputString)):
        if not current.hasChild(inputString[letterIndex]):
            isAnimal = False
            animal = inputString[:letterIndex]
            while len(current.children) > 0:
                index = random.randint(0, len(current.children) - 1)
                animal += current.childValues[index]
                current = current.children[index]
            break
        else:
            current = current.children[current.childValues.index(inputString[letterIndex])]
    if isAnimal and current.isEnd:
        print("Is an animal.")
    elif not current.isEnd:
        animal = inputString[:letterIndex + 1]
        while len(current.children) > 0:
            index = random.randint(0, len(current.children) - 1)
            animal = (animal + current.childValues[index])
            current = current.children[index]
        print("Not an animal. Did you mean " + animal.capitalize() + "?")
    else:
        print("Not an animal. Did you mean " + animal.capitalize() + "?")



    inputString = input("Input a one-word animal (\"x\" to stop): ")
    current = encyclopedia


    
    
        
