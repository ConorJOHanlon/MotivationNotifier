import time 
from plyer import notification 
import json
import os
import sys
import random

if __name__=="__main__":
    here = os.path.dirname(os.path.normpath(__file__))
    filename = os.path.join(here, 'quotes.json')
    with open(filename,  encoding="utf8") as json_file:
        data = json.load(json_file)
        r = random.randint(0,len(data))
        title = data[r]['from']
        message = data[r]['text']
        notification.notify( 
                title = title, 
                message= message, 
                
                # displaying time 
                timeout=10 
        ) 
        # waiting time 
        time.sleep(10)