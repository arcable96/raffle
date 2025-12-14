import json
import os

FILE = "tickets.json"

def load_tickets():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_tickets(tickets):
    with open(FILE, "w") as f:
        json.dump(tickets, f)