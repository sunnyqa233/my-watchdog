from discord import send_message
from config import ServiceList
import psutil
import os

"""
Get existing processes
"""
ProcessList = []
for pid in psutil.pids():
    try:
        process_object = psutil.Process(pid)
        process_name = process_object.name()
        process_bin = process_object.exe()
        # Ensures no blank string
        if not (process_name and process_bin):
            raise ValueError
    except:
        pass
    else:
        ProcessList.append(
            {
                "name": process_name,
                "bin": process_bin
            }
        )


"""
Check items in Service List
"""
for item in ServiceList:
    found = False
    # Try to find process
    for process in ProcessList:
        if (process["name"] == item["name"]) and (process["bin"] == item["bin"]):
            found = True
            break
    # See if restart is needed
    if not found:
        os.system(item["restart_cmd"])
        send_message(item["message"])
