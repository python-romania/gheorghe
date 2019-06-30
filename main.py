"""
main.py
"""
# Standard library
import os

# Third-party library
import slack
from dotenv import load_dotenv

# Load env
load_dotenv()

def init():
    """
    Init function.
    """
    if __name__ == "__main__":
        print("Program starts..")
        token = os.getenv("SLACK_BOT_TOKEN")
        rtm_client = slack.RTMClient(token=token)
        rtm_client.start()

# Start program
init()
