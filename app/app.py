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
                background: linear-gradient(45deg, #000, #1a0033);
                color: #00ffff;
                font-family: monospace;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .wave {
                font-size: 12px;
                line-height: 1;
                white-space: pre;
                animation: wave 2s ease-in-out infinite;
                text-shadow: 0 0 10px #00ffff;
            }
            @keyframes wave {
                0%, 100% { transform: translateY(0px) scale(1); }
                50% { transform: translateY(-10px) scale(1.05); }
            }
            .ripple {
                animation: ripple 3s linear infinite;
            }
            @keyframes ripple {
                0% { transform: scale(1); opacity: 1; }
                100% { transform: scale(1.5); opacity: 0; }
            }
        </style>
    </head>
    <body>
        <h1>ECS Project Deployment</h1>
        <div class="wave">
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
        ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
        ▒▓██████████████████████████▓▒
        ▒▓██████████████████████████▓▒
        ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░
        ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        </div>
        <p class="ripple">Python Flask + Docker + Terraform + AWS ECS</p>
        <p><a href="/api/health" style="color: #ff00ff;">Health Check</a></p>
    </body>
    </html>
    '''


@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'service': 'Python Flask App'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)