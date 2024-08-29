#!/bin/bash

for i
do
case $i in 
    test)
        PIPENV_VERBOSITY=-1 LOG_LEVEL='none' pipenv run python3 -m unittest discover
    ;;
    run)
        PIPENV_VERBOSITY=-1 LOG_LEVEL='debug' pipenv run python3 main.py
        PIPENV_VERBOSITY=-1 LOG_LEVEL='debug' pipenv run python3 validation.py
        PIPENV_VERBOSITY=-1 LOG_LEVEL='debug' pipenv run python3 match.py
        PIPENV_VERBOSITY=-1 LOG_LEVEL='debug' pipenv run python3 evaluation.py
    ;;
esac
done
