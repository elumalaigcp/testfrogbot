import requests
import json
import os
import sys
import pandas as pd

cars = {'Brand': ['Honda Accord','BMW Z4','Nissan Skyline','Audi R8'],
        'Price': [22000,25000,27000,35000,40000]
        }

df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

print(df)
sys.exit(0)

DB_PASSWORD = "password123"
ACCESS_TOKEN = "ghp_abc123thisisonlyfortesting"
