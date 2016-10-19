# -*- coding: utf-8 -*-

def detect_language(text, languages):
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
            value = score
            result = language
    return result