#!/bin/bash

for i
do
case $i in 
    test)
#        load-env
        LOG_LEVEL='none' GENERATE_ONLY='false' python3 -m unittest discover
    ;;
    run)
#        load-env
        LOG_LEVEL='debug' GENERATE_ONLY='false' python3 main.py
    ;;
esac
done
