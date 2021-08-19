#!/usr/bin/bash

SEED=1
NUMBER=100

for SONANTS in "" "--start-with-sonant"; do
    for CONSONANTS in "" "--end-with-consonant"; do
	for SYLLABLES in 2 3 4; do
	    COMMAND="python3 namegen.py --syllables $SYLLABLES $SONANTS $CONSONANTS --seed $SEED --number-of-names $NUMBER";
	    SEED=$((SEED+1));
	    echo $COMMAND;
	    $COMMAND;
	done
    done
done
