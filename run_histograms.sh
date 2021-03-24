#!/bin/bash

# dark Higgs 50 GeV nominal + reweighted samples (starting from gx=1.0)
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/110000/DAOD_TRUTH1.mc16_13TeV.110000.110817.root

# dark Higgs 50 GeV nominal + reweighted samples (starting from gx=2.0)
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/110002/DAOD_TRUTH1.mc16_13TeV.110002.493613.root

# dark Higgs 50 GeV nominal + reweighted samples (starting from gx=3.0)
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/110004/DAOD_TRUTH1.mc16_13TeV.110004.411357.root



# dark Higgs 90 GeV nominal + reweighted samples (starting from gx=1.0)
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/110010/DAOD_TRUTH1.mc16_13TeV.110010.219897.root

# # dark Higgs 90 GeV nominal + reweighted samples (starting from gx=2.0)
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/110012/DAOD_TRUTH1.mc16_13TeV.110012.412482.root

# # dark Higgs 90 GeV nominal + reweighted samples (starting from gx=3.0)
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/110014/DAOD_TRUTH1.mc16_13TeV.110014.480462.root



# # nominal samples for validation
# - m=50 GeV, gx 0p1
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111000/DAOD_TRUTH1.mc16_13TeV.111000.422036.root --weights nominal

# - m=50 GeV, gx 0p3
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111001/DAOD_TRUTH1.mc16_13TeV.111001.163400.root --weights nominal

# - m=50 GeV, gx 0p5
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111002/DAOD_TRUTH1.mc16_13TeV.111002.102810.root --weights nominal

# - m=50 GeV, gx 0p7
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111003/DAOD_TRUTH1.mc16_13TeV.111003.480164.root --weights nominal

# - m=50 GeV, gx 1p0
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111004/DAOD_TRUTH1.mc16_13TeV.111004.457222.root --weights nominal

# - m=50 GeV, gx 1p3
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111005/DAOD_TRUTH1.mc16_13TeV.111005.496067.root --weights nominal

# # - m=50 GeV, gx 1p7
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111006/DAOD_TRUTH1.mc16_13TeV.111006.416871.root --weights nominal

# # - m=50 GeV, gx 2p0
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111007/DAOD_TRUTH1.mc16_13TeV.111007.226957.root --weights nominal

# # - m=50 GeV, gx 2p3
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111008/DAOD_TRUTH1.mc16_13TeV.111008.403713.root --weights nominal

# # - m=50 GeV, gx 2p7
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111009/DAOD_TRUTH1.mc16_13TeV.111009.464784.root --weights nominal


# - m=90 GeV, gx 0p1
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111010/DAOD_TRUTH1.mc16_13TeV.111010.344967.root --weights nominal

# - m=90 GeV, gx 0p3
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111011/DAOD_TRUTH1.mc16_13TeV.111011.315856.root --weights nominal

# - m=90 GeV, gx 0p5
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111012/DAOD_TRUTH1.mc16_13TeV.111012.145892.root --weights nominal

# - m=90 GeV, gx 0p7
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111013/DAOD_TRUTH1.mc16_13TeV.111013.315990.root --weights nominal

# - m=90 GeV, gx 1p0
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111014/DAOD_TRUTH1.mc16_13TeV.111014.333967.root --weights nominal

# - m=90 GeV, gx 1p3
python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111015/DAOD_TRUTH1.mc16_13TeV.111015.324710.root --weights nominal

# # - m=90 GeV, gx 1p7
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111016/DAOD_TRUTH1.mc16_13TeV.111016.415782.root --weights nominal

# # - m=90 GeV, gx 2p0
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111017/DAOD_TRUTH1.mc16_13TeV.111017.165242.root --weights nominal

# # - m=90 GeV, gx 2p3
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111018/DAOD_TRUTH1.mc16_13TeV.111018.241787.root --weights nominal

# # - m=90 GeV, gx 2p7
# python DAODreader.py /nfs/dust/atlas/user/pgadow/MC/TRUTH/111019/DAOD_TRUTH1.mc16_13TeV.111019.378631.root --weights nominal

