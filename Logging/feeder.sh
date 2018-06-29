#!/bin/bash

echo "Content-type: application/json"
echo ""

echo "{"
echo "  \"host\": \""$(echo $HOSTNAME)"\","

cpu=$(top -b -n 1 | head -n 1 | cut -d":" -f5 | cut -d"," -f1 | xargs)
#cpu=$(bc -l <<< "$cpu/100" | awk '{printf "%f", $0}')
echo "  \"cpu\": \"$cpu\",";

memtot=$(top -b -n 1 | head -n 4 | tail -n 1 | cut -d":" -f2 | cut -d"," -f1)
memuse=$(top -b -n 1 | head -n 4 | tail -n 1 | cut -d":" -f2 | cut -d"," -f3)

memtot=$(echo $memtot | cut -d"t" -f1)
memuse=$(echo $memuse | cut -d"u" -f1)

memprz=$(bc -l <<< "$memuse/$memtot" | awk '{printf "%f", $0}')
echo "  \"mem\": \"$memprz\",";

disprz=$(df -l -BM --total | tail -n 1 | cut -d"M" -f4 | cut -d"%" -f1)
disprz=$(bc -l <<< "$disprz/100" | awk '{printf "%f", $0}')
echo "  \"disk\": \"$disprz\"";
echo "}"

echo ","

echo "{"
echo "  \"host\": \""$(echo $HOSTNAME)"\","
echo "  \"ipPacks\": \""$(netstat -s | grep "total packets" | cut -d"t" -f1 | xargs)"\","

resets=$(netstat -s | grep "resets" | cut -d"r" -f1 | cut -d"c" -f1 | head -n2)
resrec=$(echo $resets | xargs | cut -d" " -f1)
ressen=$(echo $resets | xargs | cut -d" " -f2)

echo "  \"TCPresetsReceived\": \""$resrec"\","
echo "  \"TCPresetsSend\": \""$ressen"\""
echo "}"

