
# All lipids available for C36mFF as of 6/12/2026
STD_LIPIDS = ("DAPC", "DLPA", "DLPC", "DLPE","DLPG",
              "DLPS","DMPA","DMPC","DMPE","DMPG",
              "DMPS","DOPA","DOPC","DOPE","DOPG",
              "DOPS","DPPA","DPPC","DPPE","DPPG",
              "DPPS","DSPA","DSPC","DSPE","DSPG",
              "DSPS","LPPC","POPA","POPC","POPE",
              "POPG","POPS","SAPC","SDPC","SOPC")

SM_LIPIDS = ("23SM","ASM","BSM","CER1","CER160",
             "CER180","CER181","CER2","CER200","CER220",
             "CER240","CER241","CER3","CER3E","CER6",
             "DSM","LSM","NSM","OSM","PSM",
             "SSM","TSM")

ARCHEAL_LIPIDS = ("ARCL2","AROL","DGT1","MEN7","MEN8",
                  "MEN9", "MKOL8", "PEAR", "PGAR", "PGMAR",
                  "UQ1","UQ10", "UQ2","UQ3","UQ4",
                  "UQ5","UQ6","UQ7","UQ8","UQ9",
                  "UQOL1", 'UQOL10','UQOL2','UQOL3','UQOL4',
                  'UQOL5','UQOL6','UQOL7','UQOL8','UQOL9')

BACTERIAL_LIPIDS = ('AIPC','AIPE','AIPG','APPC','DPPGK',
                    'IPPC','MAIPC','MAIPE','MAIPG','OOPG',
                    'OYPE','PAICL2','PAIPC','PAIPE','PAIPG',
                    'PHPC','PMPE','PMPG','PPPE','PVCL2',
                    'PVPE','PVPG','PYPG','QMPE','YLIPG',
                    'YPPG')

CARDIOLIPIN = ('LNACL1','LNACL2','LNBCL1','LNBCL2','LNCCL1',
               'LNCCL2','LNDCL1','LNDCL2','LOACL1','LOACL2',
               'LOCCL1','LOCCL2','PMCL1','PMCL2','POCL1',
               'POCL2','TLCL1','TLCL2','TMCL1','TMCL2',
               'TOCL1','TOCL2','TYCL1','TYCL2')

CHOLESTEROL = ('CAMP','CHL1','CHM1','CHNS','CHSD',
               'CHSP','ERG','GCAMP','GSITO','LANO',
               'PGCAMP','PGSITO','PGSTIG','SITO','STIG')

DAG_LIPIDS = ('DAGL','DEGL','DGGL','DIGL','DLGL',
              'DMGL','DNGL','DOGL','DSGL','DPGL',
              'DTGL','DYGL','LLGL','PLGL','POGL',
              'SAGL','SDGL','SLGL','SOGL','TIGL')

INOSITOL = ('DLIPI','DMPI','DMPI13','DMPI14','DMPI15',
            'DMPI24','DMPI25','DMPI2A','DMPI2B','DMPI2C',
            'DMPI2D','DMPI33','DMPI34','DMPI35','DPPI',
            'LINPI','PLPI','PLPI13','PLPI14','PLPI15',
            'PLPI24','PLPI25','PLPI2A','PLPI2B','PLPI2C',
            'PLPI2D','PLPI33','PLPI34','PLPI35','PNPI',
            'PNPI13','PNPI14','PNPI15','PNPI24','PNPI25',
            'PNPI2A','PNPI2B','PNPI2C','PNPI2D','PNPI33',
            'PNPI34','PNPI35','POPI','POPI13','POPI14',
            'POPI15','POPI24','POPI25','POPI2A','POPI2B',
            'POPI2C','POPI2D','POPI33','POPI34','POPI35',
            'PSPI','PYPI','SAPI','SAPI13','SAPI14',
            'SAPI15','SAPI24','SAPI25','SAPI2A','SAPI2B',
            'SAPI2C','SAPI2D','SAPI33','SAPI34','SAPI35',
            'SDPI','SLPI')

LPS = ('ABLIPA','ABLIPB','BCLIPA','BCLIPB','BCLIPC',
       'CJLIPA','CTLIPA','ECLIPA','ECLIPB','ECLIPC',
       'HPLIPA','HPLIPB','KPLIPA','KPLIPB','KPLIPC',
       'LILIPA','MCLIPA','NGLIPA','NGLIPB','NGLIPC',
       'PALIPA','PALIPB','PALIPC','PALIPD','PALIPE',
       'SELIPA','SELIPB','SELIPC','SFLIPA','VCLIPA',
       'VCLIPB','VCLIPC','VCLIPD','VCLIPE','YPLIPA',
       'YPLIPB','YPLIPC','YPLIPD')

MYCOBAC_LIPIDS = ('PIMA','PIMB','PIMC','PIMD','PIME')

