# my-watchdog
## What can this thing do?
* Send you warning message through discord
* Monitor RAM usage(Warning at 90%)
* Monitor disk usage(Warning at 80%)
* Monitor specific process

## Install running environment
### Install python3
```bash
sudo apt install python3-pip
```
### Install python package
```commandline
pip3 install psutil
pip3 install discord-webhook
```

## Config
### Setup discord notification
1. Get a webhook url. You may refer to this post.  
[https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)  
2. Fill it into `config.py`.
```python3
"""
Discord Config
"""
# noinspection SpellCheckingInspection
webhook_url = "<Your-URL>"
```
3.  Setup crontab to run this script whenever you want.
### Set process to monitor
Here is a template of process object.
```python3
{
    "name": "<Name of the process>",
    "bin": "<Binary file of the process>",
    "restart_cmd": "<What command to execute when the process is not running>",
    "message": "<The message to send through discord after executing the cmd.>"
}
```
