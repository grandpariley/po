#!/bin/bash

for i
do
case $i in 
    test)
#        load-env
        LOG_LEVEL='none' pipenv run python3 -m unittest discover
    ;;
    run)
#        load-env
        PIPENV_VERBOSITY=-1 LOG_LEVEL='debug' pipenv run python3 main.py
    ;;
esac
done
