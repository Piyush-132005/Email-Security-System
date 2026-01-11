# 🛡️ Email Security System - Spam & Phishing Detector

A modern, machine learning-powered email security system that detects spam and phishing emails with 97.29% accuracy! Built with Flask and Scikit-learn, accessible on desktop and mobile.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

✅ **Real-time Email Analysis** - Instant spam/phishing detection  
✅ **High Accuracy** - 97.29% accuracy with Linear SVM  
✅ **Web Interface** - Beautiful, responsive design  
✅ **Multi-Device Support** - Works on desktop and mobile (same WiFi)  
✅ **Email Validation** - Ensures valid email input  
✅ **Color-coded Results** - 🟢 Safe or 🔴 Dangerous  
✅ **No Installation Required** - Just run and go!

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/email-security-system.git
cd email-security-system
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Open in browser**
- Desktop: `http://localhost:5000`
- Mobile (same WiFi): `http://YOUR_IP:5000` (shown in terminal)

---

## 📖 How to Use

### Step 1: Start the App
```bash
python app.py
```

### Step 2: Paste Email
- Copy email content from Gmail, Outlook, etc.
- Paste into the text box

### Step 3: Click Predict
- Click the **PREDICT** button
- Get instant classification

### Step 4: View Results
- 🟢 **Green** = Legitimate Email (Safe to open)
- 🔴 **Red** = Spam/Phishing (Be cautious!)

---

## 🤖 Machine Learning Model

### Algorithm
**Linear SVM (Support Vector Machine)**

### Performance Metrics
| Metric | Value |
|--------|-------|
| Accuracy | 97.29% |
| Precision | 94.64% |
| Recall | 82.81% |
| F1-Score | 0.8833 |

### Training Data
- **Total Emails**: 5,157 (cleaned)
- **Training Samples**: 4,125
- **Testing Samples**: 1,032
- **Features**: 3,000 (TF-IDF)

### Text Processing
- URL removal (regex)
- Email address removal
- Special character cleaning
- Stemming (Porter Stemmer)
- Stopword removal (NLTK)
- TF-IDF vectorization

---

## 📱 Mobile Access

### Same WiFi Network
1. Run `python app.py` on your computer
2. Note the IP address shown in terminal (e.g., `192.168.1.100`)
3. On your mobile device, open: `http://192.168.1.100:5000`
4. Use the app on your phone!

**Requirements:**
- Mobile and computer on same WiFi
- Port 5000 accessible (usually default)

---

## 📁 Project Structure

```
email-security-system/
├── app.py                          # Flask backend server
├── requirements.txt                # Python dependencies
├── Combined-Email-Security.ipynb   # ML model training notebook
├── email.csv                       # Training dataset
├── templates/
│   └── index.html                  # Web interface
├── linear_svm_model.pkl            # Trained model
├── tfidf_vectorizer.pkl            # Feature vectorizer
├── all_email_security_models.pkl   # Backup of all models
└── README.md                       # This file
```

---

## 🔒 Security Notes

⚠️ **Educational Purpose**
- This is an educational project
- Use for learning and testing only
- Not recommended for production email filtering

✅ **Best Practices**
- Never download attachments from suspicious emails
- Always verify sender email addresses
- Use official email provider filters in addition
- Enable two-factor authentication on accounts

---

## 🛠️ Troubleshooting

### Port 5000 Already in Use
Edit `app.py` line with:
```python
app.run(debug=False, host='0.0.0.0', port=8000)  # Change to 8000
```

### NLTK Data Missing
```bash
python -m nltk.downloader punkt stopwords
```

### Models Not Found Error
Ensure these files exist in the project directory:
- `linear_svm_model.pkl`
- `tfidf_vectorizer.pkl`

### Cannot Access on Mobile
- Verify both devices on same WiFi
- Check firewall settings
- Use the IP shown in terminal (not localhost)

---

## 📊 Test Examples

### ✅ Legitimate Email
```
From: john.doe@company.com
To: sarah@company.com
Subject: Q1 Project Update

Dear Sarah,

I hope this email finds you well. I wanted to follow up on our meeting yesterday regarding the Q1 project proposal.

Your insights were valuable, and I believe we can move forward with the implementation plan.

Best regards,
John
```

### ❌ Spam Email
```
CONGRATULATIONS!!! YOU HAVE WON $1,000,000!!!

Click HERE NOW to claim your prize!!!

Act fast - offer limited!!!

Verify your account at: www.fake-site.net

Call 1-800-WIN-NOW
```

---

## 🎓 Learning Resources

- **Machine Learning**: Classification, model evaluation
- **NLP**: Text preprocessing, TF-IDF vectorization
- **Web Development**: Flask framework, HTML/CSS/JavaScript
- **Python**: scikit-learn, NLTK, pandas

---

## 📝 Technical Stack

**Backend**
- Flask 3.1 (Python web framework)
- Scikit-learn 1.5 (Machine learning)
- NLTK 3.9 (Natural language processing)
- Pandas 2.2 (Data manipulation)

**Frontend**
- HTML5 (semantic markup)
- CSS3 (responsive design)
- JavaScript (vanilla, no frameworks)

**ML Libraries**
- XGBoost (ensemble method)
- LightGBM (gradient boosting)

---

## 🤝 Contributing

Contributions welcome! 

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👨‍💻 Author

Created for educational purposes as a final year university project.

---

## ⭐ Support

If you found this helpful, please star the repository! ⭐

---

## 📮 Contact & Feedback

Have questions or suggestions? Feel free to:
- Open an issue
- Submit a pull request
- Fork and improve!

---

**Happy email filtering! 🛡️✨**
