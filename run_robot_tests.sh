#!/bin/bash

while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]]; 
  do sleep 1; 
done

poetry run robot src/tests

function clean_up {
  kill $(lsof -t -i:6000)
}

trap clean_up EXIT
