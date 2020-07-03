#!/bin/bash

function clean-tex {
    rm -rf proposal/*.aux proposal/*.log proposal/*.blg proposal/*.bbl proposal/*.bcf proposal/*.xml report/*.aux report/*.log report/*.blg report/*.bbl report/*.bcf report/*.xml
}

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
        biber proposal
        pdflatex proposal.tex
        cd -
        clean-tex
    ;;
    report)
        cd report
        pdflatex report.tex
        biber report
        pdflatex report.tex
        cd -
        clean-tex
    ;;
    clean-tex)
        clean-tex    
    ;;
esac
done
