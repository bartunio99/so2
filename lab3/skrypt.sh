#!bin/bash
#W zadanym drzewie katalogów znaleźć pliki regularne,
# do których właściciel nie ma prawa zapisu,
# ale ktoś inny ma prawo wykonania,
# zmodyfikowane nie wcześniej niż 5 minut temu
# i nie później niż $2 (argument skryptu) minut temu.
if [ $# -ne 2 ]
then
	echo "Zla liczba argumentow!"
	exit 1
fi

if [ ! -d $1 ]
then
	echo "podany argument nie jest katalogiem!"
	exit 1
fi

find "$1" -type f ! -perm -u=w -perm /g=x,o=x -mmin +5 -mmin -$2 -print 
