from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<html>
<head>
    <title>7AM VIBES</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: linear-gradient(to bottom, #1a1a2e, #16213e);
            overflow: hidden;
            font-family: 'Courier New', monospace;
            height: 100vh;
            perspective: 1000px;
        }

        /* === SHAKY CAM EFFECT === */
        @keyframes shakyCam {
            0% { transform: translate(0px, 0px) rotate(0deg); }
            10% { transform: translate(-1px, 1px) rotate(-0.2deg); }
            20% { transform: translate(2px, -1px) rotate(0.3deg); }
            30% { transform: translate(-2px, 2px) rotate(0.1deg); }
            40% { transform: translate(1px, -2px) rotate(-0.3deg); }
            50% { transform: translate(-1px, 1px) rotate(0.2deg); }
            60% { transform: translate(2px, -1px) rotate(-0.1deg); }
            70% { transform: translate(-2px, 2px) rotate(0.3deg); }
            80% { transform: translate(1px, -2px) rotate(-0.2deg); }
            90% { transform: translate(-1px, 1px) rotate(0.1deg); }
            100% { transform: translate(0px, 0px) rotate(0deg); }
        }

        /* === POV BODY === */
        .pov-body {
            position: fixed;
            width: 100%;
            height: 100%;
            animation: shakyCam 0.2s infinite;
            transform-style: preserve-3d;
        }

        /* === LEFT HAND WITH CIGARETTE === */
        .left-hand {
            position: absolute;
            bottom: 30%;
            left: 10%;
            width: 200px;
            height: 300px;
            transform: rotate(-10deg) translateZ(50px);
            z-index: 100;
        }

        .hand {
            position: absolute;
            width: 120px;
            height: 180px;
            background: linear-gradient(45deg, #e8c4a1, #d4a574);
            border-radius: 60px 60px 20px 20px;
            box-shadow: 
                -5px 5px 15px rgba(0,0,0,0.5),
                inset 2px -2px 10px rgba(0,0,0,0.3);
        }

        .cigarette {
            position: absolute;
            top: 40px;
            left: 110px;
            width: 80px;
            height: 6px;
            background: linear-gradient(to right, #fff, #8b4513);
            border-radius: 3px;
            transform: rotate(15deg);
            animation: cigaretteGlow 3s infinite alternate;
        }

        .ash {
            position: absolute;
            top: 35px;
            left: 185px;
            width: 8px;
            height: 12px;
            background: #d3d3d3;
            border-radius: 4px;
            animation: ashFall 5s infinite;
        }

        .smoke {
            position: absolute;
            top: 30px;
            left: 190px;
            width: 40px;
            height: 40px;
            background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, transparent 70%);
            border-radius: 50%;
            animation: smokeRise 4s infinite ease-out;
            filter: blur(10px);
        }

        @keyframes cigaretteGlow {
            0% { box-shadow: 0 0 5px #ff4500; }
            50% { box-shadow: 0 0 15px #ff4500, 0 0 25px #ff8c00; }
            100% { box-shadow: 0 0 5px #ff4500; }
        }

        @keyframes ashFall {
            0% { transform: translateY(0px); opacity: 1; }
            80% { transform: translateY(100px); opacity: 0.5; }
            100% { transform: translateY(100px); opacity: 0; }
        }

        @keyframes smokeRise {
            0% { transform: translateY(0px) scale(0.5); opacity: 0.8; }
            100% { transform: translateY(-200px) scale(2); opacity: 0; }
        }

        /* === RIGHT HAND WITH PHONE === */
        .right-hand {
            position: absolute;
            bottom: 25%;
            right: 15%;
            width: 180px;
            height: 320px;
            transform: rotate(5deg) translateZ(100px);
            z-index: 100;
        }

        .phone {
            position: absolute;
            top: 50px;
            width: 120px;
            height: 220px;
            background: #1a1a1a;
            border-radius: 15px;
            box-shadow: 
                0 0 0 2px #333,
                inset 0 0 20px rgba(255,255,255,0.1),
                5px 5px 20px rgba(0,0,0,0.7);
            overflow: hidden;
        }

        .phone-screen {
            position: absolute;
            top: 5px;
            left: 5px;
            width: 110px;
            height: 210px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            overflow: hidden;
            font-size: 6px;
            color: white;
            padding: 8px;
        }

        .phone-content {
            animation: screenFlicker 10s infinite;
        }

        @keyframes screenFlicker {
            0%, 100% { opacity: 1; }
            95% { opacity: 0.9; }
            96% { opacity: 0.7; }
            97% { opacity: 0.9; }
            98% { opacity: 0.8; }
            99% { opacity: 1; }
        }

        /* === FLYING EFFECT BACKGROUND === */
        .flying-scene {
            position: absolute;
            width: 500%;
            height: 200%;
            background: 
                linear-gradient(to bottom, 
                    #87CEEB 0%, 
                    #4682B4 30%, 
                    #1E90FF 70%, 
                    #00008B 100%);
            animation: flyForward 20s linear infinite;
            transform-style: preserve-3d;
        }

        .cloud {
            position: absolute;
            background: rgba(255,255,255,0.9);
            border-radius: 50px;
            filter: blur(5px);
            animation: cloudFloat 15s infinite ease-in-out;
        }

        .building {
            position: absolute;
            bottom: 0;
            background: linear-gradient(to top, #2c3e50, #34495e);
            animation: buildingPass 8s infinite linear;
        }

        @keyframes flyForward {
            0% { transform: translateZ(-1000px) translateY(0px); }
            100% { transform: translateZ(100px) translateY(-50px); }
        }

        @keyframes cloudFloat {
            0%, 100% { transform: translateX(0px) translateY(0px); }
            50% { transform: translateX(100px) translateY(-20px); }
        }

        @keyframes buildingPass {
            0% { transform: translateX(-100px); }
            100% { transform: translateX(100vw); }
        }

        /* === COFFEE JITTERS === */
        .coffee-effect {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 20% 80%, rgba(139, 69, 19, 0.1) 0%, transparent 50%);
            animation: coffeePulse 2s infinite alternate;
            pointer-events: none;
            z-index: 50;
        }

        @keyframes coffeePulse {
            0% { opacity: 0.1; transform: scale(1); }
            100% { opacity: 0.3; transform: scale(1.1); }
        }

        /* === HEARTBEAT EFFECT === */
        .heartbeat {
            position: fixed;
            top: 50%;
            left: 50%;
            width: 100px;
            height: 100px;
            background: radial-gradient(circle, rgba(255,0,0,0.3) 0%, transparent 70%);
            border-radius: 50%;
            animation: heartbeat 1.5s infinite;
            pointer-events: none;
            z-index: 25;
        }

        @keyframes heartbeat {
            0% { transform: translate(-50%, -50%) scale(0.8); opacity: 0; }
            50% { transform: translate(-50%, -50%) scale(1.2); opacity: 0.3; }
            100% { transform: translate(-50%, -50%) scale(0.8); opacity: 0; }
        }
    </style>
</head>
<body>
    <div class="pov-body">
        <!-- Flying Scene -->
        <div class="flying-scene">
            <!-- Clouds -->
            <div class="cloud" style="top: 20%; left: 10%; width: 150px; height: 60px;"></div>
            <div class="cloud" style="top: 40%; left: 40%; width: 200px; height: 80px;"></div>
            <div class="cloud" style="top: 60%; left: 70%; width: 180px; height: 70px;"></div>
            
            <!-- Buildings -->
            <div class="building" style="left: 5%; width: 80px; height: 200px;"></div>
            <div class="building" style="left: 15%; width: 120px; height: 300px;"></div>
            <div class="building" style="left: 30%; width: 90px; height: 250px;"></div>
        </div>

        <!-- Left Hand with Cigarette -->
        <div class="left-hand">
            <div class="hand"></div>
            <div class="cigarette"></div>
            <div class="ash"></div>
            <div class="smoke"></div>
            <div class="smoke" style="animation-delay: 1s;"></div>
            <div class="smoke" style="animation-delay: 2s;"></div>
        </div>

        <!-- Right Hand with Phone -->
        <div class="right-hand">
            <div class="hand"></div>
            <div class="phone">
                <div class="phone-screen">
                    <div class="phone-content">
                        <div style="text-align: center; margin-bottom: 5px;">
                            <strong>ECS DEPLOYMENT</strong>
                        </div>
                        <div style="background: rgba(0,0,0,0.3); padding: 3px; border-radius: 2px; margin: 2px 0;">
                            ✅ Python Flask<br>
                            ✅ Docker<br>
                            ✅ Terraform<br>
                            ✅ AWS ECS<br>
                        </div>
                        <div style="margin-top: 5px; font-size: 5px;">
                            Status: <span style="color: #00ff00;">RUNNING</span><br>
                            Health: <span style="color: #00ff00;">OK</span><br>
                            Load: <span style="color: #ffff00;">87%</span>
                        </div>
                        <div style="margin-top: 8px; text-align: center;">
                            <a href="/api/health" style="color: #00ffff; font-size: 5px;">HEALTH CHECK</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Effects -->
        <div class="coffee-effect"></div>
        <div class="heartbeat"></div>
    </div>

    <script>
        // Enhanced shaky cam based on mouse movement
        document.addEventListener('mousemove', (e) => {
            const body = document.querySelector('.pov-body');
            const x = (e.clientX / window.innerWidth - 0.5) * 4;
            const y = (e.clientY / window.innerHeight - 0.5) * 4;
            body.style.transform = `translate(${x}px, ${y}px) rotate(${x * 0.1}deg)`;
        });

        // Random cigarette ash drops
        setInterval(() => {
            const ash = document.createElement('div');
            ash.className = 'ash';
            ash.style.left = (185 + Math.random() * 10) + 'px';
            ash.style.animationDelay = Math.random() + 's';
            document.querySelector('.left-hand').appendChild(ash);
            
            setTimeout(() => ash.remove(), 5000);
        }, 2000);

        // Phone screen flicker (bad signal simulation)
        setInterval(() => {
            const screen = document.querySelector('.phone-screen');
            screen.style.filter = `hue-rotate(${Math.random() * 360}deg) brightness(${0.8 + Math.random() * 0.4})`;
        }, 3000);

        // Coffee jitter intensity based on time
        setInterval(() => {
            const coffee = document.querySelector('.coffee-effect');
            const intensity = 0.1 + Math.random() * 0.3;
            coffee.style.opacity = intensity;
        }, 1000);

        // Create more smoke occasionally
        setInterval(() => {
            const smoke = document.createElement('div');
            smoke.className = 'smoke';
            smoke.style.left = (190 + Math.random() * 20) + 'px';
            smoke.style.animationDelay = Math.random() * 2 + 's';
            document.querySelector('.left-hand').appendChild(smoke);
            
            setTimeout(() => smoke.remove(), 4000);
        }, 1500);

        // Simulate occasional cough (screen shake)
        setInterval(() => {
            if (Math.random() > 0.7) {
                const body = document.querySelector('.pov-body');
                body.style.animation = 'none';
                setTimeout(() => {
                    body.style.animation = 'shakyCam 0.2s infinite';
                }, 100);
            }
        }, 8000);
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