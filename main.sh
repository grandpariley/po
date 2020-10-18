#!/bin/bash

function clean-tex {
    rm -rf proposal/*.fls proposal/*.aux proposal/*.log proposal/*.blg proposal/*.bbl proposal/*.bcf proposal/*.xml proposal/*.dvi proposal/*.fdb_latexmk report/*.aux report/*.log report/*.blg report/*.bbl report/*.bcf report/*.xml report/*.dvi report/*.fdb_latexmk report/*.fls
}

function load-env {
    if [ -f .env ]
    then
        export "$(< .env xargs)"
    fi
}

for i
do
case $i in 
    test)
        load-env
        python3 -m unittest discover
    ;;
    run)
        load-env
        # /usr/bin/time -v python3 main.py
        python3 main.py
    ;;
esac
done
