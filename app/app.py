from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<html>
<head>
    <title>BRAIN MELTER 9000</title>
    <style>
        * { 
            margin: 0; padding: 0; box-sizing: border-box; 
            animation-duration: 0.02s !important;
        }
        
        body { 
            background: #000; 
            overflow: hidden;
            font-family: Arial, sans-serif;
            cursor: none;
        }

        /* === HYPE BEAST BACKGROUND === */
        .hype-grid {
            position: fixed;
            width: 500%; height: 500%;
            background: 
                repeating-linear-gradient(90deg, #ff00ff 0px, #ff00ff 10px, transparent 10px, transparent 20px),
                repeating-linear-gradient(0deg, #00ffff 0px, #00ffff 10px, transparent 10px, transparent 20px),
                repeating-linear-gradient(45deg, #ffff00 0px, #ffff00 5px, transparent 5px, transparent 10px);
            animation: gridMove 0.1s infinite linear;
            mix-blend-mode: overlay;
        }
        
        @keyframes gridMove {
            0% { transform: translateX(0px) rotate(0deg); }
            100% { transform: translateX(-100px) rotate(1deg); }
        }

        /* === TRENDING STROBE EFFECT === */
        .strobe-overlay {
            position: fixed;
            width: 100%; height: 100%;
            background: radial-gradient(circle, #ff0000, #00ff00, #0000ff);
            animation: hypeStrobe 0.05s infinite alternate;
            mix-blend-mode: difference;
        }
        
        @keyframes hypeStrobe {
            0% { opacity: 1; filter: hue-rotate(0deg) blur(0px); }
            100% { opacity: 0.3; filter: hue-rotate(180deg) blur(20px); }
        }

        /* === VIRAL TEXT EFFECTS === */
        .hype-text {
            position: fixed;
            font-size: 120px;
            font-weight: 900;
            text-transform: uppercase;
            animation: textHype 0.03s infinite;
            text-shadow: 
                0 0 20px #fff,
                0 0 40px #ff00ff,
                0 0 60px #00ffff;
            mix-blend-mode: overlay;
            z-index: 1000;
        }
        
        @keyframes textHype {
            0% { 
                color: #ff0000; 
                transform: scale(1) skew(10deg, 5deg) rotate(0deg);
                text-shadow: 0 0 50px #ff0000;
            }
            25% { 
                color: #00ff00; 
                transform: scale(1.2) skew(-10deg, -5deg) rotate(5deg);
                text-shadow: 0 0 50px #00ff00;
            }
            50% { 
                color: #0000ff; 
                transform: scale(1.1) skew(15deg, 10deg) rotate(-5deg);
                text-shadow: 0 0 50px #0000ff;
            }
            75% { 
                color: #ffff00; 
                transform: scale(1.3) skew(-15deg, -10deg) rotate(3deg);
                text-shadow: 0 0 50px #ffff00;
            }
            100% { 
                color: #ff00ff; 
                transform: scale(1) skew(10deg, 5deg) rotate(0deg);
                text-shadow: 0 0 50px #ff00ff;
            }
        }

        /* === EMOJI RAIN === */
        .emoji-storm {
            position: fixed;
            width: 100%; height: 100%;
            pointer-events: none;
            font-size: 30px;
            animation: emojiColorShift 0.1s infinite;
        }
        
        @keyframes emojiColorShift {
            0% { filter: hue-rotate(0deg); }
            100% { filter: hue-rotate(360deg); }
        }

        .emoji {
            position: absolute;
            animation: emojiFall 2s linear forwards;
            text-shadow: 0 0 10px currentColor;
        }
        
        @keyframes emojiFall {
            0% { 
                transform: translateY(-100px) rotate(0deg) scale(0.5);
                opacity: 0;
            }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { 
                transform: translateY(100vh) rotate(360deg) scale(1.5);
                opacity: 0;
            }
        }

        /* === TRENDING BADGES === */
        .trending-badge {
            position: fixed;
            padding: 20px 40px;
            background: linear-gradient(45deg, #ff0000, #ffff00, #00ff00, #00ffff, #0000ff, #ff00ff);
            color: white;
            font-weight: 900;
            font-size: 24px;
            border-radius: 50px;
            animation: badgeHype 0.1s infinite alternate;
            mix-blend-mode: overlay;
            z-index: 500;
        }
        
        @keyframes badgeHype {
            0% { 
                transform: scale(1) rotate(0deg);
                box-shadow: 0 0 50px #ff0000;
            }
            100% { 
                transform: scale(1.3) rotate(5deg);
                box-shadow: 0 0 50px #00ffff;
            }
        }

        /* === SOCIAL MEDIA UI ELEMENTS === */
        .ui-overlay {
            position: fixed;
            width: 100%; height: 100%;
            pointer-events: none;
        }

        .notification {
            position: absolute;
            background: rgba(255,255,255,0.9);
            padding: 15px 25px;
            border-radius: 25px;
            font-weight: bold;
            animation: notificationPop 0.5s infinite alternate;
            box-shadow: 0 0 30px currentColor;
        }
        
        @keyframes notificationPop {
            0% { transform: scale(0.8) translateX(-100px); opacity: 0; }
            100% { transform: scale(1) translateX(0px); opacity: 1; }
        }

        /* === HYPE CONTENT BOX === */
        .main-content {
            position: fixed;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0,0,0,0.8);
            padding: 60px 80px;
            border: 8px solid;
            border-image: linear-gradient(45deg, #ff0000, #00ff00, #0000ff, #ffff00, #ff00ff) 1;
            animation: contentPulse 0.05s infinite alternate;
            z-index: 10000;
            text-align: center;
            backdrop-filter: blur(10px);
        }
        
        @keyframes contentPulse {
            0% { 
                box-shadow: 
                    0 0 100px #ff0000,
                    0 0 200px #00ff00,
                    inset 0 0 100px #0000ff;
            }
            100% { 
                box-shadow: 
                    0 0 100px #00ffff,
                    0 0 200px #ff00ff,
                    inset 0 0 100px #ffff00;
            }
        }

        .main-title {
            font-size: 4em;
            background: linear-gradient(45deg, #ff0000, #ffff00, #00ff00, #00ffff, #0000ff, #ff00ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: titleHype 0.03s infinite;
            margin-bottom: 30px;
        }
        
        @keyframes titleHype {
            0% { transform: scale(1) skew(5deg, 2deg); }
            50% { transform: scale(1.1) skew(-5deg, -2deg); }
            100% { transform: scale(1) skew(5deg, 2deg); }
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin: 30px 0;
        }
        
        .stat {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            animation: statFlash 0.1s infinite;
            border: 2px solid;
        }
        
        @keyframes statFlash {
            0% { border-color: #ff0000; background: #00ff00; }
            33% { border-color: #00ff00; background: #0000ff; }
            66% { border-color: #0000ff; background: #ffff00; }
            100% { border-color: #ffff00; background: #ff0000; }
        }
    </style>
</head>
<body>
    <div class="hype-grid"></div>
    <div class="strobe-overlay"></div>
    <div class="emoji-storm" id="emojiContainer"></div>
    <div class="ui-overlay" id="uiOverlay"></div>

    <!-- HYPE TEXT OVERLAYS -->
    <div class="hype-text" style="top: 5%; left: 5%;">TRENDING</div>
    <div class="hype-text" style="top: 15%; right: 5%;">VIRAL</div>
    <div class="hype-text" style="bottom: 20%; left: 10%;">HYPE</div>
    <div class="hype-text" style="bottom: 10%; right: 15%;">FIRE</div>
    <div class="hype-text" style="top: 50%; left: 2%;">LIT</div>
    <div class="hype-text" style="top: 60%; right: 2%;">GOATED</div>

    <!-- TRENDING BADGES -->
    <div class="trending-badge" style="top: 30%; left: 20%;">#1 TRENDING</div>
    <div class="trending-badge" style="top: 70%; right: 25%;">BREAKING</div>
    <div class="trending-badge" style="bottom: 30%; left: 15%;">HOT 🔥</div>

    <!-- MAIN CONTENT -->
    <div class="main-content">
        <div class="main-title">🚀 ECS GOATED 🚀</div>
        
        <div class="stats-grid">
            <div class="stat">🔥 2.4M VIEWS</div>
            <div class="stat">💫 500K LIKES</div>
            <div class="stat">⚡ 100K SHARES</div>
            <div class="stat">🎯 #1 TRENDING</div>
        </div>

        <div style="font-size: 1.5em; margin: 20px 0; animation: textHype 0.05s infinite;">
            PYTHON 🐍 × DOCKER 🐳 × TERRAFORM ☁️ × AWS ⚡
        </div>

        <a href="/api/health" style="
            display: inline-block;
            padding: 20px 40px;
            background: linear-gradient(45deg, #ff0000, #ffff00, #00ff00);
            color: white;
            text-decoration: none;
            font-weight: 900;
            font-size: 1.5em;
            border-radius: 50px;
            animation: badgeHype 0.05s infinite;
            margin-top: 20px;
        ">
            🔍 CHECK STATS
        </a>
    </div>

    <script>
        // EMOJI STORM GENERATOR
        const emojis = ['🔥','💫','⚡','🎯','🚀','💥','🌟','🎉','👑','💎','🎊','❤️','✨','⭐'];
        const emojiContainer = document.getElementById('emojiContainer');
        
        function createEmojiStorm() {
            for (let i = 0; i < 50; i++) {
                const emoji = document.createElement('div');
                emoji.className = 'emoji';
                emoji.textContent = emojis[Math.floor(Math.random() * emojis.length)];
                emoji.style.left = Math.random() * 100 + 'vw';
                emoji.style.animationDelay = Math.random() * 2 + 's';
                emoji.style.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
                emoji.style.fontSize = (20 + Math.random() * 30) + 'px';
                emojiContainer.appendChild(emoji);
                
                setTimeout(() => emoji.remove(), 2000);
            }
        }
        setInterval(createEmojiStorm, 100);

        // SOCIAL MEDIA NOTIFICATIONS
        const notifications = [
            "🔥 2.4M VIEWS!", "💫 TRENDING #1", "⚡ 500K LIKES", 
            "🎯 GOATED AF", "🚀 VIRAL POST", "💎 BREAKING RECORDS"
        ];
        const uiOverlay = document.getElementById('uiOverlay');
        
        function spawnNotification() {
            const notif = document.createElement('div');
            notif.className = 'notification';
            notif.textContent = notifications[Math.floor(Math.random() * notifications.length)];
            notif.style.top = Math.random() * 80 + 10 + '%';
            notif.style.left = Math.random() * 80 + 10 + '%';
            notif.style.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
            notif.style.animationDelay = Math.random() + 's';
            uiOverlay.appendChild(notif);
            
            setTimeout(() => notif.remove(), 2000);
        }
        setInterval(spawnNotification, 200);

        // BACKGROUND COLOR CYCLING
        setInterval(() => {
            document.body.style.background = `hsl(${Math.random() * 360}, 100%, ${10 + Math.random() * 20}%)`;
        }, 100);

        // HYPE TEXT MOVEMENT
        setInterval(() => {
            const hypeTexts = document.querySelectorAll('.hype-text');
            hypeTexts.forEach(text => {
                text.style.top = Math.random() * 90 + 5 + '%';
                text.style.left = Math.random() * 90 + 5 + '%';
                text.style.fontSize = (80 + Math.random() * 80) + 'px';
            });
        }, 500);

        // TRENDING BADGE MOVEMENT
        setInterval(() => {
            const badges = document.querySelectorAll('.trending-badge');
            badges.forEach(badge => {
                badge.style.top = Math.random() * 80 + 10 + '%';
                badge.style.left = Math.random() * 80 + 10 + '%';
            });
        }, 300);

        // MOUSE INTERACTION HYPE
        document.addEventListener('mousemove', (e) => {
            for (let i = 0; i < 10; i++) {
                const sparkle = document.createElement('div');
                sparkle.textContent = '✨';
                sparkle.style.position = 'fixed';
                sparkle.style.left = (e.clientX + Math.random() * 100 - 50) + 'px';
                sparkle.style.top = (e.clientY + Math.random() * 100 - 50) + 'px';
                sparkle.style.fontSize = (20 + Math.random() * 30) + 'px';
                sparkle.style.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
                sparkle.style.animation = `emojiFall ${1 + Math.random()}s forwards`;
                sparkle.style.zIndex = '1000';
                document.body.appendChild(sparkle);
                setTimeout(() => sparkle.remove(), 1000);
            }
        });

        // RANDOM SOUND EFFECT VISUALS
        setInterval(() => {
            const visualBeat = document.createElement('div');
            visualBeat.style.position = 'fixed';
            visualBeat.style.inset = '0';
            visualBeat.style.background = `radial-gradient(circle, 
                hsl(${Math.random() * 360}, 100%, 50%) 0%, 
                transparent 70%)`;
            visualBeat.style.animation = 'hypeStrobe 0.1s forwards';
            visualBeat.style.mixBlendMode = 'overlay';
            document.body.appendChild(visualBeat);
            setTimeout(() => visualBeat.remove(), 100);
        }, 150);

        // VIEW COUNT INCREMENT (FAKE HYPE)
        let viewCount = 2400000;
        setInterval(() => {
            viewCount += Math.floor(Math.random() * 1000);
            document.querySelector('.stat').textContent = `🔥 ${(viewCount/1000000).toFixed(1)}M VIEWS`;
        }, 100);

        // AUTO-REFRESH FOR INFINITE SCROLL EFFECT
        setTimeout(() => {
            window.location.reload();
        }, 15000);
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