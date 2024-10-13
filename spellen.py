import random

def Cijferraadspel():
    laagste = 1
    hoogste = int(input("Geef het hoogste getal waar je mee wilt spelen: "))
    max_attempts = int(input("Geef aan hoeveel kansen je wilt hebben: "))
    getal = random.randint(laagste, hoogste)

    def get_guess():
        while True:
            try:
                guess = int(input(f"Raad een getal tussen {laagste} en {hoogste}: "))
                if laagste <= guess <= hoogste:
                    return guess
                else:
                    print("Ongeldige input. Voer een getal tussen de waardes in.")
            except ValueError:
                print("Ongeldige invoer, probeer het opnieuw.")

    def check_guess(guess, getal):
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
                print(f"Gefeliciteerd! Je hebt {getal} in {attempts}x geraden.")
                won = True
                break
            else:
                print(f"{result}. Probeer opnieuw!")

        if not won:
            print(f"Sorry, je gokbeurten zijn over. Het juiste getal was {getal}.")

    print("Welkom bij het getal raad spel!")
    nummerraadspel()

    nogpotje = input("Wil je nog een potje spelen? (ja/nee): ").lower()
    if nogpotje == "ja":
        Cijferraadspel()
    else:
        from Menu import hoofdmenu  # Zorg ervoor dat deze import correct is
        hoofdmenu()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Hier begint het galgje!!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

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

    if miss_count < len(stages):
        print(stages[miss_count])
    else:
        print(stages[-1])


