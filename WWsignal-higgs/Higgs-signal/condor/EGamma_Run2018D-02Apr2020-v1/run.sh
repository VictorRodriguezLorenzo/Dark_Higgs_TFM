#!/bin/bash
source /cvmfs/sft.cern.ch/lcg/views/LCG_104a/x86_64-el9-gcc11-opt/setup.sh
source /afs/cern.ch/user/v/victorr/private/mkShapesRDF/myenv/bin/activate
time python runner.py
cp output.root /afs/cern.ch/user/v/victorr/private/WWsignal-higgs/Higgs-signal/rootFiles__darkHiggs2018_v7/mkShapes__darkHiggs2018_v7__ALL__${1}.root
rm output.root
rm script.py
