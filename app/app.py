from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🚀 My ECS Deployment Project</h1>
    <p>This Python app will be deployed to AWS ECS!</p>
    <p><strong>Technology Stack:</strong></p>
    <ul>
        <li>Python Flask</li>
        <li>Docker</li>
        <li>Terraform</li>
        <li>AWS ECS</li>
        <li>GitHub Actions</li>
    </ul>
    <p><a href="/api/health">Check Health Status</a></p>
    '''

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'service': 'Python Flask App',
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/api/info')
def info():
    return jsonify({
        'message': 'This is a simple Python app for AWS ECS deployment',
        'student': 'Your Name',
        'course': 'Networking CA',
        'technology': ['Python', 'Flask', 'Docker', 'AWS', 'Terraform']
    })

if __name__ == '__main__':
    print("Starting Python Flask server...")
    print("Access the app at: http://localhost:3000")
    print("Health check at: http://localhost:3000/api/health")
    app.run(host='0.0.0.0', port=3000, debug=True)