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
                background: #000;
                color: #0f0;
                font-family: 'Courier New', monospace;
                margin: 0;
                overflow: hidden;
                position: relative;
            }
            .matrix-container {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                display: flex;
                flex-wrap: wrap;
                pointer-events: none;
            }
            .matrix-char {
                font-size: 14px;
                animation: matrixFall linear infinite;
                opacity: 0;
                text-shadow: 0 0 8px #0f0, 0 0 16px #0f0;
            }
            @keyframes matrixFall {
                0% { 
                    transform: translateY(-100px) rotate(0deg);
                    opacity: 0; 
                }
                5% { 
                    opacity: 1; 
                }
                95% { 
                    opacity: 1; 
                }
                100% { 
                    transform: translateY(100vh) rotate(360deg);
                    opacity: 0; 
                }
            }
            .cyber-grid {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: 
                    linear-gradient(90deg, transparent 99%, #0f0 99%),
                    linear-gradient(0deg, transparent 99%, #0f0 99%);
                background-size: 50px 50px;
                animation: gridPulse 2s ease-in-out infinite alternate;
                opacity: 0.3;
            }
            @keyframes gridPulse {
                0% { opacity: 0.1; }
                100% { opacity: 0.5; }
            }
            .content {
                position: relative;
                z-index: 10;
                text-align: center;
                background: rgba(0, 20, 0, 0.8);
                padding: 30px;
                border: 2px solid #0f0;
                box-shadow: 0 0 30px #0f0;
                animation: glow 3s ease-in-out infinite alternate;
            }
            @keyframes glow {
                0% { box-shadow: 0 0 20px #0f0, 0 0 40px #0f0; }
                100% { box-shadow: 0 0 30px #0f0, 0 0 60px #0f0, 0 0 80px #0f0; }
            }
            h1 {
                animation: textGlitch 5s infinite;
                text-shadow: 2px 2px 0 #f0f, -2px -2px 0 #0ff;
            }
            @keyframes textGlitch {
                0%, 100% { transform: translateX(0); }
                10% { transform: translateX(-2px); }
                20% { transform: translateX(2px); }
                30% { transform: translateX(-2px); }
                40% { transform: translateX(2px); }
                50% { transform: translateX(0); }
            }
        </style>
    </head>
    <body>
        <div class="cyber-grid"></div>
        <div class="matrix-container" id="matrix"></div>
        
        <div class="content">
            <h1>⚡ CYBER ECS DEPLOYMENT ⚡</h1>
            <div style="font-size: 24px; margin: 20px 0;">
            [██████████] 100% DEPLOYED
            </div>
            <div style="animation: pulse 1s infinite;">
            🔥 REAL-TIME CONTAINER ORCHESTRATION 🔥
            </div>
            <p style="margin: 20px 0;">
            PYTHON ⚡ DOCKER ⚡ TERRAFORM ⚡ AWS ECS
            </p>
            <p><a href="/api/health" style="color: #0ff; text-decoration: none; font-weight: bold;">
            🔍 SYSTEM HEALTH SCAN
            </a></p>
        </div>

        <script>
            // Matrix digital rain
            const chars = '01アイウエオカキクケコサシスセソタチツテト';
            const matrixContainer = document.getElementById('matrix');
            
            function createMatrix() {
                for (let i = 0; i < 150; i++) {
                    const char = document.createElement('div');
                    char.className = 'matrix-char';
                    char.textContent = chars[Math.floor(Math.random() * chars.length)];
                    char.style.left = Math.random() * 100 + 'vw';
                    char.style.animationDelay = Math.random() * 10 + 's';
                    char.style.animationDuration = (3 + Math.random() * 5) + 's';
                    char.style.fontSize = (10 + Math.random() * 10) + 'px';
                    char.style.color = `hsl(${Math.random() * 120 + 60}, 100%, 50%)`;
                    matrixContainer.appendChild(char);
                }
            }
            
            createMatrix();
            
            // Pulsing effects
            setInterval(() => {
                document.body.style.background = `hsl(${Math.random() * 360}, 50%, 5%)`;
            }, 2000);
            
            // Add glitch effect occasionally
            setInterval(() => {
                document.querySelector('h1').style.transform = 'skew(10deg, 0deg)';
                setTimeout(() => {
                    document.querySelector('h1').style.transform = 'skew(0deg, 0deg)';
                }, 100);
            }, 5000);
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