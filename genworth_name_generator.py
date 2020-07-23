import random
import re

rock = ["Onyx", "Agate", "Agate Geode", "Almandine Garnet", "Amber", "Amazonite", "Amethyst", "Amethyst Geode", "Ametrine", "Ammolite", "Andalusite", "Andesine Labradorite", "Apatite", "Aquamarine", "Aventurine", "Beryl", "Black Opal", "Bloodstone", "Boulder Opal", "Calcite", "Carnelian", "Chalcedony", "Charoite", "Chocolate Opal", "Chrome Diopside", "Chrome Tourmaline", "Chrysoberyl", "Chrysocolla", "Chrysoprase", "Citrine", "Coral", "Demantoid Garnet", "Dendritic Agate", "Diamond", "Druzy Azurite", "Emerald", "Enstatite", "Fire Agate", "Fire Opal", "Fluorite", "Fossil Coral", "Garnet", "Golden Beryl", "Grandidierite", "Grossularite Garnet", "Hematite", "Hemimorphite Druzy", "Hessonite Garnet", "Hiddenite", "Howlite", "Idocrase", "Imperial Topaz", "Iolite", "Jade Gemstones", "Jadeite", "Jasper", "Kornerupine", "Kunzite", "Kyanite", "Labradorite", "Lapis Lazuli", "Larimar", "Malachite", "Malaya Garnet", "Mali Garnet", "Maw-Sit-Sit", "Moonstone", "Morganite", "Moss Opal", "Mother of Pearl", "Mystic Quartz", "Mystic Topaz", "Nuummite", "Obsidian", "Opal", "Opal Doublet", "Opal in Matrix", "Pearl", "Peridot", "Pietersite", "Prehnite", "Pyrite", "Pyrope Garnet", "Quartz", "Quartz With Marcasite", "Rainbow Moonstone", "Rainbow Pyrite", "Rhodochrosite", "Rhodolite Garnet", "Rhodonite", "Rose Quartz", "Ruby", "Ruby-Zoisite", "Rutile Quartz", "Sapphire", "Scolecite", "Seraphinite", "Serpentine", "Sillimanite", "Smithsonite", "Smoky Quartz", "Snowflake Obsidian", "Sodalite", "Spectrolite", "Spessartite Garnet", "Sphalerite", "Sphene", "Spinel", "Star Diopside", "Star Garnet", "Star Gemstones", "Star Lemon Quartz", "Star Moonstone", "Star Rose Quartz", "Star Ruby", "Star Sapphire", "Star Sunstone", "Strawberry Quartz", "Sugilite", "Sunstone", "Tanzanite", "Tiger's Eye", "Topaz", "Tourmaline", "Tsavorite Garnet", "Turquoise", "Variscite", "Zircon", "Quartz", "Marble", "Granite", "Flint", "Slate", "Shale", "Basalt", "Pumice", "Obsidian", "Chalk", "Coal"]
myth = ["Zeus", "Hera", "Poseidon", "Demeter", "Ares", "Athena", "Apollo", "Artemis", "Aphrodite", "Hermes", "Hades", "Hypnos", "Nike", "Iris", "Hypnos", "Chronos", "Thanatos", "Gaia", "Tartarus", "Hyperion", "Atlas", "Aura", "Helios", "Prometheus", "Styx", "Cyclops", "Orion", "Arachne", "Centaur", "Cerberus", "Chimera", "Harpy", "Medusa", "Minotaur", "Pegasus", "Scylla", "Siren", "Cupid", "Fauna", "Flora", "Fortuna", "Juno", "Jupiter", "Mars", "Mercury", "Minerva", "Neptune", "Pluto", "Saturn", "Venus", "Vulcan", "Ra", "Osiris", "Isis", "Horus", "Anubis"]
chem = ["Helium", "Lithium", "Hydrogen", "Sodium", "Boron", "Carbon", "Silicon", "Calcium", "Beryllium", "Fluorine", "Neon", "Sulfur", "Phosphorus", "Nitrogen", "Aluminum", "Potassium", "Chlorine", "Argon", "Magnesium", "Iron", "Bromine", "Oxygen", "Manganese", "Copper", "Cobalt", "Zinc", "Krypton", "Rubidium", "Silver", "Iodine", "Platinum", "Cadmium", "Tin", "Cesium", "Barium", "Francium", "Antimony", "Lead", "Nickel", "Chromium", "Bismuth", "Radon", "Radium", "Arsenic", "Xenon", "Uranium", "Strontium", "Polonium", "Mercury", "Gold", "Tungsten"]
animal = ["alligator", "ant", "bear", "bee", "bird", "camel", "cat", "cheetah", "chicken", "chimpanzee", "cow", "crocodile", "deer", "dog", "dolphin", "duck", "eagle", "elephant", "fish", "fly", "fox", "frog", "giraffe", "goat", "goldfish", "hamster", "hippopotamus", "horse", "kangaroo", "kitten", "lion", "lobster", "monkey", "octopus", "owl", "panda", "pig", "puppy", "rabbit", "rat", "scorpion", "seal", "shark", "sheep", "snail", "snake", "spider", "squirrel", "tiger", "turtle", "wolf", "zebra"]
pokemon = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidorina", "Nidoqueen", "Nidoran", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetched", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]

def consolidate (array):
    clean_names = []
    for string in array:
        str0 = shorten_words(string) 
        str1 = one_word(str0)
        str2 = no_specchar(str1) 
        if str0 is "null" or str1 is "null" or str2 is "null":
            continue
        else:
            clean_names.append(str2)
    no_repeat(clean_names)
    return(clean_names)

def shorten_words (string):
    if len(string) <= 8:
        return string
    else:
        return "null"

def one_word (string):
    if ' ' not in string:
        return string
    else:
        return "null"

def no_repeat (array):
    new_array = list(set(array))
    return new_array

def no_specchar (string):
    regex = re.compile('[().]')    
    if(regex.search(string) == None): 
        return string
    else:
        return "null"

first_names = []
last_names = []
first_names.append(consolidate(rock))
first_names.append(consolidate(chem))
last_names.append(consolidate(myth))
last_names.append(consolidate(animal))
last_names.append(consolidate(pokemon))

def randomize_final_name_list (first_names, last_names):
    i = 0
    final_list = []
    while i <= 1000000:
        category1 = random.choice(first_names)
        category2 = random.choice(last_names)
        name1 = (random.choice(category1)).capitalize()
        name2 = (random.choice(category2)).capitalize()
        final_name = (name1 + name2)
        final_list.append(final_name)
        i = i + 1
    no_repeat(final_list)
    return final_list

with open('names.txt', 'w') as f:
    final_list = randomize_final_name_list(first_names, last_names)
    for string in final_list:
        f.write(string + "\n")
    f.close()