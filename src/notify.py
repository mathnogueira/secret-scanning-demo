import requests

NOTIFY_API_KEY = "1PIzn2wJOau3OEak1ZvKR1osb70iJ1vxS9WtSWPM"


def notify(channel, text):
    requests.post("https://notify.example.com/send", headers={"X-Api-Key": NOTIFY_API_KEY}, json={"channel": channel, "text": text})