MISC_LIPIDS = ('BMGP','DAPA','DAPE','DAPG','DAPS',
               'DCPC','DDOPC','DDOPE','DDOPS','DDPC',
               'DEPA','DEPC','DEPE','DEPG','DEPS',
               'DGPA','DGPC','DGPE','DGPG','DGPS',
               'DIPA','DLIPC','DLIPE','DNPA','DNPC',
               'DNPE','DNPG','DNPS','DOPP1','DOPP2',
               'DOPP3','DRPC','DTPA','DUPC','DXPC',
               'DXPE','DYPA','DYPG','DYPS','LLPA',
               'LLPC','LLPE','LLPG','LLPS','LYPG',
               'OEPC','OEPE','OEPS','OLPS','PAPA',
               'PAPC','PAPE','PAPG','PAPS','PDOPC',
               'PDOPE','PEPC','PEPE','PEPS','PILPC',
               'PLEPA','PLEPC','PLEPE','PLEPG','PLEPS',
               'PLPA','PLPC','PLPE','PLPG','PLPS',
               'POPP1','POPP2','POPP3','PSPA','PSPC',
               'PSPE','PSPG','PSPS','SAPA','SAPE',
               'SAPG','SAPS','SDPA','SDPE','SDPG',
               'SDPS','SEPPC','SLEPC','SLPA','SLPC',
               'SLPE','SLPG','SLPS','SODPC','SOPA',
               'SOPE','SOPG','SOPS','TIPA','TSPC')

TAG_LIPIDS = ('LLATG','LLGTG','LLLTG','LLNTG','LNNTG',
              'LOSTG','NNNTG','OLATG','OLGTG','OLLTG',
              'OLNTG','ONATG','ONNTG','OOLTG','OONTG',
              'OOOTG','OPOTG','PLATG','PLLTG','PLNTG',
              'PNNTG','POLTG','PONTG','POOTG','POSTG',
              'PPLTG','PPNTG','PPOTG','PPPTG','PSLTG',
              'PSOTG','SLATG','SLGTG','SLLTG','SLNTG',
              'SNGTG','SNLTG','SOLTG','SONTG','SOOTG',
              'SPOTG')

YEAST_LIPIDS = ('DYPC','DYPE','PYPE','PYPC','YOPA',
                'YOPC','YOPE','YOPS')

DETERGENTS = ('ADR','ADRP','ALIN','ALINP','ARA',
              'ARAN','ARANP','ARAP','BEH','BEHP',
              'C6DHPC','C7DHPC','CHAPS','CHAPSO','CTB10',
              'CTB11','CTB12','CTB13','CTB14','CTB15',
              'CTB16','CYFOS3','CYFOS4','CYFOS5','CYFOS6',
              'CYFOS7','DDA','DDAO','DDAOP','DDAP',
              'DDMG','DGLA','DGLAP','DHA','DHAP',
              'DOMG','DPA','DPAP','DPT','DPTP',
              'EDA','EDAP','EICO','EICOP','EPA',
              'EPAP','ERU','ERUP','ETA','ETAP',
              'ETE','ETEP','FOIS11','FOIS9','FOS10',
              'FOS12','FOS13','FOS14','FOS15','FOS16',
              'GLA','GLAP','GMS1','GMS2','HPA',
              'HPAP','HTA','HTAP','LAPAO','LAPAOP',
              'LAU','LAUP','LDAO','LDAOP','LIGN',
              'LIGNP','LIN','LINP','LMPG','LPC12',
              'LPC14','LPC16','LPPG','MEA','MEAP',
              'MLN1','MLN2','MYR','MYRO','MYROP',
              'MYRP','NER','NERP','OLE','OLEP',
              'PAL','PALO','PALOP','PALP','SB3-10',
              'SB3-12','SB3-14','SDA','SDAP','SDS',
              'STE','STEP','THA','THAP','THCHL',
              'THDPPC','TPA','TPAP','TPT','TPTP',
              'TRI','TRIP','TRIPAO','TRIPAOP','TTA',
              'TTAP','UDAO','UDAOP','UFOS10')

ETHER_LIPIDS = ('DHPCE','DMPCE','DMPEE','DOPCE','DOPEE',
                'DPPEE','PLA18','PLA20','PLC18','PLC20',
                'PLC22','POPCE','POPEE')

GLYCOLIPIDS = ('A2UDM','ABAC','ACY3G','ACY4M','ACY5M',
               'ACY6M','ACY7M','ADDG','ADDM','ADDTM',
               'ADG','ADM','ADMHM','ADTM','AHTG',
               'AMHCG','ANG','ANM','ANTM','AOG',
               'AOM','AOTG','AOTM','APPM','ATM',
               'AUDM','AUDTM','B2UDM','BBAC','BBCYG',
               'BBPHG','BCY3G','BCY3M','BCY4M','BCY5M',
               'BCY6M','BCY7M','BDDG','BDDM','BDDTM',
               'BDG','BDM','BDMHM','BDMNG','BMHCG',
               'BNG','BNM','BNTM','BOG','BOGNG',
               'BOING','BOM','BOTG','BOTGNG','BOTM',
               'BPPM','BTM','BUDM','BUDTM','C10EG5',
               'C10EG6','C10EG9','C12DEG','C12EG7','C12EG8',
               'C12EG9','C13EG8','C5MNG','C6EG3','C6EG4',
               'C6EG5','C6MNG','C7EG4','C7EG5','C8EG4',
               'C8EG5','C8EG6','DHEG','DL16PP','DL19PP',
               'DMG','EGTM10','EGTM11','MGTM10','MGTM11',
               'NHEG','NIDP40','NMG','SMDD','TX100',
               'TX114','TX305','TX405','TZME10','TZME9',
               'TZMH10','TZMH9','UNDPP')