#!/bin/bash

# Color
R="\033[;31;m" #Red 
G="\033[;32;m" #Green
B="\033[;34;m" #Blue
Y="\033[;33;m" #Yellow
W="\033[;0;m"  #White

# Module
if ! command -v requests &> /dev/null
then
    echo -e "${G}Download Module 'requests' ....${W}"
    pip install requests && clear
fi
if ! command -v readline &> /dev/null
then
    echo -e "${G}Download Module 'readline' ....${W}"
    pkg i readline* && clear
fi

# value
read -p "Enter your router ip [ex: 192.168.1.1] >>> " your_router_ip
if ! curl -s --head --request GET "http://${your_router_ip}" | grep "HTTP/1.1" > /dev/null; then
    echo -e "${R}Unexpected error :/ \n${G}Tips \n${Y}+${B} Check your internet connection \n${Y}+${B} check your IP input correctly \n${W}"
    exit
fi
list_ips=()

# start scan
while true
do
    nmap -sn "${your_router_ip}"/24 | grep "for ${your_router_ip:0:4}" > wifi.txt
    while read -r ip
    do
        if ! [[ "${list_ips[*]}" =~ "$ip" ]]; then
            list_ips+=("$ip")
            echo -e "${W}>>> ${Y}${ip#*for}: -t [${G}CONNECT${W}] -t [${B}Total:${G}${#list_ips[@]}${W}] -t ${B}TIME: ${Y}$(date '+%H:%M:%S')${W}"
        fi
    done < "wifi.txt"
    for ip in "${list_ips[@]}"
    do
        if ! grep -q "$ip" "wifi.txt"; then
            list_ips=("${list_ips[@]/$ip}")
            echo -e "${W}>>> ${Y}${ip#*for}: -t [${R}DISCONNECT${W}] -t [${B}Total:${R}${#list_ips[@]}${W}] -t ${B}TIME: ${Y}$(date '+%H:%M:%S')${W}"
        fi
    done
    sleep 10
done

trap 'echo -e "${Y} User:${R} CTRL + C \n${Y} User stop the operation \n${R} Exit ...${W}" && rm wifi.txt && exit' INT TERM
