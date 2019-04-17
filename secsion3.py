import requests
import json
from tabulate import *
from my_apic_em_functions2 import *
requests.packages.urllib3.disable_warnings()


if __name__ == "__main__":
    print_hosts()
    print_devices() 
while True:
    s_ip = input("prompt string: ")
    d_ip = input("prompt string: ")
    if s_ip != "" or d_ip != "":
        path_data = {
            "sourceIP": s_ip,
            "destIP": d_ip
        }
        print("Source IP address is: ",       path_data["sourceIP"])
        print("Destination IP address is: ",  path_data["destIP"])
        break
    else:
        print("\n YOU MUST ENTER IP ADDRESSES TO CONTINUE.\nUSE CTRL-C TO QUIT\n")

        

        
    

    
    
