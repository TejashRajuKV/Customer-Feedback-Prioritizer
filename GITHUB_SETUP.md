# 🚀 GitHub Setup Instructions

## Step 1: Create Repository on GitHub

1. **Go to GitHub**: Visit [github.com](https://github.com) and sign in
2. **Create New Repository**:
   - Click the "+" icon → "New repository"
   - Repository name: `customer-feedback-prioritizer` (or your preferred name)
   - Description: `🎯 AI-powered customer feedback prioritization for product teams`
   - Make it **Public** (required for GitHub Pages)
   - **DON'T** initialize with README (we already have files)
   - Click "Create repository"

## Step 2: Connect and Push

After creating the repository, GitHub will show you commands. Use these in your terminal:

```powershell
# Add the GitHub repository as remote origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Rename main branch (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values!**

## Step 3: Enable GitHub Pages

1. **Go to Repository Settings**:
   - Click on your repository
   - Click "Settings" tab
   - Scroll down to "Pages" in the left sidebar

2. **Configure GitHub Pages**:
   - Source: "Deploy from a branch"
   - Branch: `main` (or `master`)
   - Folder: `/ (root)`
   - Click "Save"

3. **Wait for Deployment**:
   - GitHub will build your site (takes a few minutes)
   - Your site will be available at: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`

## Step 4: Update README Links

After deployment, update the links in `README_GITHUB.md`:
- Replace `your-username` with your actual GitHub username
- Replace `your-repo-name` with your actual repository name

## 🎯 Quick Commands Summary

```powershell
# Connect to GitHub (replace with your details)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## 🌐 Your Live URLs

After setup, your project will be live at:
- **Main Page**: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`
- **Report Page**: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/view_report.html`

## 📋 Files Ready for GitHub Pages

✅ `index.html` - Main feedback form (static version)
✅ `view_report.html` - Priority analytics dashboard  
✅ `app.py` - Flask backend (for local development)
✅ `README_GITHUB.md` - GitHub Pages documentation
✅ Navigation between pages
✅ Team credits included
✅ Mobile responsive design
✅ Modern dark theme UI

## 🎨 What Visitors Will See

1. **Professional landing page** with your feedback form
2. **Real-time AI analysis demo** as they type
3. **Beautiful priority report** with sample data
4. **Team credits** showing both creators
5. **Responsive design** that works on all devices

## 🔄 Future Updates

To update your site:
```powershell
# Make changes to your files
git add .
git commit -m "Update: description of changes"
git push
```

GitHub Pages will automatically rebuild and deploy your changes!

---

**🚀 Ready to showcase your hackathon project to the world!**