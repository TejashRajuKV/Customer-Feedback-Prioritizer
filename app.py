#!/usr/bin/env python3
"""
🎯 Customer Feedback Prioritizer - AI-Powered Web Application
Modern web app with real-time feedback analysis and intelligent prioritization
"""

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import json
import datetime
import logging
from pathlib import Path

# Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)
CORS(app)

# Storage
feedback_file = Path("customer_feedback.json")
if not feedback_file.exists():
    feedback_file.write_text("[]")

def load_feedback():
    try:
        return json.loads(feedback_file.read_text())
    except:
        return []

def save_feedback(feedback_list):
    try:
        feedback_file.write_text(json.dumps(feedback_list, indent=2))
        return True
    except:
        return False

def analyze_feedback(text, category="general"):
    """AI-powered feedback analysis"""
    text = text.lower()
    
    # Pattern matching for intelligent analysis
    security_patterns = ['hack', 'breach', 'security', 'unauthorized', 'compromised']
    system_failure_patterns = ['not work', 'down', 'crash', 'broken', 'stuck', 'unavailable']
    performance_patterns = ['slow', 'lag', 'delay', 'loading', 'performance']
    
    urgency_contexts = [
        ('losing money', 10), ('revenue impact', 10), ('security', 10),
        ('critical', 9), ('urgent', 8), ('important', 7),
        ('problem', 6), ('issue', 5), ('suggestion', 2)
    ]
    
    impact_contexts = [
        ('all users', 10), ('everyone', 10), ('many users', 8),
        ('customers', 7), ('users', 6), ('some', 4)
    ]
    
    # Score calculation
    urgency_score = 3
    impact_score = 3
    
    # Security critical
    if any(pattern in text for pattern in security_patterns):
        urgency_score, impact_score, theme = 10, 10, "Security Critical"
    # System failure
    elif any(pattern in text for pattern in system_failure_patterns):
        urgency_score, impact_score, theme = 8, 8, "System Failure"
    else:
        # Contextual scoring
        for context, score in urgency_contexts:
            if context in text:
                urgency_score = max(urgency_score, score)
                break
        
        for context, score in impact_contexts:
            if context in text:
                impact_score = max(impact_score, score)
                break
        
        # Theme detection
        if any(pattern in text for pattern in performance_patterns):
            theme = "Performance"
        elif any(word in text for word in ['bug', 'error', 'problem']):
            theme = "Bug"
        elif any(word in text for word in ['design', 'ui', 'ux', 'interface']):
            theme = "UI/UX"
        elif any(word in text for word in ['feature', 'add', 'want', 'request']):
            theme = "Feature"
        else:
            theme = "General"
    
    priority_score = min(10, max(urgency_score, impact_score, (urgency_score + impact_score) // 2))
    confidence = min(95, 60 + len(text) // 10)
    assigned_team = get_team_assignment(priority_score, theme)
    
    return {
        'urgency': urgency_score,
        'impact': impact_score,
        'priority': priority_score,
        'theme': theme,
        'confidence': confidence,
        'assigned_team': assigned_team
    }

def get_team_assignment(priority_score, theme):
    """Smart team assignment based on priority and theme"""
    theme_lower = theme.lower()
    
    if theme_lower == 'security critical':
        return "🚨 Security Team + Engineering + Product"
    elif theme_lower == 'system failure':
        return "🔧 Engineering Team (URGENT)"
    elif priority_score >= 8:
        return "Engineering + Product"
    elif priority_score >= 6:
        if theme_lower in ['ui/ux', 'design']:
            return "Design Team"
        elif theme_lower in ['bug', 'performance']:
            return "Engineering Team"
        else:
            return "Product Team"
    else:
        return "Product Team"

@app.route('/')
def customer_form():
    """Customer feedback form with modern UI"""
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Customer Feedback Prioritizer</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Inter', sans-serif;
            background: #0a0a0f;
            background-image: 
                radial-gradient(circle at 25% 25%, rgba(79, 70, 229, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 75% 75%, rgba(236, 72, 153, 0.15) 0%, transparent 50%);
            color: #e2e8f0;
            min-height: 100vh;
            padding: 20px;
            animation: fadeInUp 0.8s ease-out;
        }
        
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
            overflow: hidden;
            animation: scaleIn 0.8s ease-out 0.2s both;
        }
        
        @keyframes scaleIn { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }
        
        .header {
            background: linear-gradient(135deg, rgba(79, 70, 229, 0.2) 0%, rgba(236, 72, 153, 0.2) 100%);
            color: white;
            padding: 50px 40px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 3.2em;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #a78bfa 50%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
        }
        
        .header p { font-size: 1.3em; color: #cbd5e1; }
        
        .form-container { padding: 50px; }
        
        .form-group {
            margin-bottom: 30px;
            animation: slideInLeft 0.6s ease-out both;
        }
        
        @keyframes slideInLeft { from { opacity: 0; transform: translateX(-30px); } to { opacity: 1; transform: translateX(0); } }
        
        label {
            display: block;
            margin-bottom: 12px;
            font-weight: 600;
            color: #ffffff;
            font-size: 1.1rem;
        }
        
        input, textarea, select {
            width: 100%;
            padding: 18px 20px;
            background: rgba(30, 41, 59, 0.5);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            font-size: 16px;
            color: #e2e8f0;
            transition: all 0.4s ease;
        }
        
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: rgba(167, 139, 250, 0.5);
            box-shadow: 0 0 0 3px rgba(167, 139, 250, 0.1);
            transform: translateY(-2px);
        }
        
        textarea { min-height: 140px; resize: vertical; }
        
        .ai-analysis {
            margin-top: 20px;
            padding: 25px;
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid rgba(167, 139, 250, 0.3);
            border-radius: 16px;
            display: none;
        }
        
        .analysis-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .metric {
            background: rgba(15, 23, 42, 0.7);
            padding: 20px 15px;
            border-radius: 12px;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .metric:hover { transform: translateY(-4px); }
        
        .metric-value {
            font-size: 2.2em;
            font-weight: 800;
            margin-bottom: 8px;
        }
        
        .urgency { background: linear-gradient(135deg, #ef4444, #f87171); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .impact { background: linear-gradient(135deg, #f59e0b, #fbbf24); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .priority { background: linear-gradient(135deg, #a855f7, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .confidence { background: linear-gradient(135deg, #10b981, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        
        .submit-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px 40px;
            border: none;
            border-radius: 16px;
            font-size: 1.2rem;
            font-weight: 700;
            cursor: pointer;
            width: 100%;
            margin-top: 20px;
            transition: all 0.4s ease;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        }
        
        .submit-btn:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 20px 50px rgba(102, 126, 234, 0.4);
        }
        
        .message {
            padding: 20px;
            border-radius: 16px;
            margin-top: 20px;
            display: none;
        }
        
        .success { background: rgba(34, 197, 94, 0.2); color: #86efac; border-left: 4px solid #22c55e; }
        .error { background: rgba(239, 68, 68, 0.2); color: #fca5a5; border-left: 4px solid #ef4444; }
        
        .team-credits {
            margin-top: 50px;
            padding: 30px;
            background: rgba(15, 23, 42, 0.6);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
        }
        
        .team-credits h3 {
            color: #ffffff;
            margin-bottom: 20px;
            font-size: 1.3rem;
            font-weight: 600;
        }
        
        .team-member {
            display: inline-block;
            margin: 10px 20px;
            padding: 15px 20px;
            background: rgba(30, 41, 59, 0.7);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }
        
        .team-member:hover {
            transform: translateY(-2px);
            border-color: rgba(167, 139, 250, 0.3);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        }
        
        .member-name {
            color: #ffffff;
            font-weight: 700;
            font-size: 1.1rem;
            margin-bottom: 5px;
        }
        
        .member-role {
            color: #a78bfa;
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        .project-info {
            margin-top: 20px;
            color: #94a3b8;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Customer Feedback</h1>
            <p>AI-powered feedback prioritization for product teams</p>
        </div>
        
        <div class="form-container">
            <form id="feedbackForm">
                <div class="form-group">
                    <label for="name">Your Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                
                <div class="form-group">
                    <label for="email">Email Address</label>
                    <input type="email" id="email" name="email" required>
                </div>
                
                <div class="form-group">
                    <label for="category">Feedback Category</label>
                    <select id="category" name="category" required>
                        <option value="">Select a category...</option>
                        <option value="bug">🐛 Bug Report</option>
                        <option value="feature">✨ Feature Request</option>
                        <option value="performance">⚡ Performance Issue</option>
                        <option value="ui">🎨 UI/UX Feedback</option>
                        <option value="general">💬 General Feedback</option>
                        <option value="complaint">😤 Complaint</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="feedback">Your Feedback</label>
                    <textarea id="feedback" name="feedback" 
                              placeholder="Describe your feedback in detail. The AI will analyze it as you type..."
                              required></textarea>
                    
                    <div id="aiAnalysis" class="ai-analysis">
                        <h3>🤖 AI Analysis</h3>
                        <div class="analysis-grid">
                            <div class="metric">
                                <div class="metric-value urgency" id="urgencyScore">-</div>
                                <div>Urgency</div>
                            </div>
                            <div class="metric">
                                <div class="metric-value impact" id="impactScore">-</div>
                                <div>Impact</div>
                            </div>
                            <div class="metric">
                                <div class="metric-value priority" id="priorityScore">-</div>
                                <div>Priority</div>
                            </div>
                            <div class="metric">
                                <div class="metric-value confidence" id="confidenceScore">-</div>
                                <div>Confidence</div>
                            </div>
                        </div>
                        <div>
                            <strong>Theme:</strong> <span id="theme">-</span><br>
                            <strong>Assigned Team:</strong> <span id="assignedTeam">-</span>
                        </div>
                    </div>
                </div>
                
                <button type="submit" class="submit-btn" id="submitBtn">
                    Submit Feedback
                </button>
            </form>
            
            <div class="message success" id="successMessage">
                <strong>✅ Thank you!</strong><br>
                Your feedback has been received and prioritized.
            </div>
            
            <div class="message error" id="errorMessage">
                <strong>❌ Error</strong><br>
                <span id="errorText">Please try again.</span>
            </div>
            
            <div class="team-credits">
                <h3>👥 Created by</h3>
                <div class="team-member">
                    <div class="member-name">Tejash Raju K V</div>
                    <div class="member-role">Full-Stack Developer & AI Engineer</div>
                </div>
                <div class="team-member">
                    <div class="member-name">Amrutha V</div>
                    <div class="member-role">UI/UX Designer & Frontend Developer</div>
                </div>
                <div class="project-info">
                    Built with ❤️ for Product Space Hackathon • AI-Powered Customer Feedback Prioritizer
                </div>
            </div>
        </div>
    </div>
    
    <script>
        let analysisTimeout;
        
        document.getElementById('feedback').addEventListener('input', function() {
            const feedback = this.value.trim();
            if (feedback.length < 10) {
                document.getElementById('aiAnalysis').style.display = 'none';
                return;
            }
            
            clearTimeout(analysisTimeout);
            document.getElementById('aiAnalysis').style.display = 'block';
            
            analysisTimeout = setTimeout(() => {
                analyzeText(feedback);
            }, 800);
        });
        
        async function analyzeText(text) {
            try {
                const category = document.getElementById('category').value;
                const response = await fetch('/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ feedback: text, category: category })
                });
                
                if (response.ok) {
                    const analysis = await response.json();
                    document.getElementById('urgencyScore').textContent = analysis.urgency || '-';
                    document.getElementById('impactScore').textContent = analysis.impact || '-';
                    document.getElementById('priorityScore').textContent = analysis.priority || '-';
                    document.getElementById('confidenceScore').textContent = (analysis.confidence || 0) + '%';
                    document.getElementById('theme').textContent = analysis.theme || '-';
                    document.getElementById('assignedTeam').textContent = analysis.assigned_team || '-';
                }
            } catch (error) {
                console.error('Analysis error:', error);
            }
        }
        
        document.getElementById('feedbackForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            document.getElementById('submitBtn').disabled = true;
            document.getElementById('successMessage').style.display = 'none';
            document.getElementById('errorMessage').style.display = 'none';
            
            try {
                const response = await fetch('/submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    document.getElementById('successMessage').style.display = 'block';
                    document.getElementById('feedbackForm').reset();
                    document.getElementById('aiAnalysis').style.display = 'none';
                } else {
                    document.getElementById('errorMessage').style.display = 'block';
                }
            } catch (error) {
                document.getElementById('errorMessage').style.display = 'block';
            } finally {
                document.getElementById('submitBtn').disabled = false;
            }
        });
    </script>
</body>
</html>
    """)

@app.route('/analyze', methods=['POST'])
def analyze_endpoint():
    try:
        data = request.json
        feedback_text = data.get('feedback', '')
        category = data.get('category', '')
        
        if not feedback_text:
            return jsonify({'error': 'No feedback text provided'}), 400
        
        analysis = analyze_feedback(feedback_text, category)
        return jsonify(analysis)
        
    except Exception as e:
        logger.error(f"Analysis error: {e}")
        return jsonify({'error': 'Analysis failed'}), 500

@app.route('/submit', methods=['POST'])
def submit_feedback():
    try:
        data = request.json
        
        required_fields = ['name', 'email', 'feedback', 'category']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        analysis = analyze_feedback(data['feedback'], data['category'])
        
        feedback_entry = {
            'id': datetime.datetime.now().isoformat(),
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'name': data['name'],
            'email': data['email'],
            'category': data['category'],
            'feedback': data['feedback'],
            'analysis': analysis
        }
        
        feedback_list = load_feedback()
        feedback_list.append(feedback_entry)
        
        if save_feedback(feedback_list):
            return jsonify({'success': True, 'message': 'Feedback submitted successfully'})
        else:
            return jsonify({'error': 'Failed to save feedback'}), 500
            
    except Exception as e:
        logger.error(f"Submission error: {e}")
        return jsonify({'error': 'Failed to submit feedback'}), 500

@app.route('/internal/dashboard')
def dashboard():
    """Internal dashboard with modern UI"""
    feedback_list = load_feedback()
    feedback_list.sort(key=lambda x: x.get('analysis', {}).get('priority', 0), reverse=True)
    
    dashboard_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>📊 Customer Feedback Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background: #0a0a0f;
            background-image: 
                radial-gradient(circle at 25% 25%, rgba(79, 70, 229, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 75% 75%, rgba(236, 72, 153, 0.15) 0%, transparent 50%);
            color: #e2e8f0;
            min-height: 100vh;
            padding: 20px;
            animation: fadeInUp 0.8s ease-out;
        }}
        
        @keyframes fadeInUp {{ from {{ opacity: 0; transform: translateY(30px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        
        .header {{
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: white;
            padding: 40px;
            border-radius: 20px;
            margin-bottom: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #a78bfa 50%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}
        
        .stats {{
            display: flex;
            gap: 25px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }}
        
        .stat {{
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 16px;
            flex: 1;
            min-width: 200px;
            text-align: center;
            transition: all 0.3s ease;
        }}
        
        .stat:hover {{ transform: translateY(-4px); }}
        
        .stat h3 {{ color: #ffffff; font-weight: 600; margin-bottom: 10px; }}
        
        .stat p {{
            font-size: 2.5em;
            font-weight: 800;
            margin: 10px 0;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .feedback-item {{
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 20px 0;
            padding: 25px;
            border-radius: 16px;
            transition: all 0.3s ease;
        }}
        
        .feedback-item:hover {{ transform: translateY(-4px); }}
        
        .priority-critical {{ border-left: 4px solid #ef4444; }}
        .priority-high {{ border-left: 4px solid #f59e0b; }}
        .priority-medium {{ border-left: 4px solid #eab308; }}
        .priority-low {{ border-left: 4px solid #22c55e; }}
        
        .analysis {{
            background: rgba(30, 41, 59, 0.5);
            padding: 20px;
            margin-top: 15px;
            border-radius: 12px;
        }}
        
        .analysis-scores {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            margin: 15px 0;
        }}
        
        .score {{
            background: rgba(15, 23, 42, 0.7);
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            min-width: 80px;
        }}
        
        .back-link {{
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 12px;
            margin-bottom: 20px;
            font-weight: 600;
            display: inline-block;
        }}
        
        .team-credits {{
            margin-top: 50px;
            padding: 30px;
            background: rgba(15, 23, 42, 0.6);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
        }}
        
        .team-member {{
            display: inline-block;
            margin: 10px 20px;
            padding: 15px 20px;
            background: rgba(30, 41, 59, 0.7);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }}
        
        .team-member:hover {{
            transform: translateY(-2px);
            border-color: rgba(167, 139, 250, 0.3);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        }}
        
        .member-name {{
            color: #ffffff;
            font-weight: 700;
            font-size: 1.1rem;
            margin-bottom: 5px;
        }}
        
        .member-role {{
            color: #a78bfa;
            font-size: 0.9rem;
            font-weight: 500;
        }}
        
        .project-info {{
            margin-top: 20px;
            color: #94a3b8;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <a href="/test" class="back-link">← Back to Test Page</a>
    
    <div class="header">
        <h1>📊 Customer Feedback Dashboard</h1>
        <p>AI-powered feedback prioritization and analysis</p>
    </div>
    
    <div class="stats">
        <div class="stat">
            <h3>Total Feedback</h3>
            <p>{len(feedback_list)}</p>
        </div>
        <div class="stat">
            <h3>Critical Issues</h3>
            <p style="color: #ef4444;">{len([f for f in feedback_list if f.get('analysis', {}).get('priority', 0) >= 8])}</p>
        </div>
        <div class="stat">
            <h3>High Priority</h3>
            <p style="color: #f59e0b;">{len([f for f in feedback_list if f.get('analysis', {}).get('priority', 0) >= 6])}</p>
        </div>
        <div class="stat">
            <h3>This Week</h3>
            <p>{len([f for f in feedback_list if f.get('timestamp', '').startswith(datetime.datetime.now().strftime('%Y-%m'))])}</p>
        </div>
    </div>
    """
    
    if not feedback_list:
        dashboard_html += '<div style="text-align: center; padding: 40px;">No feedback yet. <a href="/" style="color: #667eea;">Submit some feedback!</a></div>'
    else:
        for feedback in feedback_list:
            priority = feedback.get('analysis', {}).get('priority', 0)
            
            if priority >= 8:
                priority_class, priority_label = 'priority-critical', 'CRITICAL'
            elif priority >= 6:
                priority_class, priority_label = 'priority-high', 'HIGH'
            elif priority >= 4:
                priority_class, priority_label = 'priority-medium', 'MEDIUM'
            else:
                priority_class, priority_label = 'priority-low', 'LOW'
            
            analysis = feedback.get('analysis', {})
            
            dashboard_html += f"""
            <div class="feedback-item {priority_class}">
                <div style="display: flex; justify-content: between; align-items: center;">
                    <h3>{feedback['name']} ({feedback['email']})</h3>
                    <span style="background: {'#ef4444' if priority >= 8 else '#f59e0b' if priority >= 6 else '#eab308' if priority >= 4 else '#22c55e'}; 
                                color: white; padding: 5px 10px; border-radius: 15px; font-size: 12px;">
                        {priority_label} PRIORITY
                    </span>
                </div>
                <p><strong>Category:</strong> {feedback['category'].title()}</p>
                <p><strong>Submitted:</strong> {feedback['timestamp']}</p>
                <p><strong>Feedback:</strong> "{feedback['feedback']}"</p>
                
                <div class="analysis">
                    <strong>🤖 AI Analysis:</strong>
                    <div class="analysis-scores">
                        <div class="score">
                            <div style="color: #ef4444; font-weight: bold;">{analysis.get('urgency', 'N/A')}</div>
                            <small>Urgency</small>
                        </div>
                        <div class="score">
                            <div style="color: #f59e0b; font-weight: bold;">{analysis.get('impact', 'N/A')}</div>
                            <small>Impact</small>
                        </div>
                        <div class="score">
                            <div style="color: #a855f7; font-weight: bold;">{analysis.get('priority', 'N/A')}</div>
                            <small>Priority</small>
                        </div>
                        <div class="score">
                            <div style="color: #22c55e; font-weight: bold;">{analysis.get('confidence', 'N/A')}%</div>
                            <small>Confidence</small>
                        </div>
                    </div>
                    <p style="margin-top: 10px;">
                        <strong>Theme:</strong> {analysis.get('theme', 'N/A')} | 
                        <strong>Assigned Team:</strong> {analysis.get('assigned_team', 'N/A')}
                    </p>
                </div>
            </div>
            """
    
    dashboard_html += '''
    <div class="team-credits">
        <h3>👥 Created by</h3>
        <div class="team-member">
            <div class="member-name">Tejash Raju K V</div>
            <div class="member-role">Full-Stack Developer & AI Engineer</div>
        </div>
        <div class="team-member">
            <div class="member-name">Amrutha V</div>
            <div class="member-role">UI/UX Designer & Frontend Developer</div>
        </div>
        <div class="project-info">
            Built with ❤️ for Product Space Hackathon • AI-Powered Customer Feedback Prioritizer
        </div>
    </div>
    </body></html>'''
    return render_template_string(dashboard_html)

@app.route('/test')
def test_page():
    """Test page"""
    return render_template_string("""
<!DOCTYPE html>
<html>
<head><title>🧪 Server Test</title></head>
<body style="font-family: Arial; padding: 40px; text-align: center; background: #f0f0f0;">
    <h1>🧪 Customer Feedback Server</h1>
    <p style="color: green; font-size: 18px;">✅ Server is running successfully!</p>
    <div style="margin: 30px 0;">
        <a href="/" style="background: #667eea; color: white; padding: 15px 30px; text-decoration: none; border-radius: 8px; margin: 10px;">
            🎯 Customer Form
        </a>
        <a href="/internal/dashboard" style="background: #764ba2; color: white; padding: 15px 30px; text-decoration: none; border-radius: 8px; margin: 10px;">
            📊 Internal Dashboard
        </a>
    </div>
</body>
</html>
    """)

if __name__ == '__main__':
    print("\n🚀 Customer Feedback Prioritizer - Starting...")
    print(f"📍 Server: http://localhost:5001")
    print(f"🎯 Customer Form: http://localhost:5001/")
    print(f"📊 Dashboard: http://localhost:5001/internal/dashboard")
    print("=" * 50 + "\n")
    
    try:
        app.run(debug=True, host='127.0.0.1', port=5001, threaded=True)
    except Exception as e:
        print(f"❌ Server failed: {e}")