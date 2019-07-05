"""
conftest.py
"""
import os
import pytest  # type: ignore imports
import slack   # type: ignore imports
from dotenv import load_dotenv

# load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def web_client_fixture() -> slack.WebClient:
    """
    Setup a web_client

    Yield:
        web_client (dict): slack api web client

    Returns:
        None
    """
    token = os.getenv("SLACK_BOT_TOKEN")
    web_client = slack.WebClient(token)
    yield web_client
    del web_client

@pytest.fixture(scope="function")
def payload_fixture():
    """
    Setup payload example

    Yield:
        payload (dict): dictionary with data

    Returns:
        None
    """
    payload = {
        "data":
        {
            "channel": "GKZ71F9DW",
            "user": "UFY99RRNU",
            "text":"start",
        },
        "web_client": "",
    }
    yield payload
