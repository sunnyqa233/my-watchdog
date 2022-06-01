# my-watchdog
## What can this thing do?
* Send you warning message through discord
* Monitor RAM usage
* Monitor swap usage
* Monitor disk usage
* Monitor disk temperature
* Monitor & restart specific process(TODO)

## Install running environment
### Install python3
```bash
sudo apt install python3-pip
sudo apt install smartmontools
```
### Install python package
```commandline
pip3 install rich
pip3 install psutil
pip3 install discord-webhook
pip3 install pySMART
```

## Settings
### Run config tool
```commandline
python3 config-tool.py
```
### Run the script regularly
You may execute main.py every five minutes. It depends on you.
