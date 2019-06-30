"""
message.py
"""
# pylint: disable=too-few-public-methods

class Message:
    """
    Message UI building block
    """

    # Divider block
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel: str, user_id: str, text: str) -> None:
        self.channel = channel
        self.username = "gheorghe"
        self.icon_emoji = ":robot_face:"
        self.user_id = user_id
        self.text = text
        self.timestamp = ""

    def get_message_payload(self) -> dict:
        """
        Returns message payload
        """
        return {
            "timestamp": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self._get_message_block(),
                self.DIVIDER_BLOCK,
                ]
            }

    def _get_message_block(self) -> dict:
        """
        Returns a message block
        """
        message = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": self.text
                }
            }
        return message
