#!/bin/bash

# Validation plots:

# python plot.py DMsbb_truth_histograms_dsid110000.root --mass 50 --process "Dark Higgs"
# python plot.py DMsbb_truth_histograms_dsid110002.root --mass 50 --process "Dark Higgs"
# python plot.py DMsbb_truth_histograms_dsid110004.root --mass 50 --process "Dark Higgs"

# reweight from 1p0 to lower values for 50 GeV sample
python plot.py DMsbb_truth_histograms_dsid110000.root --mass 50 --process "Dark Higgs" \
    --couplings \
    "gx_0p1" \
    "gx_0p3" \
    "gx_0p5" \
    "gx_0p7" \
    "gx_1p0" \
    "gx_1p3" \
    --closure \
    ${PWD}/DMsbb_truth_histograms_dsid111000.root \
    ${PWD}/DMsbb_truth_histograms_dsid111001.root \
    ${PWD}/DMsbb_truth_histograms_dsid111002.root \
    ${PWD}/DMsbb_truth_histograms_dsid111003.root \
    ${PWD}/DMsbb_truth_histograms_dsid111004.root \
    ${PWD}/DMsbb_truth_histograms_dsid111005.root \


# reweight from 1p0 to lower values for 90 GeV sample
python plot.py DMsbb_truth_histograms_dsid110010.root --mass 90 --process "Dark Higgs" \
    --couplings \
    "gx_0p1" \
    "gx_0p3" \
    "gx_0p5" \
    "gx_0p7" \
    "gx_1p0" \
    "gx_1p3" \
    --closure \
    ${PWD}/DMsbb_truth_histograms_dsid111010.root \
    ${PWD}/DMsbb_truth_histograms_dsid111011.root \
    ${PWD}/DMsbb_truth_histograms_dsid111012.root \
    ${PWD}/DMsbb_truth_histograms_dsid111013.root \
    ${PWD}/DMsbb_truth_histograms_dsid111014.root \
    ${PWD}/DMsbb_truth_histograms_dsid111015.root \
