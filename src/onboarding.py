"""
onboarding.py
"""
# pylint: disable=too-few-public-methods

import pathlib

HERE = pathlib.Path(__file__).parent

ABOUT_GROUP = (HERE / "data/about.txt").read_text()
INTRODUCE = (HERE / "data/introduce.txt").read_text()


class OnboardingMessage:
    """
    Onboarding UI bulding message
    """

    # Message block
    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ABOUT_GROUP,
        }
    }

    # Divider blocnk
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel: str, new_user_id: str) -> None:
        self.channel = channel
        self.username = "gheorghe"
        self.icon_emoji = ":robot_face:"
        self.user_id = new_user_id
        self.timestamp = ""

    def get_message_payload(self) -> dict:
        """
        Returns the message block
        """
        return {
            "timestamp": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self._introduce_yourself_block(),
                self.DIVIDER_BLOCK,
                self.WELCOME_BLOCK,
                ]
            }

    def _introduce_yourself_block(self) -> dict:
        """
        Returns introduce yourself block
        """
        return {
            "type": "section",
            "text":{
                "type": "mrkdwn",
                "text": INTRODUCE,
            }
        }

    def _get_admins(self) -> dict:
        """
        Return group's admin
        """
