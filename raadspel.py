# Python nummer raad spel. Laat de computer een random integer bepalen.
import random
# Bepaal laagste een hoogste getal
laagste_num = 1
hoogste_num = 20

# Onthoud een getal tussen het laagste_num en hoogste_num
antwoord = random.randint(laagste_num, hoogste_num)

print("Python nummer raad spel")
print(f"Selecteer een nummer tussen {laagste_num} en {hoogste_num}")

# Laat de gebruiker 5 keer raden
for poging in range(5):

    gok = input("Doe een gok: ")
    # Is de invoer en cijfer dan doe je volgende stap
    if gok.isdigit():
        # Converteer tekst naar integer
        gok = int(gok)

    if gok < laagste_num or gok > hoogste_num:
      print("Dat nummer is out of range")
      print( "Selecteer alsjeblieft een nummer tussen 1 en 20")
    elif gok < antwoord:
       print("Te laag! Probeer nog een keer")
    elif gok > antwoord:
       print("Te hoog! Probeer nog een keer")

    else:
       print(f"Correct! Het goede antwoord was {antwoord}")
       print(f"Aantal pogingen: {poging + 1}")
       break
# Als na vijf pogingen het getal niet is geraden
# dan for-loop eindigt en 'else' conditie is waar
else:
    print("Helaas! Je hebt verloren")
    print("aantal pogingen: 5 keer")


