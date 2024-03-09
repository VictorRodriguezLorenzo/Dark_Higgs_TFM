variables = {}

variables['events']  = {   
    'name': '1',
    'range' : (1,0,2),
    'xaxis' : 'events',
    'fold' : 3
}


variables['mll']  = {   'name': 'mll',
                        'range' : (40, 20, 320),
                        'xaxis' : 'm_{ll} [GeV]',
                        'fold' : 3
                        }



variables['drll']  = {   'name': 'drll',
                         'range' : (30, 0, 2.5),
                        'xaxis' : 'dr_{ll} [GeV]',
                        'fold' : 3
                        }


variables['mth']  = {   'name': 'mth',
                        'range' : (30, 20, 225),
                        'xaxis' : 'm_{T}^{ll+MET} [GeV]',
                        'fold' : 3
                        }

variables['ptll']  = {   'name': 'ptll',
                        'range' : (30, 30,120),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 3
                        }

variables['pt1']  = {   'name': 'Lepton_pt[0]',
                        'range' : (30,25,225),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3
                        }

variables['pt2']  = {   'name': 'Lepton_pt[1]',
                        'range' : (30,20,125),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3
                        }


variables['eta1']  = {   'name': 'Lepton_eta[0]',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3
                        }

variables['eta2']  = {  'name': 'Lepton_eta[1]',
                        'range' : (30,-3,3),
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3
                        }

variables['puppimet']  = {'name': 'PuppiMET_pt',
                        'range' : (30,20,300),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }

variables['mpmet']  = { 'name': 'mpmet',
                        'range' : (30,20,200),
                        'xaxis' : 'mpmet [GeV]',
                        'fold'  : 3
                        }

variables['dphill']  = { 'name': 'abs(dphill)',
                        'range' : (30,0,3.14),
                        'xaxis' : '#Delta#phi_{ll}',
                        'fold' : 3
                        }
variables['njets']  = { 'name': 'njets',
                        'range' : (4,0,6),
                        'xaxis' : 'N jets',
                        'fold' : 3
                        }
variables['nbjets']  = { 'name': 'nbjets',
                        'range' : (4,0,3),
                        'xaxis' : 'N b jets',
                        'fold' : 3
                        }

variables['btag_ID']  = { 'name': 'btag_ID',
                        'range' : (30,0,1),
                        'xaxis' : 'b tag',
                        'fold' : 3
                        }
