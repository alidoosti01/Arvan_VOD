#!/bin/bash

churl="https://napi.arvancloud.ir/vod/2.0/channels"
header="Content-Type: application/json"

read -p "Enter your API key: " apikey
function apiKeyValidator() {
    validateApiKey=$apikey
    pattern="^apikey [a-z0-9\-]+$"
    if [[ $validateApiKey =~ $pattern ]]
    then
        echo "$validateApiKey"
    else
        echo "Error: Invalid API, API token should be in format: 'apikey xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'"
        exit 1
    fi
}
apiKeyValidator

read -p "Enter channel id: " ch_id
function urlInput() {
    arr_id=()
    echo "enter your Vidoe URL then enter -1 for continue: "
    while read vodurl && [ "$vodurl" != -1 ]
    do
        arr_id+=($vodurl)
    done
}

function upload() {
    counter=0
    for i in "${arr_id[@]}"
    do
        filename="${i##*/}"
        out=$(curl -sS --location "$churl/$ch_id/$var1" -H "$header" -H "Authorization: $apikey" --data "{\"title\": \"$filename\",\"convert_mode\": \"auto\", \"$var2\": \"$i\"}")
        echo "$out" | jq '{ID: .data.id, name: .data.title, message: .message}'

        ((counter++))
        if (( counter % 30 == 0 )); then
            echo "Pausing for 3 second ..."
            sleep 3
        fi
    done
}

function detail() {
    for i in {1..100}
    do
        out=$(curl -sS --location "$churl/$ch_id/$var?page=$i&per_page=100" -H "Authorization: $apikey" | jq -c '.data[] | {ID: .id,   status: .status,   name: .title}')
        echo "$out"
        if [ -z "$out" ]; then
            break
        fi

    done
}

function retry() {
    declare -a arr_vid
    for i in {1..100}
    do
        out=$(curl -sS --location "$churl/$ch_id/$var?page=$i&per_page=100" -H "Authorization: $apikey" | jq -r '.data[] | .id')
        if [ -z "$out" ]; then
            break
        fi
        arr_vid+=($out)
    done

    for j in "${arr_vid[@]}"
    do
        status=$(curl -sS --location "https://napi.arvancloud.ir/vod/2.0/$var/$j" -H "Authorization: $apikey" | jq -r '.data.status')

        if [ "$status" != "complete" ]; then
            echo "ID: $j, Status: $status"
        fi
    done
}

handle_video() {
    local option
    select option in "Get All Videos" "Upload Video (URL)" "Back" "Quit"; do
        case $option in
            "Get All Videos")
                var="videos"
                detail;;

            "Upload Video (URL)")
                urlInput
                var1="videos"
                var2="video_url"
                upload;;

            Back)
                break;;

            Quit) exit;;
        esac
    done
}

handle_audio() {
    local option
    select option in "Get All Audios" "Upload Audio (URL)" "back" "quit"; do
        case $option in
            "Get All Audios")
                var="audios"
                detail;;

            "Upload Audio (URL)")
                urlInput
                var1="audios"
                var2="audio_url"
                upload;;

            back)
                break;;

            quit) exit;;
        esac
    done
}

handle_retry() {
    select option in "Retry the Videos" "Retry the Audios" "back" "quit"; do
        case $option in
            "Retry the Videos")
                var="videos"
                retry;;

            "Retry the Audios")
                var="audios"
                retry;;

            back)
                break;;

            quit) exit;;
        esac
    done
}

while true; do
    select choice in "Video" "Audio" "Retry" "Quit"; do
        case $choice in
            Video) handle_video;;
            Audio) handle_audio;;
            Retry) handle_retry;;
            Quit) exit;;
        esac
    done
done
