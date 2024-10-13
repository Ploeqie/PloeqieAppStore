def cijferraadspel():
    import random

    laagste = 1
    hoogste = int(input("Geef het hoogste getal waar je mee wilt spelen:  "))
    max_attempts = int(input("Geef aan hoeveel kansen je wilt hebben:  "))

    getal = random.randint(laagste, hoogste)

    def get_guess():
        while True:
            try:
                guess = int(input(f"Raad een getal tusen {laagste} em {hoogste}: "))
                if laagste <= guess <= hoogste:
                    return guess
                else:
                    print("ongeldige input. Voer een getal tussen de waardes in")
            except ValueError:
                print("Ongeldige invoer probeer het opnieuw.")

    def check_guess(guess, secret_number):
        if guess == getal:
            return "Correct"
        elif guess < getal:
            return "Te laag"
        else:
            return "Te hoog"

    def nummerraadspel():
        attempts = 0
        won = False

        while attempts < max_attempts:
            attempts += 1
            guess = get_guess()
            result = check_guess(guess, getal)

            if result == "Correct":
                print(f"Gefeliciteerd! Je heb {getal} in {attempts}x geraden.")
                won = True
                break
            else:
                print(f"{result}. Probeer opnieuw!")

        if not won:
            print(f"Sorry, je gokbeurten zijn over het juiste getal was {getal}.")

    if __name__ == "__main__":
        print("Welkom bij het getal raad spel!")
        nummerraadspel()






def Galgjespel():
    import random

    def print_galg(miss_count):
        stages = [
            """  
                --------
                |      |
                |      
                |    
                |     
                |     
                -   
             """,
            """  
                --------
                |      |
                |      O
                |    
                |     
                |     
                -   
             """,
            """  
                --------
                |      |
                |      O
                |      |
                |     
                |     
                -   
             """,
            """  
                --------
                |      |
                |      O
                |     /|
                |     
                |     
                -   
             """,
            """  
                --------
                |      |
                |      O
                |     /|\\
                |     
                |     
                -   
             """,
            """  
                --------
                |      |
                |      O
                |     /|\\
                |     / 
                |     
                -   
             """,
            """  
                --------
                |      |
                |      O
                |     /|\\
                |     / \\
                |     
                -   
             """,
        ]

        # Zorg ervoor dat je niet verder gaat dan het aantal stages
        if miss_count < len(stages):
            print(stages[miss_count])
        else:
            print(stages[-1])  # Laat de laatste galg zien als je meer foutieve beurten hebt

    def galgje():
        woordenlijst = [
            'aan', 'aanbod', 'aanraken', 'aanval', 'aap', 'aardappel',
            # Voeg hier meer woorden toe als nodig
        ]

        te_raden_woord = random.choice(woordenlijst)
        te_raden_letters = set(te_raden_woord)
        geraden_letters = set()
        foutieve_beurten = 0
        max_fouten = 6  # Maximaal aantal mislukte beurten voor een spel

        print("Welkom bij Galgje!")

        while len(te_raden_letters) > 0 and foutieve_beurten < max_fouten:
            print(f"Je hebt {max_fouten - foutieve_beurten} pogingen over.")
            print("Geraadde letters: ", " ".join(geraden_letters))
            print("Huidige status: ",
                  " ".join([letter if letter in geraden_letters else '_' for letter in te_raden_woord]))

            gok = input("Raad een letter: ").lower()

            if gok in geraden_letters:
                print("Je hebt deze letter al geraden.")
            elif gok in te_raden_letters:
                geraden_letters.add(gok)
                te_raden_letters.remove(gok)
                print(f"Goed gedaan! {gok} zit in het woord.")
            else:
                foutieve_beurten += 1
                print(f"Fout! {gok} zit niet in het woord.")
                print_galg(foutieve_beurten)

        if foutieve_beurten == max_fouten:
            print(f"Helaas, je hebt verloren. Het woord was {te_raden_woord}.")
        else:
            print(f"Gefeliciteerd! Je hebt het woord {te_raden_woord} geraden.")

        nogpotje = input("Wil je nog een potje spelen?").lower()

        if nogpotje == "ja":
            galgje()
        else:
            from Menu import selecteer_spel

    galgje()