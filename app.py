import os
import uuid
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from agents import DesignAgent
from vision import analyze_room_image

app = Flask(__name__)
# Use an absolute path based on the application's root path for robust uploads
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize Agent
design_agent = DesignAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
        
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if file:
        filename = secure_filename(file.filename)
        # Fallback if secure_filename removes all characters (e.g. non-ASCII names)
        if not filename:
            filename = f"upload_{uuid.uuid4().hex[:8]}.jpg"
            
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # 1. Vision API Analysis
        room_features = analyze_room_image(filepath)
        
        # 2. Agentic AI Recommendations
        user_preferences = request.form.get('preferences', 'Modern minimalist')
        recommendations = design_agent.generate_recommendations(room_features, user_preferences)
        
        return jsonify({
            'success': True,
            'image_url': f'/static/uploads/{filename}',
            'features': room_features,
            'recommendations': recommendations
        })

@app.route('/api/chat', methods=['POST'])
def chat():
    # Use robust method to parse JSON to avoid AttributeError if data is missing
    data = request.get_json(silent=True) or {}
    user_message = data.get('message', '')
    context = data.get('context', {})
    
    response = design_agent.chat(user_message, context)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
