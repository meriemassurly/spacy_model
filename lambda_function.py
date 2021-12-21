import json
import os
import sys
sys.path.append("/mnt/access")

import joblib

def lambda_handler(event, context):
    
    #print(np.zeros(3))
    
    
    #print("Before : ",os.listdir("/mnt/access"))
    
    
    #with open("/mnt/access/file.txt","w") as f:
        #f.write("Hello, from lambda")
        
    #print("After :",os.listdir("/mnt/access"))
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
