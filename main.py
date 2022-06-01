import plugins.notification
import plugins.temperature
import plugins.disk
import plugins.ram
import json
import os

# Read options
with open(os.path.dirname(os.path.realpath(__file__))+"/config.json", "r", encoding="utf-8") as f:
    options = json.loads(f.read())

# Create discord webhook
webhook = plugins.notification.Discord(options['discord_webhook'])

# Run disk usage check
if options['disk_usage_check']:
    for item in plugins.disk.get_disk_usage():
        if item[0] > options['disk_usage_threshold']:
            webhook.send(f"{item[2]} mounted on {item[1]} used {item[0]}%.")


# Run disk temperature check
if options['disk_temperature_check']:
    for item in plugins.temperature.get_disk_temperature():
        if item[0] > options['disk_temperature_threshold']:
            webhook.send(f"{item[1]} reaches {item[0]} degree celsius.")
            if options['disk_temperature_shutdown']:
                # noinspection SpellCheckingInspection
                os.system("poweroff")

# Run ram usage check
if options['ram_usage_check']:
    if plugins.ram.get_ram_used_percentage() > options['ram_usage_threshold']:
        webhook.send(f"Ram usage reaches {plugins.ram.get_ram_used_percentage()}%.")

# Run swap usage check
if options["swap_usage_check"]:
    if plugins.ram.get_swap_used_percentage() > options["swap_usage_threshold"]:
        webhook.send(f"Swap usage reaches {plugins.ram.get_swap_used_percentage()}%.")
