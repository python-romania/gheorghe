"""
callback.py
"""
# Standard library
from typing import Optional

# Third-party library
import slack # type: ignore imports

# Local modules
from .message import Message
from .onboarding import OnboardingMessage

# In memory storage
ONBOARDING_MESSAGE_LOG: dict = {}

def start_onboarding(web_client: slack.WebClient, new_user_id: str, channel: str) -> None:
    """
    Send a direct message to the new user with the
    welcome message.

    Attributes:
        web_client (slack.WebClient): slack api web client
        user_id (str): user if of the new user
        channel (str): the channel/direct message

    Returns:
        a dict with response from slack
    """
    # Build the message
    onboarding_message = OnboardingMessage(channel=channel, new_user_id=new_user_id)

    # Get the message
    message_to_be_sent = onboarding_message.get_message_payload()

    # Send the message to user
    response = web_client.chat_postMessage(**message_to_be_sent)

    # Get the timestamp
    onboarding_message.timestamp = response["ts"]

    # Log the message sent
    if channel not in ONBOARDING_MESSAGE_LOG:
        ONBOARDING_MESSAGE_LOG["channel"] = {}
    ONBOARDING_MESSAGE_LOG["channel"]["user_id"] = onboarding_message



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
