"""
onboarding.py
"""
# pylint: disable=too-few-public-methods

import pathlib

HERE = pathlib.Path(__file__).parent

ABOUT_GROUP = (HERE / "data/about.md").read_text()
INTRODUCE = (HERE / "data/introduce.md").read_text()


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

    def __init__(self: OnboardingMessage, channel: str, user_id: str) -> None:
        self.channel = channel
        self.username = "gheorghe"
        self.icon_emoji = ":robot_face:"
        self.user_id = user_id
        self.timestamp = ""

    def get_message_payload(self: OnboardingMessage) -> dict:
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
                self.DIVIDER_BLOCK,
                ]
            }

    def _introduce_yourself_block(self: OnboardingMessage) -> dict:
        """
        Returns introduce yourself block
        """
        text = (
            f"*Hello {self.user_id}*\n",
            INTRODUCE
        )

        return {
            "type": "section",
            "text":{
                "type": "mrkdwn",
                "text": text,
            }
        }

    def _get_admins(self: OnboardingMessage) -> dict:
        """
        Return group's admin
        """
