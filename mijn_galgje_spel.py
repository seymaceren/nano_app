# Het spel galgje
# Het spel maakt gebruik van een JSON bestand waarin woorden gecatogoriseerd
# staan (makkelijk, gemiddeld en moeilijk).
# Gebruiker gevraaggd de moeilijkheidsgraad te selecteren
# Van elke gebruiker wordt  de score met de datum bijgehouden in een scorebestand
import json
import os
import random
import datetime
from json import JSONEncoder

# inhoud van mijn JSON bestand
woorden = {"makkelijk": ["bal", "appel", "klok","vogel","zon","maan","rups","kalf","haas","kip"],
                       "gemiddeld": ["bankstel", "laptoptas", "computer","geniaal", "vloerkleed","examen","schoolbus","regenlaarzen","capuchon","teamleider"],
                       "moeilijk": ["boodschappenlijstje", "paraferen", "geavanceerd","raamkozijn","gegeneraliseerd","eloquent","traditiegetrouw","belangeloos","adequaat"] }
# Deze functie zorgt ervoor dat voor elke foute invoer
# een deel van de hangman getekent wordt
# parameter aantal_fouten is de index van lijst hangman
def teken_galg(aantal_fouten):
    # variabele hangman is een lijst van strings in ASCI code
    hangman = [""" 
    ========
    |      |
    |
    |  
    |
    |
    """,
    """ 
    ========
    |      |
    |     ()
    |     
    |
    |
    """,
    """
    ========
    |      |
    |     ()
    |     /
    |
    |
    """,
    """ 
    ========
    |      |
    |     ()
    |     /|
    |
    |
    """,
    """ 
    ========
    |      |
    |     ()
    |     /|\\
    |
    |
    """,
    """ 
    ========
    |      |
    |     ()
    |     /|\\
    |     / \\
    |
    """]

    print(hangman[aantal_fouten])

def speel_galg():
    # met os.path.exist controleren we of het JSON bestand bestaat en zo niet:
    # dan wordt het toch aangemaakt.
    # Bij eerste keer runnen wordt het bestand aangemaakt
    print("Welkom bij Galg spel!")
    json_data = None
    if not os.path.exists("mijn_galgje_spel.json"):
        maak_bestand(woorden, "mijn_galgje_spel.json")
        # Na aanmaken van het bestand dictionary woorden toekennen aan json_data
        json_data = woorden
    else:
        # Als het bestand bestaat dan wordt het geopend om in te lezen in een JSON variabele
        with open("mijn_galgje_spel.json", "r") as file:
            json_data = json.load(file)
    # Als json_data niet none is
    if json_data:
        # Vraag de gebruiker zijn of haar naam
        naam = input("Wat is uw naam? ")
        # Vraag de moeilikheidsgraad
        moeilijkheidsgraad = input("Welke moeilijkheidsgraad? Makkelijk, gemiddeld of moeilijk? ")
        # Haal de woorden op basis van de moeilijksgraad uit het json_data
        woorden_op_moeilijkheidsgraad = json_data[moeilijkheidsgraad]
        # bepaal met random module een woord
        woord = random.choice(woorden_op_moeilijkheidsgraad)


        geraden_letters = []
        niet_geraden_letters = []
        is_running = True
        aantal_fouten = 0
        pogingen = 0
        # Zolang is_running True is dan,
        while is_running:
            #  dan wordt het galgje getekend op basis van aantal_fouten
            teken_galg(aantal_fouten)
            print(f"Je hebt nog {5 - aantal_fouten} pogingen.")
            # Als aantal fouten invoer gelijk is aan 5, geef dan een melding
            # dat speler niet heeft gewonnen en verlaat het spel
            if aantal_fouten == 5:
                print(f"{naam}, helaas je hebt 5 keer geprobeerd maar het woord {woord} niet geraden.")
                score_bijwerken(naam, False, pogingen)
                break

            letters_nog_te_raden = []
            # gebruikersinvoer voor het woord of de letter
            woord_of_letter = input(f"{naam} Raad het woord of letter? ")
            pogingen += 1
            # Als lengte van de invoer >1 dan is dat een geraden woord
            # en wordt vergeleken met het onthouden woord.
            # Als invoer gelijk is aan woord, dan geven we een melding van succes
            # en maken we 'is_running' variabele False, zodat niet verder gevraagd wordt
            if len(woord_of_letter) > 1 and woord_of_letter == woord:
                print(f"{naam}, gefeliciteerd! Je hebt het woord geraden.")
                is_running = False
                score_bijwerken(naam, True, pogingen)
            else:
                # Als de lengte van invoer 1 is en komt de letter voor in woord
                # dan wordt die toegevoegd in de lijst geraden_letters
                # als die in de lijst niet bestaat
                if len(woord_of_letter) == 1 and woord_of_letter in woord:
                    if woord_of_letter not in geraden_letters:
                        geraden_letters.append(woord_of_letter)
                    else:
                        # Als de gebruiker dezelfde letter meerdere keren invoert,
                        # dan verhogen we aantal_fouten met 1
                        aantal_fouten += 1
                        print("Deze letter heb je al ingevoerd.")
                else:
                    if len (woord_of_letter) == 1:
                        # Als de letter niet voorkomt, in het woord en al een
                        # keertje ingevoerd is, dan melden we dat die letter
                        # al een keer gebruikt is anders voegen we toe in de lijst
                        # niet_geraden_letters
                        if woord_of_letter in niet_geraden_letters:
                            print(f"je hebt letter {woord_of_letter} al gepropeerd.")
                        else:
                            niet_geraden_letters.append(woord_of_letter)

                    aantal_fouten += 1

                # Hier houden we een lijst van de geraden letters
                # en niet geraden letters bij zoals bv. bij 'klok' [k,_,_,k]
                for letter in woord:
                    if letter not in geraden_letters:
                        letters_nog_te_raden.append('_')
                    else:
                        letters_nog_te_raden.append(letter)

                if (aantal_fouten):
                    print(f"Je hebt deze letters al ingevoerd: {niet_geraden_letters}")
                print(letters_nog_te_raden)
                #  Hier controleren we alle geraden letters een woord vormen dat
                #  gelijk is aan het onthouden woord.
                #  Als dat het geval is dan geven een melding van succes.
                if "".join(letters_nog_te_raden) == woord:
                    print(f"{naam}, gefeliciteerd! Je hebt het woord geraden.")
                    is_running = False
                    score_bijwerken(naam, True, pogingen)

# Deze functie maakt een bestand met de meegegeven bestandsnaam
# parameter 'inhoud' is een dictionary die eerst omgezet wordt
# in een json string en die wordt daarna toegevoegd in het bestand.
def maak_bestand(inhoud, bestansnaam):
    with open(bestansnaam, "w+") as file:
        json_inhoud = json.dumps(inhoud)
        file.write(json_inhoud + "\n\r")

# Deze functie werkt de score van de spelers bij in een json bestand
# parameters naam, is_graden (boolean) en aantal pogingen
# Als datum wordt de datum van  vandaag bijgeschreven
def score_bijwerken(naam, is_geraden, pogingen):
    score = {}
    score["naam"] = naam
    score["woord_graden"] = is_geraden
    score["aantal_keren_raden"] = pogingen
    score["datum"] = datetime.datetime.now().strftime("%d/%m/%Y")
    if not os.path.exists("score.json"):
        maak_bestand(score, "score.json")
    else:
        with open("score.json", "a") as file:
            json_inhoud = json.dumps(score)
            file.write(json_inhoud + "\n\r")



