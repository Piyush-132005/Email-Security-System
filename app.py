from importlib.resources import open_text
from flask import Flask, render_template, request, jsonify
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os
import webbrowser
import threading
import time
import socket

# Download NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

app = Flask(__name__)

# Change to project directory
os.chdir(r'c:\Users\Piyush\Desktop\AI and ML Projects\Email spam Classification')

# Global variables for models
model = None
vectorizer = None
models_loaded = False

def load_models():
    """Load trained models and vectorizer"""
    global model, vectorizer, models_loaded
    try:
        print("Loading models...")
        with open('linear_svm_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        with open('tfidf_vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        
        models_loaded = True
        print("✅ Models loaded successfully!")
        return True
    except FileNotFoundError:
        print("❌ Model files not found!")
        models_loaded = False
        return False

def preprocess_text(text):
    """Preprocess email text"""
    # Lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords and apply stemming
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words and len(word) > 2]
    
    return ' '.join(tokens)

def validate_email_input(email_text):
    """Validate email input (ALLOW phishing content)"""
    if not email_text or email_text.strip() == "":
        return False, "Please enter email content!"

    if len(email_text.strip()) < 5:
        return False, "Email content too short!"

    return True, ""


@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict email classification"""
    if not models_loaded:
        return jsonify({'error': 'Models not loaded!'}), 500
    
    data = request.json
    email_text = data.get('email', '')
    
    # Validate input
    is_valid, error_msg = validate_email_input(email_text)
    if not is_valid:
        return jsonify({'error': error_msg}), 400
    
    try:
        # Preprocess
        processed_text = preprocess_text(email_text)
        
        # Check if processed text is empty
        if not processed_text or len(processed_text.strip()) == 0:
            return jsonify({'error': 'Email text contains no meaningful words!\nTry entering a real email.'}), 400
        
        # Vectorize
        vectorized = vectorizer.transform([processed_text])
        
        # Predict
        prediction = model.predict(vectorized)[0]
        
        # 🔐 Rule-based phishing override (IMPORTANT)
        phishing_keywords = ['verify', 'account', 'password', 'login', 'click', 'bank', 'urgent', 'immediately', 'suspend', 'update']
        has_link = ("http://" in email_text) or ("https://" in email_text)
        if prediction == 0:  # model says HAM
            if has_link and any(word in email_text for word in phishing_keywords):
                prediction = 2
        
            safe_phrases = [
            "we never ask for otp",
            "informational purposes only",
            "no action is required"
            ]

            if any(phrase in email_text.lower() for phrase in safe_phrases):
                prediction = 0  # force HAM
            prediction = 0  # force HAM
        
        # Get probability if available
        if hasattr(model, 'predict_proba'):
            proba = model.predict_proba(vectorized)[0]
            confidence = max(proba) * 100
        else:
            confidence = None
        
        # Prepare response
        if prediction == 0:
            classification = "LEGITIMATE EMAIL"
            status = "legitimate"
            emoji = "✅"
            color = "#2ecc71"  # Green
            advice = "🟢 This email appears to be LEGITIMATE<br>✓ Safe to open and interact with"
        else:
            classification = "SPAM/PHISHING EMAIL"
            status = "spam"
            emoji = "⚠️"
            color = "#e74c3c"  # Red
            advice = "🔴 This email appears to be SPAM/PHISHING<br>✗ Be cautious - do not click links<br>✗ Do not provide personal information"
        
        return jsonify({
            'classification': classification,
            'status': status,
            'emoji': emoji,
            'color': color,
            'confidence': round(confidence, 2) if confidence else None,
            'advice': advice,
            'success': True
        })
        
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

def get_local_ip():
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def open_browser():
    """Open browser after a short delay to let Flask start (only once)"""
    time.sleep(2)
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    # Load models on startup
    if load_models():
        local_ip = get_local_ip()
        print("\n" + "="*70)
        print("🚀 EMAIL SECURITY SYSTEM STARTED!")
        print("="*70)
        print(f"🖥️  Desktop (localhost):  http://localhost:5000")
        print(f"📱 Mobile (same WiFi):   http://{local_ip}:5000")
        print("="*70 + "\n")
        
        # Only open browser on the main process, not on reloader
        import os
        if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
            print("📱 Opening browser automatically on desktop...")
            browser_thread = threading.Thread(target=open_browser, daemon=True)
            browser_thread.start()
        
        app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=True)
    else:
        print("❌ Failed to load models. Please run the notebook first.")
