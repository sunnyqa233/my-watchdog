import discord_webhook


class Discord:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send(self, content: str) -> int:
        """
        Send text through webhook. Will return 200 if success.
        """
        webhook = discord_webhook.DiscordWebhook(url=self.webhook_url, rate_limit_retry=True, content=content)
        return webhook.execute().status_code
