#!/bin/bash
#run tools as root user!

#colors
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
blue=`tput setaf 4`
magenta=`tput setaf 5`
reset=`tput sgr0`

read -p "Enter the Domain name : " DOM

if [ -d ~/Desktop ]
then
  echo " "
else
  sudo mkdir ~/Desktop
fi

if [ -d ~/Desktop/$DOM ]
then
  echo " "
else
  sudo mkdir ~/Desktop/$DOM
  chmod 777 $DOM
fi

if [ -d ~/Desktop/$DOM/Subdomains ]
then
  echo " "
else
  sudo mkdir ~/Desktop/$DOM/Subdomains 
fi
echo "${red}  ____  _____ ____ ___  _   _ _              
|  _ \| ____/ ___/ _ \| \ | (_)_______ _ __ 
| |_) |  _|| |  | | | |  \| | |_  / _ \ '__|
|  _ <| |__| |__| |_| | |\  | |/ /  __/ |   
|_| \_\_____\____\___/|_| \_|_/___\___|_|   "
echo "${red} BY 5YN1X"
echo " "
echo " "
echo "${blue} [+] Started Subdomain Enumeration ${reset}"

#assefinder
echo "${yellow} ---------------------------------- xxxxxxxx ---------------------------------- ${reset}"
echo " "
if [ -f /usr/local/bin/assetfinder ]
then
  echo "${magenta} [+] Running Assetfinder for subdomain enumeration${reset}"
  assetfinder -subs-only $DOM  >> ~/Desktop/$DOM/Subdomains/assetfinder.txt 
else
  echo "${blue} [+] Installing Assetfinder ${reset}"
  go get -u github.com/tomnomnom/assetfinder
  echo "${magenta} [+] Running Assetfinder for subdomain enumeration${reset}"
  assetfinder -subs-only $DOM  >> ~/Desktop/$DOM/Subdomains/assetfinder.txt
fi
echo " "
echo "${blue} [+] Succesfully saved as assetfinder.txt  ${reset}"
echo " "

#subfinder
echo "${yellow} ---------------------------------- xxxxxxxx ---------------------------------- ${reset}"
echo " "
if [ -f /usr/local/bin/subfinder ]
then
  echo "${magenta} [+] Running Subfinder for subdomain enumeration${reset}"
  subfinder -d $DOM -o ~/Desktop/$DOM/Subdomains/subfinder.txt 
else
  echo "${blue} [+] Installing Subfinder ${reset}"
  go get -u -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder
  echo "${magenta} [+] Running Subfinder for subdomain enumeration${reset}"
  subfinder -d $DOM -o ~/Desktop/$DOM/Subdomains/subfinder.txt
fi
echo " "
echo "${blue} [+] Succesfully saved as subfinder.txt  ${reset}"
echo " "

#uniquesubdomains
echo "${yellow} ---------------------------------- xxxxxxxx ---------------------------------- ${reset}"
echo " "
echo "${magenta} [+] Fetching unique domains ${reset}"
echo " "
cat ~/Desktop/$DOM/Subdomains/*.txt | sort -u >> ~/Desktop/$DOM/Subdomains/unique.txt
echo "${blue} [+] Succesfully saved as unique.txt ${reset}"
echo " "

#sorting alive subdomains
echo "${yellow} ---------------------------------- xxxxxxxx ---------------------------------- ${reset}"
echo " "
if [ -f /usr/bin/httpx-toolkit ]
then
  echo "${magenta} [+] Running Httpx for sorting alive subdomains${reset}"
  cat ~/Desktop/$DOM/Subdomains/unique.txt | httpx-toolkit >> ~/Desktop/$DOM/Subdomains/all-alive-subs.txt
  cat ~/Desktop/$DOM/Subdomains/all-alive-subs.txt | sed 's/http\(.?*\)*:\/\///g' | sort -u > ~/Desktop/$DOM/Subdomains/protoless-all-alive-subs.txt
else 
  echo "${blue} [+] Installing Httpx ${reset}"
  go get -u github.com/projectdiscovery/httpx/cmd/httpx
  echo "${magenta} [+] Running Httpx for sorting alive subdomains${reset}"
  cat ~/Desktop/$DOM/Subdomains/unique.txt | httpx-toolkit >> ~/Desktop/$DOM/Subdomains/all-alive-subs.txt
  cat ~/Desktop/$DOM/Subdomains/all-alive-subs.txt | sed 's/http\(.?*\)*:\/\///g' | sort -u > ~/Desktop/$DOM/Subdomains/protoless-all-alive-subs.txt
fi
echo " "
echo "${blue} [+] Successfully saved the results"
echo " "
echo " "
echo "${blue} [+] Your Recon Succsessfully Completed!!"

/usr/bin/python3 telegram_automation.py
