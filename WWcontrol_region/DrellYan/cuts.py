# cuts

cuts = {}


_tmp = [
    'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    'Lepton_pt[0] > 25.',
     ]

preselections = ' && '.join(_tmp)

cuts['DY_cr_'] = {
    'expr': 'Lepton_pt[1] > 20.',
    'categories' : {
#        '1cut' : 'PuppiMET_pt >20',
#        '2cuts' : 'PuppiMET_pt >20 && mpmet > 20.',
#        '3cuts' : 'PuppiMET_pt >20 && mpmet > 20. && ptll<30',
#        '4cuts' : 'PuppiMET_pt >20  && mpmet > 20. && ptll<30 && mll<80',
#        '5cuts' : 'PuppiMET_pt >20 && mpmet > 20. && ptll<30 && mll<80 && Alt(Lepton_pt,2, 0) < 10.',
#        '6cuts' : 'PuppiMET_pt >20 && mpmet > 20. && ptll<30 && mll<80 && Alt(Lepton_pt,2, 0) < 10. && bVeto',
        'allcuts-0jet' : 'PuppiMET_pt >20 && mpmet > 20. && ptll<30 && mll<80 && Alt(Lepton_pt,2, 0) < 10. && bVeto && zeroJet',
        'allcuts-1jet' : 'PuppiMET_pt >20 && mpmet > 20. && ptll<30 && mll<80 && Alt(Lepton_pt,2, 0) < 10. && mth>50 && bVeto && oneJet',
    }
}

