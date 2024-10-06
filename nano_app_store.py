# Nano App Store applicatie
# De gebruiker krijgt een keuze menu met een aantal spellen
# om te spelen
def main():
    print("Ceren's AppStore")
    print("Kies een spel om te spelen.")
    print("1. Nummer Raad Spel")
    print("2. Galg spel")
    keuze = int(input())

    if keuze == 1:
        import raadspel
    elif keuze == 2:
        import mijn_galgje_spel
        mijn_galgje_spel.speel_galg()


if __name__ == '__main__':
    main()
