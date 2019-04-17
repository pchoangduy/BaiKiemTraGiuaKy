import requests
import json
import time
from my_apic_em_functions2 import *
from tabulate import *
requests.packages.urllib3.disable_warnings()
    
path = json.dumps(path_data)
resp = requests.post(api_url, path, headers=headers, verify=False)
resp_json = resp.json()
flowAnalysisId = resp_json["response"]["flowAnalysisId"]
print("FLOW ANALYSIS ID: ", flowAnalysisId)

        
