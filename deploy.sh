#!/bin/bash

# Note: this a temporary script for app deployment

# Check if redis container is running
CONTAINER="redis"
HOST="0.0.0.0"
PORT="8000"

echo "[*] Checking if Redis container is running"
if [ "$(docker container inspect -f {{.State.Running}} $CONTAINER)" == "true" ]
then
    echo "[+] Container is running"
else
    echo "[+] Starting container"
    docker start $CONTAINER
fi

python manage.py runserver $HOST:$PORT