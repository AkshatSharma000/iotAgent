import requests
from random import choice
import time

randlist = [i for i in range(0, 100)]

response = requests.get('http://127.0.0.1:8000/Akshat/')
ans = response.status_code

if(ans != 200):
    url = 'http://127.0.0.1:8000/'
    payload = {
            "userID": "Akshat",
            "deviceID": "Test1",
            "uptime": 20,
            "cpu_usage": 70,
            "memory_usage": "8Gb",
            "disk_partitions_usage": "/dev/nvme0n1p6  290G   76G  200G  28% /"
        }
    response = requests.post(url,data=payload)

while 1:
    url1 = 'http://127.0.0.1:8000/Akshat/'
    x = choice(randlist)
    y = choice(randlist)
    payload = {
        "userID":"Akshat",
        "deviceID": "Test1",
        "uptime": x,
        "cpu_usage": y,
        "memory_usage": "8Gb",
        "disk_partitions_usage": "/dev/nvme0n1p6  290G   76G  200G  28% /"
    }
    response = requests.put(url1,data=payload)
    print(response.status_code)
    time.sleep(10)
