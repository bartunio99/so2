#Zmiana nazw wszystkich plików w zadanym katalogu (parametr wywołania skryptu), do których 
#mamy ustawione prawo odczytu i zapisu, przez dopisanie dodatkowego członu .old. Wcześniej
#należy skasować wszystkie pliki, które już mają takie rozszerzenie.
#!/bin/bash

if [ $# -ne 1 ]
then
	echo "Zla liczba argumentow!!"
	exit 1
fi


if [ ! -d "$1" ]
then
	echo "Argument nie jest sciezka!"
	exit 1
fi

rm -f "$1"/*.old

for file in "$1"/*
do
	if [ -f "$file" ] && [ -w "$file" ] && [ -r "$file" ]
	then
			mv "$file" "$file.old"
	fi
done
