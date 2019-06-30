"""
test_app.py
"""
# pylint: disable=too-few-public-methods

# Standard library
from importlib import reload
from unittest.mock import patch

# Third-party library
import slack
import pytest

# Local modules
from src import app


class TestApp:
    """
    Testing app events
    """

    @staticmethod
    def test_message_event(
            web_client_fixture: slack.WebClient,
            response_fixture: dict,
            payload_fixture: dict) -> None:
        """
        Tests if a message is sent and an "OK" response is received.

        Attributes:
            web_client_fixture(slack.WebClient): slack api web client

        Returns:
            None
        """
        payload_fixture["web_client"] = web_client_fixture

        with patch("slack.RTMClient.run_on", lambda *arg, **kwarg: lambda f: f):
            reload(app)
            response = app.message(**payload_fixture)
            assert response["ok"]
            assert response["channel"] == response_fixture["channel"]

        reload(app)

    @staticmethod
    def test_message_event_none(
            web_client_fixture: slack.WebClient,
            payload_fixture: dict) -> None:
        """
        Test if if None is returned. That means the message will
        not be "start".

        Attributes:
            web_client (slack.WebClient)

        Returns:
            Nothing
        """
        payload_fixture["web_client"] = web_client_fixture
        payload_fixture["data"]["text"] = "other"

        with patch("slack.RTMClient.run_on", lambda *arg, **kwarg: lambda f: f):
            reload(app)
            response = app.message(**payload_fixture)
            assert response is None


@pytest.mark.skip()
class TestCallback:
    """
    Testing app's function callbacks
    """
    @staticmethod
    def test_none_message(web_client_fixture: slack.WebClient) -> None:
        """
        Testing if not "start" message
        """
        payload = {
            "data": {
                "channel": "GKZ71F9DW",
                "user": "UFY99RRNU",
                "text":"other"},
            "web_client": web_client_fixture,
            }
        with patch("slack.RTMClient.run_on", lambda *arg, **kwarg: lambda f: f):
            reload(app)
            data = app.message(**payload)
            assert data is None

    @staticmethod
    def test_send_messages(web_client_fixture: slack.WebClient) -> None:
        """
        Testing send message
        """
        channel = "GKZ71F9DW"
        user = "UFY99RRNU"
        message = "This is a simple test message"
        response = app.send_message(web_client_fixture, channel, user, message)
        assert response["ok"]

class TestMessage:
    """
    Testing UI message blocks
    """

class TestOnboarding:
    """
    Testing UI onboarding blocks
    """





