# tresc zadania: W zadanym katalogu ($1) przerób wszystkie dowiązania symboliczne, zdefiniowane ścieżkami względnymi, na równoważne zdefiniowane ścieżkami bezwzględnymi. 
#!bin/bash

if [ $# -ne 1 ]
then
	echo "Zla liczba argumentow!"
	exit 1
fi

if [ ! -d "$1" ]
then
	echo "Podany argument nie jest sciezka!!"
	exit 1
fi

cd "$1"

for file in *
do
	if [ -L "$file" ]
	then
		target=$(readlink -f "$file")
		ln -sf "$target" "$file"
		echo "Przeksztalcono dowiazanie symboliczne '$file' na '$target'"
	fi
done

echo "Koniec"
