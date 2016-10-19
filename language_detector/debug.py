# -*- coding: utf-8 -*-

from languages import LANGUAGES

text_spanish = """
    Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
    conocido como Leo Messi, es un futbolista argentino11 que juega
    como delantero en el Fútbol Club Barcelona y en la selección
    argentina, de la que es capitán. Considerado con frecuencia el
    mejor jugador del mundo y calificado en el ámbito deportivo como el
    más grande de todos los tiempos, Messi es el único futbolista en la
    historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
    ellos en forma consecutiva– y el primero en
    recibir tres Botas de Oro.
"""

text_german = """
    Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
    Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
    der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
    erzielte. Inzwischen hat Messi als einziger Spieler mehr als 300
    Erstligatore erzielt und ist damit Rekordtorschütze
    der Primera División.
"""

text_mixed = """
    # spanish
    Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
    conocido como Leo Messi, es un futbolista argentino11 que juega
    como delantero en el Fútbol Club Barcelona y en la selección
    argentina, de la que es capitán.

    # german
    Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
    Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
    der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
    erzielte.
"""

text_english = """
    # english
    Lionel Andrés 'Leo' Messi is an Argentine professional footballer
    who plays as a forward for Spanish club FC Barcelona and the
    Argentina national team. Often considered the best player in the
    world and rated by many in the sport as the greatest of all time,
    Messi is the only football player in history to win five FIFA
    Ballons, four of which he won consecutively, and the first player
    to win three European Golden Shoes.
"""

def print_language(text, languages):
    #split into a list of term
    
    split_text = text.lower().split()
    # for each language dictionary in the list of languages
    
    matches = {}
    
    for language in languages:
    #compare passage list of terms to lanage list of terms
        name = language['name']
        matches[name] = len([item for item in split_text if item in language['common_words']])
       
    result = ''
    value = 0
    #find the largest score in the matches dictionary
    for language, score in matches.items():
        if score > value:
            print language
            value = score
            result = language
    print result
    return result
    
print_language(text_english, LANGUAGES)