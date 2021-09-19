#!/bin/bash

for i
do
case $i in 
    test)
#        load-env
        LOG_LEVEL='none' EXTERNAL_API='false' python3 -m unittest discover
    ;;
    run)
#        load-env
        # /usr/bin/time -v python3 main.py
        LOG_LEVEL='none' EXTERNAL_API='false' python3 main.py
    ;;
esac
done
