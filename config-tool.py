import plugins.notification
from rich import console
import json

"""
Read & Write config
"""
config_path = "config.json"
config = {}


def read_config():
    global config
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.loads(f.read())


def write_config():
    global config
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(config))


"""
Config functions
"""
read_config()
terminal = console.Console()


def input_yes_no() -> bool:
    global terminal
    valid = False
    while not valid:
        option = terminal.input("(Y)es/(N)o: ").lower()
        if option in ["y", "yes", "(y)es"]:
            return True
        elif option in ["n", "no", "(n)o"]:
            return False
        else:
            terminal.print("Input invalid! Please try again.\n")


def input_int_1to100() -> int:
    global terminal
    valid = False
    while not valid:
        num_input = terminal.input("Input: ")
        try:
            num_input = int(num_input)
            if (num_input > 100) or (num_input < 1):
                raise ValueError
        except ValueError:
            terminal.print(f"{num_input} is not a number in 1-100.")
        else:
            return num_input


def set_discord_url():
    global terminal
    global config
    terminal.print("\n\n")
    url = terminal.input("[blue]Please enter new discord webhook url: [/blue]")
    webhook = plugins.notification.Discord(url)
    # Validation of url
    terminal.print("[blue]Do you want to send a validation message to check the url?[/blue]")
    usr_option = input_yes_no()
    if usr_option:
        webhook.send("Congratulations! If you see this message, then you've fill-in the webhook url correctly.")
        terminal.print("[blue]Have you receive the validation message?[/blue]")
        usr_option = input_yes_no()
        if not usr_option:
            set_discord_url()
    # Save settings
    config["discord_webhook"] = url
    write_config()


def set_disk_usage_check():
    global terminal
    global config
    terminal.print("\n\n")
    # Enable/Disable function
    terminal.print("[blue]Do you want to enable disk usage check?[/blue]")
    usr_option = input_yes_no()
    if usr_option:
        config["disk_usage_check"] = True
    else:
        config["disk_usage_check"] = False
    # Set warning threshold
    if config["disk_usage_check"]:
        terminal.print("[blue]Please enter the disk usage threshold(% of usage) for warning you "
                       "through discord.[/blue]")
        num = input_int_1to100()
        config["disk_usage_threshold"] = num
    # Save settings
    write_config()


def set_disk_temperature_check():
    global terminal
    global config
    terminal.print("\n\n")
    # Enable/Disable function
    terminal.print("[blue]Do you want to enable disk temperature check?[/blue]")
    usr_option = input_yes_no()
    if usr_option:
        config["disk_temperature_check"] = True
    else:
        config["disk_temperature_check"] = False
    # Set warning threshold
    if config["disk_temperature_check"]:
        terminal.print("[blue]Please enter the disk temperature threshold(degree celsius) for warning you "
                       "through discord.[/blue]")
        temp = input_int_1to100()
        config["disk_temperature_threshold"] = temp
    # Set emergency shutdown
    if config["disk_temperature_check"]:
        terminal.print("[blue]Do you want the watchdog to power off the system to prevent disk damage?[/blue]")
        usr_option = input_yes_no()
        if usr_option:
            config["disk_temperature_shutdown"] = True
        else:
            config["disk_temperature_shutdown"] = False
    # Save settings
    write_config()


def set_ram_usage_check():
    global terminal
    global config
    terminal.print("\n\n")
    # Enable/Disable function
    terminal.print("[blue]Do you want to enable ram usage check?[/blue]")
    usr_option = input_yes_no()
    if usr_option:
        config["ram_usage_check"] = True
    else:
        config["ram_usage_check"] = False
    # Set warning threshold
    if config["ram_usage_check"]:
        terminal.print("[blue]Please enter the ram usage threshold(% of usage) for warning you "
                       "through discord.[/blue]")
        num = input_int_1to100()
        config["ram_usage_threshold"] = num
    # Save settings
    write_config()


def set_swap_usage_check():
    global terminal
    global config
    terminal.print("\n\n")
    # Enable/Disable function
    terminal.print("[blue]Do you want to enable swap usage check?[/blue]")
    usr_option = input_yes_no()
    if usr_option:
        config["swap_usage_check"] = True
    else:
        config["swap_usage_check"] = False
    # Set warning threshold
    if config["swap_usage_check"]:
        terminal.print("[blue]Please enter the swap usage threshold(% of usage) for warning you "
                       "through discord.[/blue]")
        num = input_int_1to100()
        config["swap_usage_threshold"] = num
    # Save settings
    write_config()


"""
Main
"""
if config["discord_webhook"] == "":
    set_discord_url()

done = False
while not done:
    terminal.print(
        "Menu:",
        f"(1) Set discord webhook url",
        f"(2) Set disk usage check | Enabled: {config['disk_usage_check']} | Threshold: {config['disk_usage_threshold']}",
        f"(3) Set disk temperature check | Enabled: {config['disk_temperature_check']} | Threshold: {config['disk_temperature_threshold']} | Emergency Shutdown: {config['disk_temperature_shutdown']}",
        f"(4) Set ram usage check | Enabled: {config['ram_usage_check']} | Threshold: {config['ram_usage_threshold']}",
        f"(5) Set swap usage check | Enabled: {config['swap_usage_check']} | Threshold: {config['swap_usage_threshold']}",
        "(6) Quit",
        sep="\n"
    )
    try:
        option = int(terminal.input("Input: "))
        if option < 1 or option > 6:
            raise ValueError
    except ValueError:
        terminal.print("Please enter a valid number!")
    else:
        if option == 1:
            set_discord_url()
        elif option == 2:
            set_disk_usage_check()
        elif option == 3:
            set_disk_temperature_check()
        elif option == 4:
            set_ram_usage_check()
        elif option == 5:
            set_swap_usage_check()
        elif option == 6:
            exit(0)
