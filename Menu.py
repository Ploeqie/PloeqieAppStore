def hoofdmenu():
    while True:
        print("Welkom bij het PloeqieAppStore! Er volgen nu 3 keuzes die u kunt selecteren om te doen.")
        print("1. Nummer Raadspel")
        print("2. Galgje")
        print("3. Stoppen")

        keuze = input("Kies een spel: ")

        if keuze == '1':
            from spellen import Cijferraadspel
            Cijferraadspel()
        elif keuze == '2':
            from spellen import Galgjespel
            Galgjespel()
        elif keuze == '3':
            print("Bedankt voor het spelen!")
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")

hoofdmenu()