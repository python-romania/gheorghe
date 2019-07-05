"""
app.py

Simple slack bot app.
"""
# Standard library import
from typing import Union

# Third-party library
import slack  # type: ignore

# Local modules
from . import callback

@slack.RTMClient.run_on(event="team_join")
def onboarding_event(**payload) -> None:
    """
    When a new user joins the team, "start_onboarding"
    callback method is triggered.

    Attributes:
        payload (dict): payload responde from slack api

    Returns:
        Response if the message was sent OK

    """
    # Get the web_client
    web_client = payload["web_client"]

    # Get the id of new user
    new_user_id = payload["data"]["user"]["id"]

    # Open a direct message with the new user
    response = web_client.im_open(user=new_user_id)
    channel = response["channel"]["id"]

    # Build the message
    if response:
        callback.start_onboarding(web_client, new_user_id, channel)
        return response
    return None

@slack.RTMClient.run_on(event="message")
def message(**payload: dict) -> Union[dict, None]:
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
