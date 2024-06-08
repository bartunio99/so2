#!/usr/bin/env python3

'''
W zadanym pliku tekstowym należy znaleźć i wylistować na ekran wszystkie teksty cytowane,
tzn. zamknięte w parach znaków ‘. Należy uwzględnić, 
że w tej samej linii może być wiele tekstów cytowanych, 
oraz że wewnątrz tekstu cytowanego mogą występować nowe linie.
'''

import re
import sys
import os

def readFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        return file.read()
    
def findQuotes(text):
    regex = re.compile(r"'(.*?)'",re.DOTALL)
    return regex.findall(text)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("zla liczba argumentow!")
        sys.exit(1)

    filePath = sys.argv[1]

    ext = os.path.splitext(filePath)[-1].lower()

    if not ext=='.txt':
        print(f"{filePath} nie jest plikiem tekstowym")
        sys.exit(1)

    text = readFile(filePath)
    quotes = findQuotes(text)

    for i, quote in enumerate(quotes,1):
        print(f"Cytat {i}: {quote}")
