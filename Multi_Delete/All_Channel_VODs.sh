#!/bin/bash

read -p "Enter your API key: " apikey
read -p "Enter channel ID: " ch_id

declare -a vods_id

for i in {1..30}; do
        while IFS= read -r line; do
                vods_id+=("$line")
        done < <(curl -sS --location "https://napi.arvancloud.ir/vod/2.0/channels/$ch_id/videos?page=$i&per_page=30" -H "Authorization: $apikey" | jq -r '.data[].id')
done

counter=0
for i in "${vods_id[@]}"; do
        echo -e "send Delete request for $i : "
        curl --location --request DELETE "https://napi.arvancloud.ir/vod/2.0/videos/$i" -H "Authorization: $apikey"
        echo -e "\n"
        ((counter++))
        if (( counter % 2 == 0 )); then
                echo "Pausing for 5 second ..."
                sleep 5
        fi
done
