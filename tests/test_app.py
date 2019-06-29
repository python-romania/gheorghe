"""
test_app.py
"""
from importlib import reload
from unittest.mock import patch

import slack

from src import app
# Sample data payload
#
# data = {'channel': 'GKZ71F9DW',
#          'client_msg_id': 'cfcf307d-f78e-47ad-...c8bcb0fe4',
#          'event_ts': '1561815400.004000',
#          'source_team': 'TG03E73T9',
#          'suppress_notification': False,
#          'team': 'TG03E73T9',
#          'text': 'start',
#          'ts': '1561815400.004000',
#          'user': 'UFY99RRNU',
#          'user_team': 'TG03E73T9'}

# Sample response for slack.web_client.chat_postMessage
# response = {
#     "ok": true,
#     "channel": "C1H9RESGL",
#     "ts": "1503435956.000247",
#     "message": {
#         "text": "Here's a message for you",
#         "username": "ecto1",
#         "bot_id": "B19LU7CSY",
#         "attachments": [
#             {
#                 "text": "This is an attachment",
#                 "id": 1,
#                 "fallback": "This is an attachment's fallback"
#             }
#         ],
#         "type": "message",
#         "subtype": "bot_message",
#         "ts": "1503435956.000247"
#     }
# }


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


def test_data_payload(web_client_fixture: slack.WebClient) -> None:
    """
    Testing data payload
    """
    payload = {
        "data": {
            "channel": "GKZ71F9DW",
            "user": "UFY99RRNU",
            "text":"start"},
        "web_client": web_client_fixture,
        }
    with patch("slack.RTMClient.run_on", lambda *arg, **kwarg: lambda f: f):
        reload(app)     # reload app module
        expected_data = payload["data"]
        data = app.message(**payload)
        assert data.get("user") == expected_data.get("user")
        assert data.get("channel") == expected_data.get("channel")
        assert data.get("text") == expected_data.get("text")
    reload(app) # reload app module


def test_send_message(web_client_fixture: slack.WebClient) -> None:
    """
    Testing send message
    """
    channel = "GKZ71F9DW"
    user = "UFY99RRNU"
    message = "This is a simple test message"
    response = app.send_message(web_client_fixture, channel, user, message)
    assert response["ok"]
