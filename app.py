import os
import logging
from sheets import append_to_sheets
from paperParser import get_paper_title
from flask import Flask
from slack_sdk.web import WebClient
from slackeventsapi import SlackEventAdapter
# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])


    #return 0

# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@slack_events_adapter.on("message")
def message(payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("username")
    text = event.get("text")
    result = slack_web_client.users_profile_get(user=user_id)
    user_name = result['profile']['real_name']
    print("hello_main func")
    if text and 'https' in text.lower():
        paper_title, paper_link=get_paper_title(text)
        rows = [user_name, paper_link, paper_title.text]
        #print(rows)
        append_to_sheets(rows)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(port=3000)