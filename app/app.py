from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <style>
            body {
                background-color: black;
                color: white;
                font-family: monospace;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .cube {
                font-size: 16px;
                line-height: 1;
                white-space: pre;
            }
        </style>
    </head>
    <body>
        <h1>ECS Deployment Project</h1>
        <div class="cube">
        +-------+
       /|      /|
      +-------+ |
      | |     | |
      | +-----|-+
      |/      |/
      +-------+
        </div>
        <p>Python Flask + Docker + Terraform + AWS ECS</p>
        <p><a href="/api/health" style="color: cyan;">Health Check</a></p>
    </body>
    </html>
    '''