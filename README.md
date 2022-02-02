# iotAgent
This is the python application used in iot device to collect data from the device and populate the data to the api server.
It populates the data in real time with an JSON schema.

JSON Schema:

```sh
{
  "userID": "Akshat",
  "deviceID": "Test1",
  "uptime": 20,
  "cpu_usage": 70,
  "memory_usage": "8Gb",
  "disk_partitions_usage": "/dev/nvme0n1p6  290G   76G  200G  28% /"
}
```

## KeyPoints
    cpu_usage is like 50%

    memory usage is 4gb/16b 

    disk_partitions is a list - its just output of df command in linux.
    /dev/nvme0n1p6  290G   76G  200G  28% /
    /dev/nvme0n1p1  296M   31M  266M  11% /boot/ef
