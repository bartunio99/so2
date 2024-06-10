#!/bin/bash

#W zadanym drzewie katalogów wylistować wszystkie pliki regularne, mające jedno z rozszerzeń o postaci „exe” 
#(wielokrotne rozszerzenia to rozszerzenia, od kropki do kropki lub do końca nazwy, gdy plik ma wiele kropek w nazwie). 

if [ $# -ne 1 ]
    then
        echo "Zla liczba argumentow"
        exit
fi

if [ ! -d $1 ]
    then    
        echo "Argument nie jest katalogiem!"
        exit
fi


find $1 -type f | awk 'tolower($0) ~ /\.exe(\..*)?$/'
