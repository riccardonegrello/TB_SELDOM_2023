# TB_SELDOM_2023

Hi! This is a short guide to the code.
To use this code access to the data and the logbook is mandatory.

STEP 1: The alignment

The first thing to do is align the detector on the beam. Once the alignment run has been chosen, it has to be saved in a file called "config.json". This file will contain all the main variables useful when operating the 3 codes.
The **run of the alignment** has to be the one with no crystal so that the detectors can be aligned.
Then move to the "CodeAlign.ipynb" which in principle will automatically calculate the offsets and save them in the "config.json". Some minor tuning could be needed.


