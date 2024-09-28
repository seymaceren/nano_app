# Het spel galgje
# Het spel maakt gebruik van een JSON bestand waarin woorden gecatogoriseerd
# staan (makkelijk, gemiddeld en moeilijk).
# Gebruiker gevraaggd de moeilijkheidsgraad te selecteren
# Van elke gebruiker wordt  de score met de datum bijgehouden in een scorebestand
import json
import os
from json import JSONEncoder

woorden = """{"makkelijk": ["bal", "appel", "klok","vogel","zon","maan","rups","kalf","haas","kip"], 
                       "gemiddeld": ["bankstel", "laptoptas", "computer","geniaal", "vloerkleed","examen","schoolbus","regenlaarzen","capuchon","teamleider"],
                       "moeijlijk": ["boodschappenlijstje", "paraferen", "geavanceerd","raamkozijn","gegeneraliseerd","eloquent","traditiegetrouw","belangeloos","adequaat"] }"""

def teken_galg(aantal_fouten):
    hangman = [""" 
    ========
    |      |
    |
    |  
    |
    |
    """,
    """ ========
        |      |
        |     ()
        |     
        |
        |
    """,
    """ ========
        |      |
        |     ()
        |     /
        |
        |
    """,
    """ ========
        |      |
        |     ()
        |     /|
        |
        |
    """,
    """ ========
        |      |
        |     ()
        |     /|\
        |
        |
    """,
    """ ========
        |      |
        |     ()
        |     /|\
        |     / \
        |
       """
               ]
    print(hangman[aantal_fouten])

def speel_galg():
    json_data = None
    if not os.path.exists("mijn_galgje_spel.json"):
        woorden_bestand = open("mijn_galgje_spel.json", "w+")
        woorden_bestand.write(woorden)
    else:
        with open("mijn_galgje_spel.json", "r") as file:
            json_data = json.load(file)

    if json_data:
        naam = input("Wat is uw naam? ")
        moeilijkheidsgraad = input("Welke moeilijkheidsgraad? Makkelijk, gemiddeld of moeilijk? ")
        woorden_op_moeilijkheidsgraad = json_data[moeilijkheidsgraad]
        print(woorden_op_moeilijkheidsgraad)

speel_galg()