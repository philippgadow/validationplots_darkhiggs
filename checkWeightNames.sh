#!/bin/bash

# setup ATLAS software
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh

# setup AthAnalysis to check metadata of DxAODs using checkMetaSG.py
asetup 21.2,AthAnalysis,latest
DxAOD="${1}"
if [[ -z ${DxAOD} ]]; then
    DxAOD="/nfs/dust/atlas/user/pgadow/MC/TRUTH/110000/DAOD_TRUTH1.mc16_13TeV.110000.125923.root"
fi

mkdir run_weightcheck && cd run_weightcheck
checkMetaSG.py ${DxAOD} | tee weights.txt
cd -
