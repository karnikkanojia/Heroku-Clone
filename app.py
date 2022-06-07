import os
from flask import Flask, render_template

import pulumi.automation as auto


def ensure_plugins():
    ws = auto.LocalWorkspace()
    ws.install_plugin("aws", "v4.0.0")

def create_app():
    ensure_plugins()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    app.run()