"""
test_app.py
"""
# pylint: disable=too-few-public-methods

# Standard library
from importlib import reload
from unittest.mock import patch
from unittest.mock import MagicMock

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
    @patch("slack.WebClient", spec=True)
    def test_message_event(fake_web_client, response_fixture: dict, payload_fixture: dict,) -> None:
        """
        Tests if a message is sent and an "OK" response is received.

        Attributes:
            response_fixture (dict): response of web_client
            payload_fixture (dict): payload received from rtm_client

        Returns:
            None
        """

        fake_web_client.chat_postMessage.return_value = response_fixture
        payload_fixture["web_client"] = fake_web_client

        with patch("slack.RTMClient.run_on", lambda *arg, **kwarg: lambda f: f):

            # Import again app module with the and apply the patched decorator
            reload(app)

            response = app.message(**payload_fixture)
            assert response["ok"]
            assert response["channel"] == response_fixture["channel"]

        # Import again app module without applying the patched decorator
        reload(app)

    @staticmethod
    @patch("slack.WebClient", spec=True)
    def test_message_event_none(fake_web_client, payload_fixture: dict) -> None:
        """
        Test if if None is returned. That means the message will
        not be "start".

        Attributes:
            web_client (slack.WebClient)

        Returns:
            Nothing
        """
        payload_fixture["web_client"] = fake_web_client
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

class TestMessage:
    """
    Testing UI message blocks
    """

class TestOnboarding:
    """
    Testing UI onboarding blocks
    """





