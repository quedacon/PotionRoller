import random

stringpool = [
    "What can I get started for you?",
    "How would you like your potions today?",
    "Would you like fries with that?",
    "How's it goin?",
    "How does this work again?",
    "What does this button do?",
    "Did you say something?",
    "What is the airspeed velocity of an unlaiden swallow?",
    "Hows the weather where you're at?",
    "Take a bite out of crime!",
    "Have you tried... potions?",
    "Don't drink and drive.",
    "Let's Roll!",
    "Let's Potion!",
    "Let's Potions!",
    "Let's Potentiate!",
    "Let's Pontificate!",
    "I'll drink to that!",
    "Let's Get Potions!",
    "Let's Get Potioning!",
    "Let's Get Potionated!",
    "Let's Get Potatoed!",
    "Let's Kick Shell!",
    "Let's Drink!",
    "Let's Drink Potions!",
    "Let's EAT Potions!",
    "Let's do the thing!",
    "It's Exciting!",
    "It's Amazing!",
    "It's Brilliant!",
    "Guaranteed!",
    "It's OK!",
    "It's Random!",
    "Part of a Healthy Breakfast",
    "Made with Real Potion!",
    "Certified Fresh!",
    "My God, It's Full of Potions!",
    "Lets Roll Some Potions!",
    "Lets Brew!",
    "Are You Ready?",
    "Get Psyched!",
    "Ready to Roll... potions.",
    "Ready to Roll!",
    "Thirsty? Try Potions!",
    "Yes, but have you tried Potions?",
    "A Potion a Day Keeps the Cleric Away...",
    "Banned in 49 states!",
    "Banned in 52 countries!",
    "Now Playing!",
    "Now With Flavor!",
    "Now With Features!",
    "Now With Extra Bonus Features!",
    "Now With Director Commentary!",
    "Who reads these things anyway?",
    "Double, double, toil and trouble...",
    "Fire burn and cauldron bubble...",
    "Eye of newt and toe of frog...",
    "Scale of dragon, tooth of wolf...",
    "Adder's fork and blind-worm's sting...",
    "Lizard's leg and owlet's wing...",
    "Don't drink them all at once.",
]

def random_string():
    r = random.randrange(0, len(stringpool))
    return stringpool[r]