#!/usr/bin/env python3

# W zadanym katalogu przerób wszystkie dowiązania symboliczne 
# wskazujące na pliki regularne 
# (do których wykonujący skrypt ma prawo odczytu), 
# na kopie wskazywanych plików. 


import os
import shutil
import sys

def replace(directory):

    dir = os.path.realpath(directory)

    try:
        entries = os.listdir(dir)
    except OSError:
        print(f"Odmowa dostepu: {dir}")
        
    for entry in entries:
        path = os.path.join(dir, entry)

        print(path)

        if os.path.islink(path):
            target = os.path.realpath(path)

            if os.path.isfile(targetPath) and os.access(target, os.R_OK):
                os.unlink(path)
                shutil.copy2(target,path)
                print(f"zastapiono dowiazanie {path} kopia {target}")
 
            else:
                print(f"Nie mozna zastapic dowiazania {path}, gdyz cel {targetPath} nie jest dostepny do odczytu")
        

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Zla liczba argumentow!")
        sys.exit(1)

    targetDirectory = sys.argv[1]
    if not os.path.isdir(targetDirectory):
        print(f"{targetDirectory} nie jest katalogiem!")
        sys.exit(1)

    replace(targetDirectory)
