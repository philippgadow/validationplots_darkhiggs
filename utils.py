#!/usr/bin/env python


def readxAOD(fname, treename="CollectionTree"):
    # set up ROOT and RootCore:
    import ROOT
    ROOT.gROOT.Macro( '$ROOTCOREDIR/scripts/load_packages.C' )
    # initialize the xAOD infrastructure
    ROOT.xAOD.Init().ignore()

    # get tree
    f = ROOT.TFile.Open(fname)
    t = ROOT.xAOD.MakeTransientTree( f, treename) # Make the "transient tree"

    # Print some information:
    print( "Number of input events: %s" % t.GetEntries() )
    return t


def getDSID(f):
    import re
    try:
        found = re.search('mc16_13TeV\.(.+?)\.', f).group(1)
    except AttributeError:
        found = ''
    return found

# To find the last decay chain's particles from the mother particle
def DecayingParticle(tp):
    PDG = tp.pdgId()
    #print "Particle ", PDG, "nChildren is: ", tp.nChildren()
    for chIdx in xrange (tp.nChildren()):
	#print "Children's PDG id is:", tp.child(chIdx).pdgId()
        if (tp.child(chIdx)==None):
            continue
        if (tp.child(chIdx).pdgId() == PDG):
            return DecayingParticle(tp.child(chIdx))
    return tp

