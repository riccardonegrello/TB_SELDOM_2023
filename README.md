# TB_SELDOM_2023

Hi! This is a short guide to the code.
To use this code the acces to the data and the logbook is mandatory.

STEP 1: The alignment

The first thing to do is align the detector on the beam. Once the alignment run has been chosen, it has to be saved in a file called "config.json", this file will contain all the main variables that can be useful when operating the 3 codes.
The **run of the alignment** has to be the one with no crystal, so the detectors can be aligned.
Then move to the "CodeAlign.ipynb" which in principle will automatically calculate the offsets and save them in the "config.json". Some small tuning could be needed.

STEP 2: WHERE IS THE CRYSTAL?

In the Analysis code, the first part is dedicated to finding the correct position of the crystal on the beam.
This can be done in different ways but the one that is used exploits the deflections of the particles, so a lateral scan is required 
