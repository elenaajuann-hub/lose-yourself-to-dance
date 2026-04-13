#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Not enough parameters"
    exit -1
fi


if [ ! -d $1 ]
then
    echo "Is not a directory"
    exit -1
fi


while read directory #In this function we reset the made-up directories to make easier the index-carpet assignation
do
    while read file
    do
        mv "$1/$directory/$file" "$1"
    done < <(ls "$1/$directory/")
done < <(ls $1 | grep -E "P")


count=$(ls $1 | grep -E ".sh" | cut -d'_' -f1 | sort -u | wc -l) #Here it counts the number of different index


for((i=1; i<=$count; i++)) #It makes all different index-directories
do
    if [ -d "/$1/P$i" ]
    then
        break
    else
        mkdir P$i
        mv P$i $1
    fi
done


while read file #We move files to the directory
do      

    index=$(echo "$file" | cut -d'_' -f1 | rev | cut -c 1)
    mv "$1/$file" "$1/P$index/"
done < <(ls $1 | grep -E ".sh")