def Galgjespel():
    woordenlijst = [
        'afspraak', 'aanslag', 'abonnement', 'afdeling', 'aflevering', 'afspraak', 'afwas', 'afkomst', 'afkorting',
    'afspraak', 'afschuw', 'afgunst', 'afschaffen', 'afspraak', 'afstammeling', 'afval', 'afvalbak', 'afvalscheiding',
    'afvalverwerking', 'afvoer', 'afspelen', 'afspiegeling', 'afspraak', 'afschrikkend', 'afschuwelijk', 'agressief',
    'ahorn', 'alleen', 'afleiding', 'almond', 'aloe', 'alternatief', 'alpen', 'amber', 'ananas', 'analytisch',
    'aanpassing', 'ander', 'andere', 'anesthesie', 'angst', 'ankerkruid', 'applaus', 'appel', 'applicatie', 'april',
    'argeloos', 'aqua', 'aroma', 'armband', 'arrest', 'artiest', 'atlas', 'autobiografie', 'auto', 'bacterie',
    'ballet', 'banaan', 'barbecue', 'barkeeper', 'barometer', 'beweging', 'beetje', 'belangrijk', 'belastingen',
    'belgië', 'belgisch', 'belletje', 'beneden', 'bereiding', 'berichten', 'beroepsmatig', 'beslissing', 'betrekking',
    'beweging', 'bewaking', 'bewustzijn', 'biodiversiteit', 'biografie', 'bizarre', 'bladen', 'bladzijde', 'blessure',
    'blinde', 'bloem', 'bloemkool', 'boerderij', 'boogschutter', 'boor', 'boom', 'boek', 'boomgaard', 'boot', 'boze',
    'bron', 'brood', 'broodjes', 'broodrooster', 'brug', 'buik', 'bundel', 'burgt', 'butterfly', 'cabaret', 'cadeau',
    'camera', 'campus', 'capuchon', 'caravan', 'carrière', 'carnaval', 'ceremonie', 'chaos', 'chocolade', 'cirkel',
    'clown', 'communicatie', 'computer', 'consultant', 'contract', 'cursus', 'da Vinci', 'dagelijkse', 'dansen',
    'deksel', 'delfstoffen', 'denkbeeldig', 'denkproces', 'derde', 'desinfecteren', 'dezelfde', 'diamant', 'dieet',
    'doel', 'doelstellingen', 'dominator', 'donder', 'doorn', 'dubbel', 'duif', 'duizend', 'duizelingwekkend', 'edukatief',
    'economie', 'educatie', 'effectief', 'efectief', 'elegant', 'embleem', 'empire', 'empirisch', 'engagement', 'enigma',
    'enquête', 'epidemie', 'erfgoed', 'ergonomie', 'erfgenaam', 'ervaringsdeskundige', 'ervaringsuitwisseling', 'eerste',
    'eetstoornis', 'egocentrisch', 'eigen', 'eind', 'eisen', 'elektriciteit', 'element', 'elementair', 'elf', 'elektrisch',
    'emotioneel', 'envelop', 'envelope', 'enthousiast', 'ergonomisch', 'etentje', 'evenement', 'evenwicht', 'fabriek',
    'faciliteit', 'familie', 'farce', 'fantasie', 'fauna', 'fiets', 'figuur', 'film', 'flap', 'flessen', 'flits',
    'flitslicht', 'fluit', 'fluiter', 'fotografie', 'frisdrank', 'fruit', 'funtastisch', 'galgje', 'geluid', 'geluksgevoel',
    'geolied', 'geopolitiek', 'geplande', 'gerucht', 'gezelschap', 'gezondheid', 'gezicht', 'geschiedenis', 'gezin',
    'glaasje', 'globe', 'goede', 'grond', 'groen', 'grootte', 'haken', 'hals', 'handhaving', 'hapje', 'harigheid',
    'hardloop', 'hectare', 'hedendaags', 'herkenning', 'herinnering', 'hierarchie', 'historie', 'hoed', 'hoofd', 'hoop',
    'horloge', 'horizontaal', 'huishoudelijk', 'huis', 'huiskamer', 'huisterrein', 'ijverig', 'ijverig', 'ijverig',
    'ijskast', 'ijskoude', 'ijzel', 'ijzer', 'ik', 'illustratie', 'immigratie', 'impact', 'instructie', 'internet',
    'interview', 'introductie', 'invitatie', 'investering', 'io', 'isolatie', 'jaarlijks', 'januari', 'jargon', 'jeugd',
    'jodendom', 'jong', 'junior', 'juweel', 'kader', 'kaas', 'kaars', 'kaart', 'kader', 'kantoor', 'kaos', 'kerst',
    'keuken', 'kijken', 'klank', 'klankkast', 'klapper', 'klas', 'kleed', 'klein', 'kleinkind', 'knap', 'koppeling',
    'kopen', 'kras', 'krant', 'kruis', 'kruid', 'kruidenierswinkel', 'kruiswoord', 'laagland', 'laptop', 'lasagne',
    'lastig', 'levensonderhoud', 'levensstijl', 'licht', 'lichaam', 'lid', 'lingerie', 'lokaal', 'luchthaven', 'luidruchtig',
    'luifel', 'maak', 'maken', 'maaltijd', 'magie', 'magnetron', 'management', 'manier', 'medewerker', 'medicijn',
    'melk', 'menu', 'meten', 'metropolis', 'milieu', 'minister', 'moeder', 'moeilijk', 'moment', 'motor', 'museum',
    'mysterie', 'mystiek', 'mysterieuze', 'naald', 'naamsvermelding', 'naamwoord', 'neef', 'negen', 'netwerk', 'nieuw',
    'nieuws', 'nomineren', 'omgang', 'omroep', 'ontbijt', 'ontdekken', 'ontdoen', 'ontspanning', 'opdracht', 'opkomst',
    'oplossing', 'opmerking', 'organisch', 'organisatie', 'overeenkomst', 'overlijden', 'overzien', 'overwinning',
    'overtuiging', 'paddle', 'panda', 'parachute', 'park', 'partner', 'pech', 'peper', 'pesto', 'piano', 'pijpen',
    'pilaar', 'pincet', 'pizza', 'plan', 'plank', 'plankton', 'plezier', 'plezier', 'pluim', 'pluimvee', 'pocket',
    'politiek', 'polyester', 'pool', 'pop', 'poëzie', 'portfolio', 'procent', 'proef', 'profiel', 'project', 'pronk',
    'publiciteit', 'puin', 'publiek', 'quarantaine', 'quilt', 'raaf', 'raam', 'raar', 'raisin', 'rank', 'reageren',
    'recept', 'redacteur', 'relatie', 'remmen', 'repetitie', 'revolutie', 'rijden', 'rijken', 'rolstoel', 'romantisch',
    'ronde', 'rook', 'rooster', 'rustig', 'rustplaats', 'schaap', 'schaduw', 'schakelaar', 'scheiding', 'schijf',
    'schilder', 'schimmel', 'school', 'schoon', 'schrijf', 'schrijver', 'scooter', 'sneak', 'sneeuw', 'snijden', 'soep',
    'soul', 'spiegel', 'sport', 'sprinkhaan', 'standaard', 'standpunt', 'steun', 'stijl', 'stolperen', 'stoel', 'stoet',
    'stop', 'stoplicht', 'stroming', 'smaak', 'sneeuwbal', 'sneeuwman', 'sneeuwvlok', 'sneeuwstorm', 'snel', 'spanning',
    'spelen', 'spelt', 'spider', 'spons', 'spreeuw', 'stad', 'stap', 'star', 'streep', 'stijl', 'stijg',
    ]

    te_raden_woord = random.choice(woordenlijst)
    te_raden_letters = set(te_raden_woord)
    geraden_letters = set()
    foutieve_beurten = 0
    max_fouten = int(input("Geef aan hoeveel kansen je wilt hebben:  "))

    print("Welkom bij Galgje!")

    while len(te_raden_letters) > 0 and foutieve_beurten < max_fouten:
        print(f"Je hebt {max_fouten - foutieve_beurten} pogingen over.")
        print("Geraadde letters: ", " ".join(geraden_letters))
        print("Huidige status: ", " ".join([letter if letter in geraden_letters else '_' for letter in te_raden_woord]))

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

    nogpotje = input("Wil je nog een potje spelen? (ja/nee): ").lower()

    if nogpotje == "ja":
        Galgjespel()
    else:
        from Menu import selecteer_spel

