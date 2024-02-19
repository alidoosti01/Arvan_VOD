#!/bin/bash

arr_id=()

read -p "Enter you API key: " apikey

echo "enter your VOD ids then enter -1 for continue: "
while read id && [ "$id" != -1 ]
do
       arr_id+=($id)
done

counter=0
for i in "${arr_id[@]}"
do
        echo -e "send Delete request for $i : "
        curl --location --request DELETE "https://napi.arvancloud.ir/vod/2.0/videos/$i" -H "Authorization: $apikey"
        echo -e "\n"
        ((counter++))
        if (( counter % 2 == 0 )); then
                echo "Pausing for 5 second ..."
                sleep 5
        fi
done
