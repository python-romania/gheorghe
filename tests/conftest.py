"""
conftest.py
"""
import os
import pytest
import slack
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

@pytest.fixture(scope="session")
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
            'client_msg_id': 'cfcf307d-f78e-47ad-...c8bcb0fe4',
            'event_ts': '1561815400.004000',
            'source_team': 'TG03E73T9',
            'suppress_notification': False,
            'team': 'TG03E73T9',
            'ts': '1561815400.004000',
            'user_team': 'TG03E73T9',
        },
        "web_client": "",
    }
    yield payload
    del payload

@pytest.fixture(scope="function")
def response_fixture():
    """
    Setup response example

    Yield:
        response (dict): response sample

    Returns:
        None
    """
    response = {
        "ok": True,
        "channel":  "GKZ71F9DW",
        "username": "ecto1",
        "bot_id": "B19LU7CSY",
        "attachments": [
            {
                "text": "This is an attachment",
                "id": 1,
                "fallback": "This is an attachment's fallback"
            }
        ],
        "type": "message",
        "subtype": "bot_message",
        "ts": "1503435956.000247"
    }
    yield response
    del response


@pytest.fixture(scope="session")
def team_join_event_fixture():
    """
    Setup for team_join event.

    Yield:
        response (dict): response sample

    Returns:
        None
    """
    response = {
        "data": {
            "user": {
                "id": "UFY99RRNU"
            }
        },
        "web_client": "",
    }
    yield response
    del response
