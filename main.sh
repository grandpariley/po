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
    proposal)
        cd proposal
        pdflatex proposal.tex
        cd -
    ;;
    report)
        cd report
        pdflatex report.tex
        cd -
    ;;
    clean-tex)
        rm proposal/*.aux proposal/*.log report/*.aux report/*.log
    ;;
esac
done