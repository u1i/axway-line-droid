from random import randint
import json

def random_color():

    colors=["amber", "amethyst", "apricot", "aqua", "aquamarine", "auburn", "azure", "beige", "black", "blue", "bronze", "brown", "buff", "cardinal", "carmine", "celadon", "cerise", "cerulean", "charcoal", "chartreuse", "chocolate", "cinnamon", "copper", "coral", "cream", "crimson", "cyan", "denim", "ebony", "ecru", "eggplant", "emerald", "forest", "green", "fuchsia", "gold", "goldenrod", "gray", "green", "grey", "hue", "indigo", "ivory", "jade", "jet", "khaki", "lavender", "lemon", "light", "lilac", "lime", "magenta", "mahogany", "maroon", "mauve", "mustard", "ocher", "olive", "orange", "orchid", "pale", "pastel", "peach", "periwinkle", "persimmon", "pewter", "pink", "primary", "puce", "pumpkin", "purple", "rainbow", "red", "rose", "ruby", "russet", "rust", "saffron", "salmon", "sapphire", "scarlet", "sepia", "shade", "shamrock", "sienna", "silver", "spectrum", "slate", "tan", "tangerine", "taupe", "teal", "terracotta", "thistle", "tint", "tomato", "topaz", "turquoise", "ultramarine", "umber", "vermilion", "violet", "viridian", "wheat", "white", "wisteria", "yellow"]
    return colors[randint(0,len(colors)-1)]

def random_animal():

    animals=["abalone", "albatross", "alligator", "amoeba", "ant", "antelope", "ape", "baboon", "badger", "barracuda", "bat", "beagle", "bear", "beaver", "bee", "beetle", "bird", "bison", "blowfish", "boxer", "bug", "bull", "bullfrog", "butterfly", "caiman", "camel", "canary", "caribou", "cat", "caterpillar", "cattle", "cavy", "centipede", "cheetah", "chickadee", "chicken", "chihuahua", "chipmunk", "clam", "clownfish", "cobra", "cod", "cockroach", "collie", "colugo", "cow", "coyote", "crab", "crane", "cricket", "crocodile", "crow", "dalmatian", "deer", "dingo", "dog", "dolphin", "donkey", "dragonfly", "dromedary", "duck", "eagle", "earthworm", "earwig", "eel", "elephant", "elk", "emu", "falcon", "ferret", "firefly", "fish", "flamingo", "flea", "flounder", "fly", "fox", "frog", "gazelle", "gecko", "gibbon", "giraffe", "gnu", "goat", "goldfish", "goose", "gopher", "gorilla", "grizzly", "groundhog", "hamster", "hare", "hawk", "hedgehog", "hen", "hippo", "horse", "hound", "husky", "hyena", "ibis", "jaguar", "jellyfish", "kangaroo", "kiwi", "koala", "krill", "ladybug", "lemming", "lemur", "leopard", "lion", "lizard", "llama", "lobster", "locust", "longhorn", "lynx", "mackerel", "mammoth", "mamba", "mastodon", "monkey", "moose", "mouse", "nautilus", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "owl", "ox", "panda", "panther", "parrot", "peacock", "pelican", "penguin", "pig", "pigeon", "piranha", "plankton", "puma", "python", "quail", "rabbit", "rat", "ray", "reindeer", "rhino", "roadrunner", "roach", "rooster", "sailfish", "salamander", "salmon", "sandpiper", "scallop", "scorpion", "seahorse", "seal", "shark", "sheep", "shrimp", "silkworm", "skipper", "sloth", "snail", "snake", "snapper", "sparrow", "spider", "squid", "stingray", "swan", "tiger", "toad", "tortoise", "tuna", "turkey", "turtle", "urchin", "viper", "vulture", "walrus", "wasp", "weasel", "whale", "wolf", "wombat", "worm", "yak", "zebra"]
    return animals[randint(0,len(animals)-1)]

with open('/home/brentano/bla.json') as json_data:
    d = json.load(json_data)
    print d

def random_username():
    new_name=random_color() + "_" + random_animal()
    return new_name

