#!/bin/bash

# setup ATLAS software
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh

# setup AnalysisBase to make histograms and plots (default)
asetup 21.2,AnalysisBase,latest
