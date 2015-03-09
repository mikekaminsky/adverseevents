import json
import urllib2
import pandas as pd
from pprint import pprint

# Idea: can i predict label changes?

# Idea -- link the FAERS data to stock prices. Are 
# funds using these data to predict recalls?
# Can i work backwards to detect how the fund models are doing?
# Can i do better?

def base_path(type):
    return("https://api.enigma.io/v2/" + type + "/707e9a59091579c077c86004d2e4039a/")

meta_path = base_path('meta') + "us.gov.fda.aers"
meta_json = json.load(urllib2.urlopen(meta_path))

for meta in meta_json['result']['children_tables']:
    datapath = meta['datapath']
    name = meta['db_boundary_label']
    print name
    print datapath

demo_current = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.demo.current"))['result'])
demo_historical = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.demo.historical"))['result'])

drug_current = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.drug.current"))['result'])
drug_historical = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.drug.historical"))['result'])

ther_current = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.ther.current"))['result'])
ther_historical = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.ther.historical"))['result'])

reac_current = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.reac.current"))['result'])
reac_historical = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.reac.historical"))['result'])

outc_current = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.outc.current"))['result'])
outc_historical = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.outc.historical"))['result'])

indi_current = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.indi.current"))['result'])
indi_historical = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.indi.historical"))['result'])

rpsr_current = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.rpsr.current"))['result'])
rpsr_historical = pd.DataFrame(json.load(urllib2.urlopen(base_path('data') + "us.gov.fda.aers.rpsr.historical"))['result'])



#1. DEMOyyQq.TXT contains patient demographic and administrative information, a single record for each event report.

#2. DRUGyyQq.TXT contains drug/biologic information for as many medications as were reported for the event (1 or more per event).

#3. REACyyQq.TXT contains all "Medical Dictionary for Regulatory Activities" (MedDRA) terms coded for the event (1 or more). For more information on MedDRA, please contact: TRW, VAR 1/6A/MSSO, 12011 Sunset Hills Road, Reston, VA 20190-3285, USA; website is www.meddramsso.com

#4. OUTCyyQq.TXT contains patient outcomes for the event (0 or more).

#5. RPSRyyQq.TXT contains report sources for event (0 or more).

#6. THERyyQq.TXT contains drug therapy start dates and end dates for the reported drugs (0 or more per drug per event).

#7. INDIyyQq.TXT contains all "Medical Dictionary for Regulatory Activities" (MedDRA) terms coded for the indications for use (diagnoses) for the reported drugs (0 or more per drug per event).
