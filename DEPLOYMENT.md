# 🚀 Streamlit Cloud Deployment Guide

## Your App Repository
🔗 https://github.com/jashshah-dev/Document-uploader-family.git

---

## Step-by-Step Deployment Instructions

### ✅ Step 1: Push to GitHub (Commands below)

Run these commands in your terminal:

```bash
cd "/Users/jashshah/Mobotory Code Git/mb_predictor/document_uploader"
git init
git add .
git commit -m "Initial commit - Document uploader app"
git branch -M main
git remote add origin https://github.com/jashshah-dev/Document-uploader-family.git
git push -u origin main
```

### ✅ Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Click "Sign in" (use your GitHub account)

2. **Create New App**
   - Click "New app" button
   - Select repository: `jashshah-dev/Document-uploader-family`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL (optional): Choose your custom subdomain

3. **Click "Deploy"**
   - Streamlit will automatically:
     - Install dependencies from `requirements.txt`
     - Start your app
     - Give you a public URL

4. **Your App URL**
   - Will be something like: `https://document-uploader-family.streamlit.app`
   - Or your custom URL: `https://YOUR-CUSTOM-NAME.streamlit.app`

### ✅ Step 3: Share the URL

Once deployed:
- **Public Upload Page**: Share the main URL with everyone
- **Admin Dashboard**: Only you access it with the password
- Files are stored in Streamlit's cloud storage (still free!)

---

## Important Notes

### 🔒 Security Settings

**IMPORTANT**: Before deploying, update the admin password in `app.py` (line 119):

```python
ADMIN_PASSWORD = "your_secure_password_here"  # Change this!
```

### 💾 Storage on Streamlit Cloud

When deployed on Streamlit Cloud:
- Files are stored in the app's file system
- **Note**: Files may be cleared on app restarts
- For permanent storage, consider adding Google Drive/Dropbox integration (optional)

### 🔄 Updating Your App

After deployment, any changes you push to GitHub will automatically redeploy:

```bash
git add .
git commit -m "Updated app"
git push
```

Streamlit Cloud will auto-detect changes and redeploy!

---

## Troubleshooting

### Issue: Git push fails
**Solution**: Make sure you have access to the repository
```bash
# If you need to authenticate
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"
```

### Issue: Streamlit deployment fails
**Solution**: Check the deployment logs in Streamlit Cloud dashboard

### Issue: Files not persisting
**Solution**: Streamlit Cloud has ephemeral storage. For production, add cloud storage:
- Google Drive API
- Dropbox API
- AWS S3
- Or download files regularly from admin dashboard

---

## Next Steps (Optional Enhancements)

### Add Email Notifications
- Get notified when someone uploads a file
- Use Streamlit's secrets management + SMTP

### Add Cloud Storage
- Integrate Google Drive or Dropbox
- Files persist permanently
- More reliable for production

### Custom Domain
- Use your own domain name
- Configure in Streamlit Cloud settings
- Requires domain ownership

---

## Support

- **Streamlit Docs**: https://docs.streamlit.io
- **Streamlit Forum**: https://discuss.streamlit.io
- **GitHub Issues**: https://github.com/jashshah-dev/Document-uploader-family/issues

Happy deploying! 🎉

