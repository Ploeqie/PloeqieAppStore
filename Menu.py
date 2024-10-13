print("Welkom bij PloeqieAppStore")

def selecteer_spel():
    while True:
        keuze = input("Selecteer een spel: Nummerraadspel (1) of Galgje (2): ")

        if keuze in ["Nummerraadspel", "1", "nummerraadspel"]:
            return "nummerraadspel"

        elif keuze in ["Galgje", "2", "galgje"]:
            return "galgje"

        else:
            print("Ongeldige keuze, probeer het opnieuw.")

def nummerraadspel():
    print("Je speelt nu het Nummerraadspel!")
    from spellen import cijferraadspel

def galgjespel():
    print("Je speelt nu Galgje!")
    from spellen import Galgjespel

while True:
    starten = selecteer_spel()

    if starten == "nummerraadspel":
        nummerraadspel()

    elif starten == "galgje":
        galgjespel()

    opnieuw = input("Wil je een nieuw spel starten? (ja/nee): ").lower()
    if opnieuw != "ja":
        print("Bedankt voor het spelen!")
        break