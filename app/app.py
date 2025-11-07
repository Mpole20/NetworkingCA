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
                background-color: #0a0a2a;
                color: #00ffcc;
                font-family: 'Courier New', monospace;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                overflow: hidden;
            }
            .dna-container {
                animation: spinDNA 4s linear infinite;
                transform-style: preserve-3d;
            }
            .dna {
                font-size: 6px;
                line-height: 0.8;
                white-space: pre;
                text-shadow: 0 0 10px #00ffcc;
            }
            @keyframes spinDNA {
                0% { transform: rotateY(0deg) rotateX(10deg); }
                100% { transform: rotateY(360deg) rotateX(10deg); }
            }
            .pulse {
                animation: pulse 2s ease-in-out infinite alternate;
            }
            @keyframes pulse {
                0% { color: #00ffcc; text-shadow: 0 0 5px #00ffcc; }
                100% { color: #ff00cc; text-shadow: 0 0 15px #ff00cc; }
            }
        </style>
    </head>
    <body>
        <h1 class="pulse">ECS Project Deployment</h1>
        <div class="dna-container">
            <div class="dna" id="dnaHelix"></div>
        </div>
        <p>Python Flask + Docker + Terraform + AWS ECS</p>
        <p><a href="/api/health" style="color: #00ffcc;">Health Check</a></p>
        
        <script>
            const dnaFrames = [
                `
          O
         / \\
        O   O
         \\ /
          O
         / \\
        O   O
         \\ /
          O
         / \\
        O   O
         \\ /
          O
                `,
                `
           O
          / \\
         O   O
          \\ /
           O
          / \\
         O   O
          \\ /
           O
          / \\
         O   O
          \\ /
           O
                `,
                `
            O
           / \\
          O   O
           \\ /
            O
           / \\
          O   O
           \\ /
            O
           / \\
          O   O
           \\ /
            O
                `
            ];
            
            let dnaFrame = 0;
            const dnaElement = document.getElementById('dnaHelix');
            
            function animateDNA() {
                dnaElement.textContent = dnaFrames[dnaFrame];
                dnaFrame = (dnaFrame + 1) % dnaFrames.length;
            }
            
            // Multiple animation speeds
            setInterval(animateDNA, 300);
            
            // Add some random color changes
            setInterval(() => {
                const colors = ['#00ffcc', '#ff00cc', '#00ccff', '#ccff00'];
                const randomColor = colors[Math.floor(Math.random() * colors.length)];
                document.body.style.color = randomColor;
            }, 2000);
        </script>
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