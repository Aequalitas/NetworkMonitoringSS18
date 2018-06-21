#!/bin/bash

num=$(cat num.txt)
num=$(expr "$num" "+" "1")
echo $num > num.txt

## declare an array variable
declare -a arr=("192.168.76.75" "192.168.76.49" "192.168.76.50")
counter="0"
curfile="log"$num".json"
echo "[" >> "$curfile"
for i in "${arr[@]}"
do
   counter=$(expr "$counter" "+" "1")
   echo "[" >> "$curfile"
   curl -f "$i/cgi-bin/test.sh" >> "$curfile"
   echo "]" >> "$curfile"
   len=$(echo ${#arr[@]})
   if [ "$len" != "$counter" ]
   then
     echo "," >> "$curfile"
   fi
done
echo "]" >> "$curfile"
wget https://blog.numericserver.de/lol.php --post-file="$curfile"