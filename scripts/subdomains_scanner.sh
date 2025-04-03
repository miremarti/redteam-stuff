#!/bin/bash

domain=$1

if [ ! -d "~/pentest" ];then
	mkdir ~/pentest
fi

if [ ! -d "~/pentest/$domain" ];then
	mkdir ~/pentest/$domain
fi

if [ ! -d "~/pentest/$domain/recon" ];then
	mkdir ~/pentest/$domain/recon
fi

if [ ! -d "~/pentest/$domain/recon/screenshots" ];then
	mkdir ~/pentest/$domain/recon/screenshots
fi

url=~/pentest/$domain/recon

echo "[+] Harvesting subdomains with assetfinder..."
assetfinder $domain > $url/assets.tmp
cat $url/assets.tmp | grep $domain > $url/assets.txt
rm $url/assets.tmp


echo "[+] Harvesting subdomains with amass..."
amass enum -d $domain >> $url/assets.txt
sort -u $url/assets.txt > $url/final_assets.txt
rm $url/assets.txt


echo "[+] Probing for alive domains..."
cat $url/final_assets.txt | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ':443' | sort -u > $url/alive_assets.txt


echo "[+] Making snapshots of alive domains..."
gowitness scan file -f $url/alive_assets.txt --no-http --screenshot-path $url/screenshots



