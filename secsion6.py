import requests
import json
from tabulate import *
from my_apic_em_functions2 import *
requests.packages.urllib3.disable_warnings()

path_source = response_json["response"]["request"]["sourceIP"]
path_dest = response_json["response"]["request"]["destIP"]
networkElementsInfo = response_json["response"]["networkElementsInfo"]
all_devices = []  
device_no = 1  
for networkElement in networkElementsInfo: 
    if "name" not in networkElement:  
        name = "Unnamed Host"
        ip = networkElement["ip"]
        egressInterfaceName = "UNKNOWN"
        ingressInterfaceName = "UNKNOWN" 
    else: 
        name = networkElement["name"]
        ip = networkElement["ip"]
        if "egressInterface" in networkElement:  
            egressInterfaceName = networkElement["egressInterface"]["physicalInterface"]["name"]
        else:
            egressInterfaceName = "UNKNOWN"

        if "ingressInterface" in networkElement:
            ingressInterfaceName = networkElement["ingressInterface"]["physicalInterface"]["name"]
        else:
            ingressInterfaceName = "UNKNOWN"
    device = [device_no, name, ip, ingressInterfaceName, egressInterfaceName]
    all_devices.append(device)
    device_no += 1
print("Path trace: \n Source: ", path_source, "\n Destination: ", path_dest)  
print("List of devices on path:")
table_header = ["Item", "Name", "IP", "Ingress Int", "Egress Int"]
print( tabulate(all_devices, table_header) )  
