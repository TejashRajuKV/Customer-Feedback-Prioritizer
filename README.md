# 🎯 Customer Feedback Prioritizer

**A modern web application with AI-powered feedback analysis that categorizes customer feedback by urgency and impact, with real-time analysis and beautiful dark UI.**

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install flask flask-cors
```

### 2. Run the Web Application
```bash
python app.py
```

### 3. Access the Application
- **Customer Form**: http://localhost:5001/ (for customers to submit feedback)
- **Internal Dashboard**: http://localhost:5001/internal/dashboard (for product teams)
- **Test Page**: http://localhost:5001/test (to verify server status)

## ✨ Features

### **🌐 Modern Web Interface**
- **Customer Feedback Form**: Beautiful dark-themed form with real-time AI analysis
- **Internal Dashboard**: Prioritized feedback overview for product teams
- **Responsive Design**: Glass morphism effects with smooth animations
- **Real-time Analysis**: See AI insights as customers type their feedback

### **🤖 Advanced AI Processing**
- **🎯 Urgency Scoring (0-10)** - Security issues, system failures, time-sensitive problems
- **📊 Impact Scoring (0-10)** - User reach, revenue impact, business criticality
- **🏷️ Smart Theme Detection** - Authentication, Payment, Performance, UI/UX, etc.
- **⚡ Intelligent Priority Calculation** - Combined urgency + impact with contextual analysis
- **💼 Team Assignment** - Automatic assignment to Engineering, Product, Design, or Security teams

### **📈 Actionable Insights**
- **🚨 Priority Dashboard** - Visual priority levels (Critical, High, Medium, Low)
- **📉 Confidence Scoring** - AI confidence levels for analysis reliability
- **🗺️ Theme Breakdown** - Grouped feedback by problem areas
- **⏱️ Team Routing** - Automatic assignment based on issue type and priority

## 🖼️ Screenshots & Demo

### Customer Feedback Form
- Modern dark theme with gradient backgrounds
- Real-time AI analysis as you type
- Glass morphism design with smooth animations
- Interactive form fields with focus effects

### Internal Dashboard
- Priority-sorted feedback with color coding
- Stats cards showing total feedback, critical issues
- AI analysis breakdown with confidence scores
- Team assignments for each feedback item

## 🎯 Example Analysis

**Input**: "Login keeps failing with 2FA on mobile; happens now and blocking our team"

**AI Analysis**:
- **Urgency**: 8/10 (blocking, immediate impact)
- **Impact**: 7/10 (affects team productivity) 
- **Priority**: 8/10 (high priority)
- **Theme**: Authentication
- **Assigned Team**: 🔧 Engineering Team (URGENT)
- **Confidence**: 89%

## 📁 Project Structure

```
├── app.py                          # Main Flask web application (clean & optimized)
├── customer_feedback.json          # Feedback data storage (JSON)
├── view_report.html                # Static priority report dashboard
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
└── HACKATHON_CHECKLIST.md         # Demo readiness checklist
```

## 🔧 Configuration

### Environment Variables (Optional)
Create a `.env` file for enhanced AI analysis:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
*Note: The system works perfectly with the built-in AI analysis even without OpenAI*

### Feedback Form Categories
Customers can choose from:
- 🐛 **Bug Report**
- ✨ **Feature Request** 
- ⚡ **Performance Issue**
- 🎨 **UI/UX Feedback**
- 💬 **General Feedback**
- 😤 **Complaint**

### Data Storage
- **Format**: JSON file (`customer_feedback.json`)
- **Structure**: Includes user info, feedback text, AI analysis, timestamps
- **Persistence**: All feedback automatically saved with analysis results

## 🎯 AI Priority Scoring

### **Urgency Score (0-10)**
- **10**: Security breaches, critical system failures
- **8-9**: System down, revenue blocking, urgent issues
- **6-7**: Important problems, user blocking issues
- **4-5**: Standard bugs, performance issues
- **2-3**: Feature requests, suggestions

### **Impact Score (0-10)** 
- **10**: All users affected, major revenue impact
- **8-9**: Many users, significant business impact
- **6-7**: Multiple users, moderate impact
- **4-5**: Some users affected
- **2-3**: Individual users, cosmetic issues

### **Priority Calculation**
`Priority = max(Urgency, Impact, (Urgency + Impact) / 2)`

## 🏷️ Smart Theme Detection

- **Security Critical** - hacks, breaches, vulnerabilities
- **System Failure** - crashes, down, not working, broken
- **Authentication** - login, password, 2FA, SSO
- **Payment** - checkout, billing, transactions
- **Performance** - slow, timeout, loading, lag
- **UI/UX** - design, interface, usability
- **Bug** - errors, problems, issues
- **Feature** - requests, additions, improvements
- **General** - other feedback types

## 🔎 Team Assignment Logic

- **🚨 Security Critical**: Security + Engineering + Product
- **🔧 System Failure**: Engineering Team (URGENT)
- **High Priority (8-10)**: Engineering + Product teams
- **Medium Priority (6-7)**: Specialized by theme
- **Low Priority (<6)**: Product Team

## 🎉 Key Benefits

✅ **Modern Web Interface** - Beautiful, responsive design with dark theme  
✅ **Real-time AI Analysis** - Instant feedback analysis as users type  
✅ **Smart Prioritization** - Advanced urgency & impact scoring  
✅ **Team Auto-Assignment** - Routes feedback to correct teams automatically  
✅ **Zero Setup Complexity** - Just install Flask and run  
✅ **Professional UI/UX** - Glass morphism with smooth animations  
✅ **Hackathon Ready** - Perfect demo-ready application  

## 🚀 Usage

### For Customers:
1. Open http://localhost:5001/
2. Fill out the feedback form
3. Watch real-time AI analysis as you type
4. Submit and get instant priority assessment

### For Product Teams:
1. Open http://localhost:5001/internal/dashboard
2. View all feedback prioritized by urgency
3. See AI analysis and team assignments
4. Take action on high-priority items first

## 🎯 Perfect For

- **Hackathon Demos** - Impressive UI with real AI functionality
- **Product Teams** - Prioritize customer feedback intelligently  
- **Startups** - Understand customer pain points quickly
- **Customer Success** - Route feedback to the right teams
- **Product Managers** - Data-driven prioritization decisions

## 🏆 Technical Highlights

- **Flask Web Framework** with modern routing
- **Advanced NLP Analysis** with contextual understanding
- **Beautiful CSS Animations** with glass morphism effects
- **Real-time JavaScript** for dynamic user experience
- **Responsive Design** that works on all devices
- **JSON Data Storage** with full feedback persistence

---

**Ready to revolutionize customer feedback management!** 🚀

*Built with ❤️ for hackathons and modern product teams*
