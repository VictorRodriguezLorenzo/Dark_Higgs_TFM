from collections import OrderedDict
samples = [('top', ['/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7/nanoLatino_TTTo2L2Nu__part54.root'], '( XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC ) * ( (Top_pTrw) )', 258, False)]
aliases = OrderedDict([('LepWPCut', {'expr': 'LepCut2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs', 'DATA']}), ('LepWPSF', {'expr': 'LepSF2l__ele_mvaFall17V1Iso_WP90__mu_cut_Tight_HWWW', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('gstarLow', {'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4', 'samples': 'VgS'}), ('gstarHigh', {'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4', 'samples': 'VgS'}), ('zeroJet', {'expr': 'Alt(CleanJet_pt,0, 0) < 30.'}), ('oneJet', {'expr': 'Alt(CleanJet_pt, 0, 0) > 30.'}), ('multiJet', {'expr': 'Alt(CleanJet_pt, 1, 0) > 30.'}), ('btag_ID', {'expr': 'Jet_btagDeepB'}), ('bVeto', {'expr': 'Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB, CleanJet_jetIdx) > 0.1241) == 0'}), ('bReq', {'expr': 'Sum(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepB, CleanJet_jetIdx) > 0.1241) >= 1'}), ('topcr', {'expr': 'mth>40 && PuppiMET_pt>20 && mll > 12 && ((zeroJet && !bVeto) || bReq)'}), ('bVetoSF', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSF', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSF', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('JetPUID_SF', {'expr': 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose)))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFjesup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_jes, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFjesdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_jes, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFjesup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_jes, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFjesdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_jes, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFjesup', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFjesup + (topcr && !zeroJet)*bReqSFjesup', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFjesdown', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFjesdown + (topcr && !zeroJet)*bReqSFjesdown', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFlfup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lf, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFlfdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lf, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFlfup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lf, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFlfdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lf, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFlfup', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfup + (topcr && !zeroJet)*bReqSFlfup', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFlfdown', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfdown + (topcr && !zeroJet)*bReqSFlfdown', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFhfup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hf, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFhfdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hf, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFhfup', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hf, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFhfdown', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hf, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFhfup', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfup + (topcr && !zeroJet)*bReqSFhfup', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFhfdown', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfdown + (topcr && !zeroJet)*bReqSFhfdown', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFlfstats1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFlfstats1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFlfstats1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFlfstats1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFlfstats1up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfstats1up + (topcr && !zeroJet)*bReqSFlfstats1up', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFlfstats1down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfstats1down + (topcr && !zeroJet)*bReqSFlfstats1down', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFlfstats2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFlfstats2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFlfstats2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_lfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFlfstats2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_lfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFlfstats2up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfstats2up + (topcr && !zeroJet)*bReqSFlfstats2up', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFlfstats2down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFlfstats2down + (topcr && !zeroJet)*bReqSFlfstats2down', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFhfstats1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFhfstats1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFhfstats1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFhfstats1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hfstats1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFhfstats1up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfstats1up + (topcr && !zeroJet)*bReqSFhfstats1up', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFhfstats1down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfstats1down + (topcr && !zeroJet)*bReqSFhfstats1down', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFhfstats2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFhfstats2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFhfstats2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_hfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFhfstats2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_hfstats2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFhfstats2up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfstats2up + (topcr && !zeroJet)*bReqSFhfstats2up', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFhfstats2down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFhfstats2down + (topcr && !zeroJet)*bReqSFhfstats2down', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFcferr1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_cferr1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFcferr1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_cferr1, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFcferr1up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_cferr1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFcferr1down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_cferr1, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFcferr1up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFcferr1up + (topcr && !zeroJet)*bReqSFcferr1up', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFcferr1down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFcferr1down + (topcr && !zeroJet)*bReqSFcferr1down', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFcferr2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_cferr2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bVetoSFcferr2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_cferr2, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFcferr2up', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_up_cferr2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('bReqSFcferr2down', {'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_deepcsv_shape_down_cferr2, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFcferr2up', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFcferr2up + (topcr && !zeroJet)*bReqSFcferr2up', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('btagSFcferr2down', {'expr': '(bVeto || (topcr && zeroJet))*bVetoSFcferr2down + (topcr && !zeroJet)*bReqSFcferr2down', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('fakeW', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW', 'samples': ['Fake']}), ('fakeWEleUp', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_EleUp', 'samples': ['Fake']}), ('fakeWEleDown', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_EleDown', 'samples': ['Fake']}), ('fakeWMuUp', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_MuUp', 'samples': ['Fake']}), ('fakeWMuDown', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_MuDown', 'samples': ['Fake']}), ('fakeWStatEleUp', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_statEleUp', 'samples': ['Fake']}), ('fakeWStatEleDown', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_statEleDown', 'samples': ['Fake']}), ('fakeWStatMuUp', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_statMuUp', 'samples': ['Fake']}), ('fakeWStatMuDown', {'expr': 'fakeW2l_ele_mvaFall17V1Iso_WP90_mu_cut_Tight_HWWW_statMuDown', 'samples': ['Fake']}), ('PromptGenLepMatch2l', {'expr': 'Alt(Lepton_promptgenmatched,0,0)*Alt(Lepton_promptgenmatched,1,0)', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('Top_pTrw', {'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)', 'samples': ['top']}), ('nCleanGenJet', {'linesToAdd': ['.L /afs/cern.ch/user/v/victorr/private/WWcontrol_region/tt/ngenjet.cc+'], 'class': 'CountGenJet', 'args': 'nLeptonGen, LeptonGen_isPrompt, LeptonGen_pdgId, LeptonGen_pt, LeptonGen_eta, LeptonGen_phi, LeptonGen_mass, nPhotonGen, PhotonGen_pt, PhotonGen_eta,PhotonGen_phi, PhotonGen_mass, nGenJet, GenJet_pt, GenJet_eta, GenJet_phi', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('getGenZpt_OTF', {'linesToAdd': ['.L /afs/cern.ch/user/v/victorr/private/WWcontrol_region/tt/getGenZpt.cc+'], 'class': 'getGenZpt', 'args': 'nGenPart, GenPart_pt, GenPart_pdgId, GenPart_genPartIdxMother, GenPart_statusFlags, gen_ptll', 'samples': ['DY']}), ('DY_NLO_pTllrw', {'expr': '(1.037822324341*((0.232707489797*TMath::Erf((getGenZpt_OTF-5.49247649598)/5.14236049539)-0.00453696373368*getGenZpt_OTF+7.45078183646e-05*getGenZpt_OTF*getGenZpt_OTF-(0.232707489797*TMath::Erf((40.0-5.49247649598)/5.14236049539)-0.00453696373368*40.0+7.45078183646e-05*40.0*40.0)+1.06118030177)*(getGenZpt_OTF<40.0)+1.06118030177*(getGenZpt_OTF>=40.0)))*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)', 'samples': ['DY']}), ('DY_LO_pTllrw', {'expr': '(1.038916491841*((0.0948703608054*TMath::Erf((getGenZpt_OTF-5.47228332651)/2.2133221824)+0.00959307355966*getGenZpt_OTF-1.67661013599e-06*getGenZpt_OTF*getGenZpt_OTF-(0.0948703608054*TMath::Erf((40.0-5.47228332651)/2.2133221824)+0.00959307355966*40.0-1.67661013599e-06*40.0*40.0)+1.22775815139)*(getGenZpt_OTF<40.0)+1.22775815139*(getGenZpt_OTF>=40.0)))*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)', 'samples': ['DY']}), ('SFweight', {'expr': 'SFweight2l * LepWPCut * LepWPSF * btagSF * JetPUID_SF', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('SFweightEleUp', {'expr': 'LepSF2l__ele_mvaFall17V1Iso_WP90__Up', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('SFweightEleDown', {'expr': 'LepSF2l__ele_mvaFall17V1Iso_WP90__Do', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('SFweightMuUp', {'expr': 'LepSF2l__mu_cut_Tight_HWWW__Up', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']}), ('SFweightMuDown', {'expr': 'LepSF2l__mu_cut_Tight_HWWW__Do', 'samples': ['DY', 'top', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS', 'VZ', 'VVV', 'Higgs']})])
variables = {'events': {'name': '1', 'range': (1, 0, 2), 'xaxis': 'events', 'fold': 3}, 'mll': {'name': 'mll', 'range': (40, 20, 320), 'xaxis': 'm_{ll} [GeV]', 'fold': 3}, 'drll': {'name': 'drll', 'range': (30, 2.5, 5), 'xaxis': 'dr_{ll} [GeV]', 'fold': 3}, 'mth': {'name': 'mth', 'range': (30, 20, 225), 'xaxis': 'm_{T}^{ll+MET} [GeV]', 'fold': 3}, 'ptll': {'name': 'ptll', 'range': (30, 30, 120), 'xaxis': 'p_{T}^{ll} [GeV]', 'fold': 3}, 'pt1': {'name': 'Lepton_pt[0]', 'range': (30, 25, 225), 'xaxis': 'p_{T} 1st lep', 'fold': 3}, 'pt2': {'name': 'Lepton_pt[1]', 'range': (30, 20, 125), 'xaxis': 'p_{T} 2nd lep', 'fold': 3}, 'eta1': {'name': 'Lepton_eta[0]', 'range': (30, -3, 3), 'xaxis': '#eta 1st lep', 'fold': 3}, 'eta2': {'name': 'Lepton_eta[1]', 'range': (30, -3, 3), 'xaxis': '#eta 2nd lep', 'fold': 3}, 'puppimet': {'name': 'PuppiMET_pt', 'range': (30, 20, 300), 'xaxis': 'puppimet [GeV]', 'fold': 3}, 'mpmet': {'name': 'mpmet', 'range': (30, 20, 200), 'xaxis': 'mpmet [GeV]', 'fold': 3}, 'dphill': {'name': 'abs(dphill)', 'range': (30, 0, 3.14), 'xaxis': '#Delta#phi_{ll}', 'fold': 3}, 'btag_ID': {'name': 'btag_ID', 'range': (30, 0, 1), 'xaxis': 'b tag', 'fold': 3}}
cuts = {'cuts': {'tt_cr_': {'expr': 'Lepton_pt[1] > 20.', 'categories': {'allcuts': 'PuppiMET_pt >20 && mpmet > 20. && ptll>30 && mll>20 && Alt(Lepton_pt,2, 0) < 10. && mth>50 && bReq'}}}, 'preselections': 'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 && Lepton_pt[0] > 25.'}
plot = {'plot': {'DY': {'color': 418, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'Fake': {'color': 921, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'top': {'nameHR': 't#bar{t}', 'color': 400, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'WW': {'color': 851, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'ggWW': {'color': 850, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'WWewk': {'color': 851, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'Vg': {'color': 859, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'VgS': {'color': 617, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'VZ': {'color': 858, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'Higgs': {'color': 632, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'VVV': {'color': 800, 'isSignal': 0, 'isData': 0, 'scale': 1.0}, 'DATA': {'nameHR': 'Data', 'color': 1, 'isSignal': 0, 'isData': 1, 'isBlind': 0}}, 'groupPlot': {'Fake': {'nameHR': 'nonprompt', 'isSignal': 0, 'color': 921, 'samples': ['Fake']}, 'VZ': {'nameHR': 'VZ', 'isSignal': 0, 'color': 617, 'samples': ['VZ']}, 'WW': {'nameHR': 'WW', 'isSignal': 0, 'color': 851, 'samples': ['WW', 'ggWW', 'WWewk']}, 'VgS': {'nameHR': 'V#gamma', 'isSignal': 0, 'color': 400, 'samples': ['VgS']}, 'top': {'nameHR': 't#bar{t}', 'isSignal': 0, 'color': 400, 'samples': ['top']}, 'DY': {'nameHR': 'DY', 'isSignal': 0, 'color': 418, 'samples': ['DY']}, 'Higgs': {'nameHR': 'Higgs', 'isSignal': 0, 'color': 632, 'samples': ['Higgs']}, 'VVV': {'nameHR': 'VVV', 'isSignal': 0, 'color': 800, 'samples': ['VVV']}}, 'legend': {'lumi': 'L = 59.74/fb', 'sqrt': '#sqrt{s} = 13 TeV'}}
nuisances = {'lumi': {'name': 'lumi_13TeV_2018', 'type': 'lnN', 'samples': {'WWewk': '1.025', 'ggWW': '1.025', 'Vg': '1.025', 'VgS': '1.025', 'VZ': '1.025', 'VVV': '1.025', 'Higgs': '1.025'}}, 'stat': {'type': 'auto', 'maxPoiss': '10', 'includeSignal': '0', 'samples': {}}}
structure = {'DY': {'isSignal': 0, 'isData': 0}, 'Fake': {'isSignal': 0, 'isData': 0}, 'top': {'isSignal': 0, 'isData': 0}, 'WW': {'isSignal': 0, 'isData': 0}, 'WWewk': {'isSignal': 0, 'isData': 0}, 'ggWW': {'isSignal': 0, 'isData': 0}, 'Vg': {'isSignal': 0, 'isData': 0}, 'VgS': {'isSignal': 0, 'isData': 0}, 'VZ': {'isSignal': 0, 'isData': 0}, 'VVV': {'isSignal': 0, 'isData': 0}, 'Higgs': {'isSignal': 0, 'isData': 0}, 'DATA': {'isSignal': 0, 'isData': 1}}
lumi = 59.8