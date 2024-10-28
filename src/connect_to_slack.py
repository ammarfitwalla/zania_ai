import logging
from slack_sdk import WebClient


class SlackConnector:
    def __init__(self, bot_token, channel_name):
        self.client = WebClient(token=bot_token)
        self.default_channel = channel_name
        logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def post_results_to_slack(self, answers_json: str, channel: str) -> None:
        """
        Posts the JSON-formatted answers to a specified Slack channel.

        Args:
            answers_json (str): JSON-formatted answers to post.
            channel (str): Slack channel ID or name. Defaults to self.default_channel.

        Returns:
            None
        """
        try:
            self.client.chat_postMessage(channel=channel, text="Here are the answers to your questions:")
            self.client.chat_postMessage(channel=channel, text=f"```{answers_json}```")
            logging.info("Results posted to Slack successfully.")
        except Exception as e:
            logging.error(f"Error posting to Slack: {e}")
