"""
app.py

Simple slack bot app.
"""
# Standard imports
import os

# Third-party library
import slack  # type: ignore
from dotenv import load_dotenv

# Local modules
from . import callback

# Load .env
load_dotenv()


@slack.RTMClient.run_on(event="message")
def message(**payload: dict) -> dict:
    """
    It listens for a 'message' event coming from
    slack and it sends a message back.

    Attributes:
        payload (dict): dict payload received from api

    Returns:
        A response if the message was sent succesfully
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")
    text_message = "Hello World"

    if text and text.lower() == "start":
        return callback.send_message(web_client, channel_id, user_id, text_message)
    return None


if __name__ == "__main__":
    print("Program starts..")
    TOKEN = os.getenv("SLACK_BOT_TOKEN")
    RTM_CLIENT = slack.RTMClient(token=TOKEN)
    RTM_CLIENT.start()
