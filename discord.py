from discord_webhook import DiscordWebhook
from config import webhook_url


def send_message(message: str):
    webhook = DiscordWebhook(url=webhook_url, content=message)
    print(f"Trying to send message via discord.\nResponse='{webhook.execute()}'")
