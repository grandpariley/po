#!/bin/bash

for i
do
case $i in 
    test)
        python3 -m unittest discover
    ;;
    run)
        # /usr/bin/time -v python3 main.py
        python3 main.py
    ;;
esac
done