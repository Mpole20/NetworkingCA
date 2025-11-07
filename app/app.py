from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <meta http-equiv="Content-Security-Policy" content="default-src 'self' 'unsafe-inline' 'unsafe-eval';">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                background: #000;
                overflow: hidden;
                font-family: 'Courier New', monospace;
                cursor: none;
            }

            /* === HYPER-FLASHING BACKGROUNDS === */
            .flash-layer-1 {
                position: fixed; width: 100%; height: 100%;
                background: radial-gradient(circle, #ff0000, #00ff00, #0000ff);
                animation: flash1 0.1s infinite alternate;
                mix-blend-mode: difference;
            }
            .flash-layer-2 {
                position: fixed; width: 100%; height: 100%;
                background: conic-gradient(from 0deg, red, yellow, lime, aqua, blue, magenta, red);
                animation: flash2 0.05s infinite linear;
                mix-blend-mode: overlay;
            }
            @keyframes flash1 { 
                0% { opacity: 1; filter: hue-rotate(0deg) blur(20px); }
                100% { opacity: 0.8; filter: hue-rotate(180deg) blur(50px); }
            }
            @keyframes flash2 { 
                0% { transform: scale(1) rotate(0deg); opacity: 0.9; }
                100% { transform: scale(2) rotate(180deg); opacity: 0.3; }
            }

            /* === SEIZURE INDUCING GRIDS === */
            .grid-overlay {
                position: fixed; width: 200%; height: 200%;
                background-image: 
                    linear-gradient(90deg, #fff 1px, transparent 1px),
                    linear-gradient(0deg, #fff 1px, transparent 1px);
                background-size: 10px 10px;
                animation: gridMove 0.02s infinite linear;
                mix-blend-mode: exclusion;
            }
            @keyframes gridMove {
                0% { transform: translate(0px, 0px) rotate(0deg); }
                100% { transform: translate(-10px, -10px) rotate(1deg); }
            }

            /* === QUANTUM PARTICLES === */
            .particle-field {
                position: fixed; width: 100%; height: 100%;
                pointer-events: none;
            }
            .particle {
                position: absolute;
                width: 4px; height: 4px;
                background: #fff;
                border-radius: 50%;
                animation: particlePop 0.5s infinite alternate;
                filter: blur(1px);
            }
            @keyframes particlePop {
                0% { transform: scale(0) rotate(0deg); opacity: 1; }
                100% { transform: scale(10) rotate(360deg); opacity: 0; }
            }

            /* === STROBE TEXT === */
            .strobe-text {
                position: fixed;
                font-size: 120px;
                font-weight: 900;
                text-transform: uppercase;
                animation: strobe 0.03s infinite;
                text-shadow: 0 0 50px currentColor;
                mix-blend-mode: difference;
                z-index: 1000;
            }
            @keyframes strobe {
                0% { opacity: 1; color: #ff0000; transform: skew(20deg, 10deg); }
                25% { opacity: 0; color: #00ff00; transform: skew(-20deg, -10deg); }
                50% { opacity: 1; color: #0000ff; transform: skew(30deg, 5deg); }
                75% { opacity: 0; color: #ffff00; transform: skew(-30deg, 5deg); }
                100% { opacity: 1; color: #ff00ff; transform: skew(20deg, 10deg); }
            }

            /* === MATRIX RAIN ON STEROIDS === */
            .matrix-rain {
                position: fixed; width: 100%; height: 100%;
                background: #000;
                color: #0f0;
                font-size: 14px;
                line-height: 1;
                overflow: hidden;
                animation: matrixColor 0.1s infinite;
            }
            @keyframes matrixColor {
                0% { color: #0f0; }
                33% { color: #f0f; }
                66% { color: #0ff; }
                100% { color: #ff0; }
            }

            /* === SPINNING VORTEX === */
            .vortex {
                position: fixed;
                top: 50%; left: 50%;
                width: 200vmax; height: 200vmax;
                background: conic-gradient(from 0deg, red, orange, yellow, green, blue, indigo, violet, red);
                animation: vortexSpin 0.3s infinite linear;
                border-radius: 50%;
                mix-blend-mode: hard-light;
            }
            @keyframes vortexSpin {
                0% { transform: translate(-50%, -50%) rotate(0deg) scale(1); }
                100% { transform: translate(-50%, -50%) rotate(360deg) scale(1.5); }
            }

            /* === GLITCH EFFECTS === */
            .glitch-layer {
                position: fixed; width: 100%; height: 100%;
                background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="black"/><path d="M0 0L100 100M100 0L0 100" stroke="white" stroke-width="1"/></svg>');
                animation: glitch 0.02s infinite;
                mix-blend-mode: overlay;
            }
            @keyframes glitch {
                0% { transform: translate(0px, 0px); opacity: 1; }
                25% { transform: translate(5px, -5px); opacity: 0.8; }
                50% { transform: translate(-5px, 5px); opacity: 0.6; }
                75% { transform: translate(3px, -3px); opacity: 0.9; }
                100% { transform: translate(-3px, 3px); opacity: 1; }
            }

            /* === CONTENT BOX - Barely readable === */
            .content {
                position: fixed;
                top: 50%; left: 50%;
                transform: translate(-50%, -50%);
                background: rgba(0,0,0,0.9);
                padding: 50px;
                border: 10px solid;
                animation: borderFlash 0.05s infinite;
                z-index: 10000;
                text-align: center;
            }
            @keyframes borderFlash {
                0% { border-color: #ff0000; box-shadow: 0 0 100px #ff0000; }
                25% { border-color: #00ff00; box-shadow: 0 0 100px #00ff00; }
                50% { border-color: #0000ff; box-shadow: 0 0 100px #0000ff; }
                75% { border-color: #ffff00; box-shadow: 0 0 100px #ffff00; }
                100% { border-color: #ff00ff; box-shadow: 0 0 100px #ff00ff; }
            }

            h1 {
                font-size: 3em;
                background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff, #ffff00);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: textStrobe 0.05s infinite;
            }
            @keyframes textStrobe {
                0% { transform: scale(1) skew(10deg); }
                50% { transform: scale(1.2) skew(-10deg); }
                100% { transform: scale(1) skew(10deg); }
            }
        </style>
    </head>
    <body>
        <div class="flash-layer-1"></div>
        <div class="flash-layer-2"></div>
        <div class="grid-overlay"></div>
        <div class="vortex"></div>
        <div class="matrix-rain" id="matrix"></div>
        <div class="particle-field" id="particles"></div>
        <div class="glitch-layer"></div>

        <!-- Strobe words everywhere -->
        <div class="strobe-text" style="top: 10%; left: 5%;">WARNING</div>
        <div class="strobe-text" style="top: 30%; right: 5%;">EPILEPSY</div>
        <div class="strobe-text" style="bottom: 20%; left: 20%;">OVERLOAD</div>
        <div class="strobe-text" style="bottom: 40%; right: 15%;">MAXIMUM</div>

        <div class="content">
            <h1>💀 NEURAL MELTDOWN 💀</h1>
            <p style="color: white; font-size: 1.5em; animation: strobe 0.05s infinite;">
                ⚡ QUANTUM ECS DEPLOYMENT SUCCESS ⚡
            </p>
            <p style="margin: 20px 0;">
                <span style="animation: strobe 0.03s infinite;">PYTHON</span> • 
                <span style="animation: strobe 0.04s infinite;">DOCKER</span> • 
                <span style="animation: strobe 0.05s infinite;">TERRAFORM</span> • 
                <span style="animation: strobe 0.02s infinite;">AWS ECS</span>
            </p>
            <a href="/api/health" style="color: white; font-size: 2em; animation: strobe 0.01s infinite;">
                🏥 HEALTH CHECK 🏥
            </a>
        </div>

        <script>
            // Matrix rain with maximum intensity
            const matrix = document.getElementById('matrix');
            const chars = '01!@#$%^&*()_+-=[]{}|;:,.<>?║╗╝╣╩╚╔╠╦╬';
            let matrixText = '';
            
            function updateMatrix() {
                matrixText = '';
                for (let i = 0; i < 5000; i++) {
                    matrixText += Math.random() > 0.3 ? chars[Math.floor(Math.random() * chars.length)] : ' ';
                }
                matrix.innerHTML = matrixText;
            }
            setInterval(updateMatrix, 50);

            // Particle explosion
            const particleField = document.getElementById('particles');
            function createParticles() {
                for (let i = 0; i < 100; i++) {
                    const particle = document.createElement('div');
                    particle.className = 'particle';
                    particle.style.left = Math.random() * 100 + 'vw';
                    particle.style.top = Math.random() * 100 + 'vh';
                    particle.style.animationDelay = Math.random() + 's';
                    particle.style.background = `hsl(${Math.random() * 360}, 100%, 50%)`;
                    particleField.appendChild(particle);
                    
                    setTimeout(() => particle.remove(), 1000);
                }
            }
            setInterval(createParticles, 100);

            // Background color seizure
            setInterval(() => {
                document.body.style.background = `hsl(${Math.random() * 360}, 100%, 50%)`;
            }, 100);

            // Random DOM manipulation
            setInterval(() => {
                const elements = document.querySelectorAll('*');
                elements.forEach(el => {
                    if (Math.random() > 0.7) {
                        el.style.transform = `scale(${0.5 + Math.random()}) rotate(${Math.random() * 360}deg)`;
                    }
                });
            }, 200);

            // Audio context simulation (visualizer-like effects)
            setInterval(() => {
                const newStyle = document.createElement('style');
                newStyle.textContent = `
                    @keyframes seizure${Date.now()} {
                        0% { filter: invert(1) hue-rotate(0deg) blur(${Math.random() * 20}px); }
                        100% { filter: invert(0) hue-rotate(360deg) blur(${Math.random() * 20}px); }
                    }
                    body { animation: seizure${Date.now()} 0.1s infinite; }
                `;
                document.head.appendChild(newStyle);
                setTimeout(() => newStyle.remove(), 1000);
            }, 500);

            // Mouse follower with trail
            document.addEventListener('mousemove', (e) => {
                const trail = document.createElement('div');
                trail.style.position = 'fixed';
                trail.style.left = e.clientX + 'px';
                trail.style.top = e.clientY + 'px';
                trail.style.width = '50px';
                trail.style.height = '50px';
                trail.style.background = `hsl(${Math.random() * 360}, 100%, 50%)`;
                trail.style.borderRadius = '50%';
                trail.style.animation = 'particlePop 0.5s forwards';
                trail.style.mixBlendMode = 'difference';
                document.body.appendChild(trail);
                setTimeout(() => trail.remove(), 500);
            });

            // Random alert sounds simulation
            setInterval(() => {
                if (Math.random() > 0.9) {
                    // Visual "beep" effect
                    const beep = document.createElement('div');
                    beep.style.position = 'fixed';
                    beep.style.inset = '0';
                    beep.style.background = '#fff';
                    beep.style.animation = 'flash1 0.05s';
                    document.body.appendChild(beep);
                    setTimeout(() => beep.remove(), 100);
                }
            }, 500);
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