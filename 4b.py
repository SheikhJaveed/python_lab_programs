import re

def count_occurrences(text):
    vowels = re.findall(r'[aeiouAEIOU]', text)
    consonants = re.findall(r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]', text)
    digits = re.findall(r'\d', text)
    
    print("Vowels:", len(vowels))
    print("Consonants:", len(consonants))
    print("Digits:", len(digits))

count_occurrences("Hello World! 123")
