"""
main.py
"""
# Standard library
import os

# Third-party library
from dotenv import load_dotenv

from src import app

# Load env
load_dotenv()

# Start program
if __name__ == "__main__":
    print("Program starts..")
    TOKEN = os.getenv("SLACK_BOT_TOKEN")
    RTM_CLIENT = app.slack.RTMClient(token=TOKEN)
    RTM_CLIENT.start()
