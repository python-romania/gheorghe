"""
app.py

Simple slack bot app.
"""
# Standard imports
import os

# Third party imports
import slack
from dotenv import load_dotenv

# Load .env
load_dotenv()


def send_message(web_client: slack.WebClient, channel_id: str, user_id: str) -> None:
    """
    Send a hello world message
    """
    message_to_be_sent = {
        "channel": channel_id,
        "user": user_id,
        "text": "Hello World!",
        }
    response = web_client.chat_postMessage(**message_to_be_sent)
    return response


@slack.RTMClient.run_on(event="message")
def message(**payload: dict) -> None:
    """
    It listens for a message event coming from
    slack and it sends a message back.
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")

    if text and text.lower() == "start":
        send_message(web_client, channel_id, user_id)


if __name__ == "__main__":
    print("Program starts..")
    TOKEN = os.getenv("SLACK_BOT_TOKEN")
    RTM_CLIENT = slack.RTMClient(token=TOKEN)
    RTM_CLIENT.start()
