"""
test_app.py
"""
# pylint: disable=too-few-public-methods

# Standard library
from importlib import reload
from unittest.mock import patch
from unittest.mock import MagicMock

# Third-party library
import pytest # type: ignore imports

# Local modules
from src import app


class TestApp:
    """
    Testing app events
    """

    @staticmethod
    @patch("slack.WebClient", spec=True)
    def test_team_join_event(fake_web_client: MagicMock, payload_fixture: dict) -> None:
        """
        Tests if a "team_join" event has been triggered.

        Attributes:
            fake_web_client (MagicMock): fake slack api web client
            payload_fixture (dict): fake payload

        Returns:
            None
        """
        payload_fixture["web_client"] = fake_web_client
        payload_fixture["data"] = {"user": {"id": "UFY99RRNU"}}

        with patch("slack.RTMClient.run_on", lambda *arg, **kwarg: lambda f: f):
            # Import again app module with the patched decorator
            reload(app)
            response = app.onboarding_event(**payload_fixture)
            assert response["ok"]

        reload(app)


    @staticmethod
    @patch("slack.WebClient", spec=True)
    def test_message_event(fake_web_client: MagicMock, payload_fixture: dict) -> None:
        """
        Tests if a message is sent and an "OK" response is received.

        Attributes:
            fake_web_client (MagicMock): fake slack web client
            payload_fixture (dict): payload received from rtm_client

        Returns:
            None
        """
        payload_fixture["web_client"] = fake_web_client
        payload_fixture["data"] = {"chnnel": "GKZ71F9DW", "user": "UFY99RRNU", "text":"start", }

        fake_response = {"ok": True, "channel": "GKZ71F9DW"}
        fake_web_client.chat_postMessage.return_value = fake_response

        with patch("slack.RTMClient.run_on", lambda *arg, **kwarg: lambda f: f):
            # Import again app module with the patced decorator
            reload(app)
            response = app.message(**payload_fixture)
            assert response["ok"]
            assert response["channel"] == fake_response["channel"]
        # Import again app module without applying the patched decorator
        reload(app)

    @staticmethod
    @patch("slack.WebClient", spec=True)
    def test_message_event_none(fake_web_client, payload_fixture: dict) -> None:
        """
        Test if if None is returned. That means the message will
        not be "start".

        Attributes:
            fake_web_client (MagicMock): fake slack web client

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





