# 🚀 Quick Start Guide

## Get Started in 3 Steps

### Step 1: Install Streamlit
```bash
cd "/Users/jashshah/Mobotory Code Git/mb_predictor/document_uploader"
pip install streamlit pandas
```

### Step 2: Run the App
```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

### Step 3: Share with Others

**For people in your office/home (same WiFi):**
```bash
streamlit run app.py --server.address 0.0.0.0
```
Then share the network URL shown (looks like `http://192.168.x.x:8501`)

**For people anywhere in the world (FREE):**
1. Create a GitHub account (free)
2. Upload this folder to GitHub
3. Go to https://share.streamlit.io
4. Connect your GitHub and deploy (takes 2 minutes)
5. Get a permanent URL like `https://your-app.streamlit.app`

---

## How It Works

### 📤 Upload Page (For Everyone)
- Anyone opens your app URL
- They enter their name
- Upload their document
- Done! You get it automatically

### 🔐 Admin Page (For You Only)
- Click "Admin Dashboard" in sidebar
- Enter password: `admin123` (change this in app.py!)
- See all uploads with names, dates, file sizes
- Download any file
- Export data to CSV

---

## Where Are Files Stored?

All uploaded files are saved in:
```
document_uploader/uploaded_documents/
```

You can browse this folder anytime to see all files!

---

## Change Admin Password

Edit line 119 in `app.py`:
```python
ADMIN_PASSWORD = "your_new_password"
```

---

## Deploy for Free Online

**Streamlit Community Cloud (Easiest & Free Forever):**

1. Install git if you don't have it
2. Run these commands:
   ```bash
   cd "/Users/jashshah/Mobotory Code Git/mb_predictor/document_uploader"
   git init
   git add .
   git commit -m "Document uploader"
   ```
3. Create GitHub repo at https://github.com/new
4. Follow GitHub's instructions to push
5. Go to https://share.streamlit.io
6. Click "New app" → Select your repo → Deploy
7. Done! Share your URL with everyone

**Alternative Free Options:**
- **Hugging Face Spaces**: https://huggingface.co/spaces
- **Railway**: https://railway.app (500 hrs/month free)
- **Render**: https://render.com (750 hrs/month free)

---

## Need Help?

1. **App won't start**: Make sure you installed streamlit: `pip install streamlit pandas`
2. **Can't access from phone**: Use `--server.address 0.0.0.0` and share the network URL
3. **Want to customize**: Edit `app.py` - it's well commented!

Enjoy! 🎉

