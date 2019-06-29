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
    """
    token = os.getenv("SLACK_BOT_TOKEN")
    web_client = slack.WebClient(token)
    yield web_client
    del web_client
