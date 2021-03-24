import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from argparse import ArgumentParser
from utils import readxAOD, DecayingParticle, getDSID
from tqdm import tqdm
import logging


def getArguments():
    parser = ArgumentParser()
    parser.add_argument("input")
    parser.add_argument(
        "--weights", nargs="*", default=["nominal", "gx_0p1", "gx_0p3", "gx_0p5", "gx_0p7", "gx_1p0", "gx_1p3", "gx_1p7", "gx_2p0", "gx_2p3", "gx_2p7"]
    )
    parser.add_argument("-o", "--output", default="DMsbb_truth_histograms")
    return parser


def main():
    # get arguments from command line
    args = getArguments().parse_args()
    # get input tree
    t = readxAOD(args.input)
    # get weights to process
    weight_to_run = {i for i in args.weights}
    # position of first reweight weight (considering offset of 1 to start counting with 1)
    weightmap_move = 110 - 1
    # counter of events with no stored Zprime for bookkeeping
    n_events_nozprime = 0

    # Set the Histograms sets
    histset = {}
    for wtsuffix in weight_to_run:
        histset["mDH" + wtsuffix] = ROOT.TH1D(
            "h_DH_m_" + wtsuffix, "Mass of dark Higgs", 300, 0.0, 300.0
        )
        histset["ptDH" + wtsuffix] = ROOT.TH1D(
            "h_DH_pt_" + wtsuffix, "pT of dark Higgs", 100, 0.0, 1000.0
        )
        histset["ptb1" + wtsuffix] = ROOT.TH1D(
            "h_b1_pt_" + wtsuffix, "pT of first b-quark", 100, 0.0, 1000.0
        )
        histset["ptb2" + wtsuffix] = ROOT.TH1D(
            "h_b2_pt_" + wtsuffix, "pT of second b-quark", 100, 0.0, 1000.0
        )
        histset["met" + wtsuffix] = ROOT.TH1D(
            "h_met_" + wtsuffix, "pT of dark matter particle pair", 150, 0.0, 1500.0
        )
    for key in histset.keys():
        histset[key].Sumw2()

    # Set the weight map
    weightmap = {
        "nominal": weightmap_move * (-1),  # should match 0-th weight: weightmap_move - weightmap_move = 0
        "gx_0p1": 1,
        "gx_0p2": 2,
        "gx_0p3": 3,
        "gx_0p4": 4,
        "gx_0p5": 5,
        "gx_0p6": 6,
        "gx_0p7": 7,
        "gx_0p8": 8,
        "gx_0p9": 9,
        "gx_1p0": 10,
        "gx_1p1": 11,
        "gx_1p2": 12,
        "gx_1p3": 13,
        "gx_1p4": 14,
        "gx_1p5": 15,
        "gx_1p6": 16,
        "gx_1p7": 17,
        "gx_1p8": 18,
        "gx_1p9": 19,
        "gx_2p0": 20,
        "gx_2p1": 21,
        "gx_2p2": 22,
        "gx_2p3": 23,
        "gx_2p4": 24,
        "gx_2p5": 25,
        "gx_2p6": 26,
        "gx_2p7": 27,
        "gx_2p8": 28,
        "gx_2p9": 29,
        "gx_3p0": 30,
        "gx_3p1": 31,
        "gx_3p2": 32,
        "gx_3p3": 33,
        "gx_3p4": 34,
        "gx_3p5": 35,
    }

    # loop over tree
    for evnt in tqdm(range(t.GetEntriesFast())):
        t.GetEntry(evnt)

        # get weight (using the weight dict defined previously)
        # the weight positions were determined using an AthAnalysis environment and checkMetaSG.py
        # to associate the weight positions to the weight name
        wt = {}
        for wtsuffix in weight_to_run:
            try:
                wt[wtsuffix] = t.EventInfo.mcEventWeights()[
                    weightmap[wtsuffix] + weightmap_move
                ]
                logging.debug(
                    "Event weight found. event = {evnt}, wt = {wt}".format(
                        evnt=evnt, wt=wt[wtsuffix]
                    )
                )
            except KeyError:
                wt[wtsuffix] = 1.0
                logging.warning(
                    "Event weight not found. event = {evnt}, wt = {wt}. Setting it to 1.0.".format(
                        evnt=evnt, wt=wt[wtsuffix]
                    )
                )

        ##################
        # find particles
        ##################
        decaying_Zprime = None
        mother_chi1 = None
        mother_chi2 = None
        decaying_chi1 = None
        decaying_chi2 = None

        decaying_darkHiggs = None
        mother_b1 = None
        mother_b2 = None
        decaying_b1 = None
        decaying_b2 = None


        # Note: PDG IDs of particles in dark Higgs model
        # - zprime: 55
        # - dark Higgs: 54
        # - dark matter: 1000022

        # loop over truth particles to find the VLB, Higgs, and b-quark
        for tp in t.TruthParticles:
            # find Zprime (further decaying to dark matter particles)
            if tp.absPdgId() == 55 and decaying_Zprime == None:
                decaying_Zprime = DecayingParticle(tp)
                # find dark matter particles
                if decaying_Zprime.nChildren() == 2 and decaying_Zprime.child(0).pdgId() == 1000022 and decaying_Zprime.child(1).pdgId() == 1000022:
                    mother_chi1 = decaying_Zprime.child(0)
                    mother_chi2 = decaying_Zprime.child(1)
                    decaying_chi1 = DecayingParticle(mother_chi1)
                    decaying_chi2 = DecayingParticle(mother_chi2)
                elif decaying_Zprime.nChildren() == 3 and decaying_Zprime.child(0).pdgId() == 54 and decaying_Zprime.child(1).pdgId() == 1000022 and decaying_Zprime.child(2).pdgId() == 1000022:
                    mother_chi1 = decaying_Zprime.child(1)
                    mother_chi2 = decaying_Zprime.child(2)
                    decaying_chi1 = DecayingParticle(mother_chi1)
                    decaying_chi2 = DecayingParticle(mother_chi2)
                elif decaying_Zprime.nChildren() == 3 and decaying_Zprime.child(0).pdgId() == 1000022 and decaying_Zprime.child(1).pdgId() == 54 and decaying_Zprime.child(2).pdgId() == 1000022:
                    mother_chi1 = decaying_Zprime.child(0)
                    mother_chi2 = decaying_Zprime.child(2)
                    decaying_chi1 = DecayingParticle(mother_chi1)
                    decaying_chi2 = DecayingParticle(mother_chi2)
                elif decaying_Zprime.nChildren() == 3 and decaying_Zprime.child(0).pdgId() == 1000022 and decaying_Zprime.child(1).pdgId() == 1000022 and decaying_Zprime.child(2).pdgId() == 54:
                    mother_chi1 = decaying_Zprime.child(0)
                    mother_chi2 = decaying_Zprime.child(1)
                    decaying_chi1 = DecayingParticle(mother_chi1)
                    decaying_chi2 = DecayingParticle(mother_chi2)
                else:
                    print('else')
                    logging.error("No decays to dark matter particles found")
                    continue
            # find dark Higgs
            if tp.absPdgId() == 54 and decaying_darkHiggs == None:
                decaying_darkHiggs = DecayingParticle(tp)
                # find b-quarks
                if decaying_darkHiggs.child(0).pdgId() == 5:
                    mother_b1 = decaying_darkHiggs.child(0)
                    mother_b2 = decaying_darkHiggs.child(1)
                    decaying_b1 = DecayingParticle(mother_b1)
                    decaying_b2 = DecayingParticle(mother_b2)
                elif decaying_darkHiggs.child(1).pdgId() == 5:
                    mother_b1 = decaying_darkHiggs.child(1)
                    mother_b2 = decaying_darkHiggs.child(0)
                    decaying_b1 = DecayingParticle(mother_b1)
                    decaying_b2 = DecayingParticle(mother_b2)
                else:
                    logging.error("No dark Higgs decays found")
                    continue
        #########################
        # reconstruct kinematics
        #########################

        # reconstruct dark matter particles -> missing transverse momentum MET
        v_mother_chi1 = ROOT.TLorentzVector()
        v_mother_chi2 = ROOT.TLorentzVector()
        v_MET = ROOT.TLorentzVector()

        try:
            v_mother_chi1.SetPtEtaPhiE(
                mother_chi1.pt(), mother_chi1.eta(), mother_chi1.phi(), mother_chi1.e()
            )
            v_mother_chi2.SetPtEtaPhiE(
                mother_chi2.pt(), mother_chi2.eta(), mother_chi2.phi(), mother_chi2.e()
            )
            v_MET = v_mother_chi1 + v_mother_chi2
        except AttributeError:
            n_events_nozprime += 1

        # reconstruct dark Higgs
        v_mother_b1 = ROOT.TLorentzVector()
        v_mother_b2 = ROOT.TLorentzVector()

        v_mother_b1.SetPtEtaPhiE(
            mother_b1.pt(), mother_b1.eta(), mother_b1.phi(), mother_b1.e()
        )
        v_mother_b2.SetPtEtaPhiE(
            mother_b2.pt(), mother_b2.eta(), mother_b2.phi(), mother_b2.e()
        )
        v_darkHiggs = ROOT.TLorentzVector()
        v_darkHiggs = v_mother_b1 + v_mother_b2


        #########################
        # fill histograms
        #########################

        # fill Histograms with appropriate weights for reweighting
        for wtsuffix in weight_to_run:
            histset["mDH" + wtsuffix].Fill(v_darkHiggs.M() / 1000.0, wt[wtsuffix])
            histset["ptDH" + wtsuffix].Fill(v_darkHiggs.Pt() / 1000.0, wt[wtsuffix])
            histset["ptb1" + wtsuffix].Fill(v_mother_b1.Pt() / 1000.0, wt[wtsuffix])
            histset["ptb2" + wtsuffix].Fill(v_mother_b2.Pt() / 1000.0, wt[wtsuffix])
            histset["met" + wtsuffix].Fill(v_MET.Pt() / 1000.0, wt[wtsuffix])

    ############################
    # write histograms to file
    ############################
    dsid = getDSID(args.input)
    histfile = ROOT.TFile(args.output + '_dsid{dsid}'.format(dsid=dsid) + ".root", "RECREATE")
    histfile.cd()
    for key in histset.keys():
        histset[key].Write()
    histfile.Close()

    if n_events_nozprime > 0:
        logging.warning('No Zprime boson found in {n} events! Setting MET in those events to zero.'.format(n=n_events_nozprime))


if __name__ == "__main__":
    main()
