#!/usr/bin/env python3

''' 	
W zadanym drzewie katalogów znaleźć katalogi puste, 
do których właściciel nie ma prawa zapisu a ma prawo wykonania, 
natomiast właściciel grupowy lub inni mają prawo wykonania. 
Skrypt nie powinien zakładać żadnych dodatkowych warunków dotyczących praw dostępu. 
'''

import os
import sys
import stat

def checkPermission(path):
    status = os.stat(path)

    #prawa dostepu wlasciciela
    ownerWrite = bool(status.st_mode & stat.S_IWUSR)
    ownerExecute = bool(status.st_mode & stat.S_IXUSR)

    #prawa dostepu grupy
    groupExecute = bool(status.st_mode & stat.S_IXGRP)

    #prawa dostepu innych
    othersExecute = bool(status.st_mode & stat.S_IXOTH)

    return not ownerWrite and ownerExecute and (groupExecute or othersExecute)


def findEmptyDirectories(basePath):
    for dirPath, dirNames, fileNames in os.walk(basePath):
        #sprawdz czy katalog jest pusty
        if not dirNames and not fileNames:
            #sprawdz prawa dostepu
            if checkPermission(dirPath):
                print(dirPath)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("zla liczba argumentow!")
        sys.exit(1)

    basePath = sys.argv[1]

    if not os.path.isdir(basePath):
        print(f"{basePath} nie jest poprawnym katalogiem")
        sys.exit(1)

    findEmptyDirectories(basePath)
