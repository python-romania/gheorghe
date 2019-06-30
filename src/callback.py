"""
callback.py
"""
# Standard library
from typing import Optional

# Third-party library
import slack

# Local modules
from .message import Message

def send_message(web_client: slack.WebClient, channel_id: str, user_id: Optional[str], text_message: Optional[str]) -> dict:
    """
    Send a message when the "message" event is triggered

    Attributes:
        web_client (slack.WebClient): slack web client
        channel_id (str): channel's id or name
        user_id (str): username or user_id
        text_message (str): message to be sent

    Returns:
        A dictionary with a response
    """
    # Instantiate message UI
    message = Message(channel_id, user_id, text_message)

    # Create message block
    message_to_be_sent = message.get_message_payload()

    # Send the message
    response = web_client.chat_postMessage(**message_to_be_sent)

    # Return response
    return response
