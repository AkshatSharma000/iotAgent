# iotAgent
This is the python application used in iot device to collect data from the device and populate the data to the api server.

It populates the data in real time with an JSON schema.
It refresh the status in every 10 sec.

## Working
 - First it will check weather the data already been posted on API or data related to the device already beeen there.
 - If it is not there it will make a POST request on API and post the data.
 - So,to update the status it will make a PUT request to update the required device's status.
This is the working of this application.

JSON Schema:

```sh
{
  "userID": "username",
  "deviceID": "device Id",
  "uptime": device uptime,
  "cpu_usage": cpu usage,
  "memory_usage": "8Gb/4Gb/16Gb",
  "disk_partitions_usage": "/dev/nvme0n1p6  290G   76G  200G  28% /"
}
```

## KeyPoints
    cpu_usage is like 50%

    memory usage is 4gb/16b 

    disk_partitions is a list - its just output of df command in linux.
    /dev/nvme0n1p6  290G   76G  200G  28% /
    /dev/nvme0n1p1  296M   31M  266M  11% /boot/ef
