# Document Upload Center 📁

A simple Streamlit web application that allows anyone to upload documents with their name. All uploads are stored centrally with an admin dashboard to view and manage them.

## Features

✅ **Public Upload Page**
- Anyone can upload documents
- Supports all file types
- Requires uploader's name
- Optional notes field
- Automatic timestamping

✅ **Admin Dashboard**
- Password protected
- View all uploads with metadata
- Search and filter uploads
- Download metadata as CSV
- Direct file downloads
- Upload statistics

✅ **100% Free**
- Local file storage (no cloud costs)
- Open-source Streamlit framework
- No external dependencies

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### 3. Share with Others

#### Option A: Local Network (Free)
Share your local network URL with people on the same WiFi:
```bash
streamlit run app.py --server.address 0.0.0.0
```
Then share the URL shown (e.g., `http://192.168.1.x:8501`)

#### Option B: Deploy Online (Free Options)

**Streamlit Community Cloud** (Recommended - 100% Free):
1. Push this code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Deploy (completely free!)

**Other Free Options:**
- Railway.app (500 hrs/month free)
- Render.com (750 hrs/month free)
- Hugging Face Spaces (free)

## Usage

### For Uploaders (Public)
1. Open the app
2. Select "📤 Upload Document" from sidebar
3. Enter your name
4. Upload your file
5. Add notes (optional)
6. Click "Upload Document"

### For Admin (You)
1. Select "🔐 Admin Dashboard" from sidebar
2. Enter password (default: `admin123`)
3. View all uploads, statistics, and download files

## Configuration

### Change Admin Password
Edit line 119 in `app.py`:
```python
ADMIN_PASSWORD = "your_secure_password_here"
```

### Storage Location
Files are stored in the `uploaded_documents/` folder
Metadata is stored in `upload_metadata.json`

## File Structure

```
document_uploader/
├── app.py                    # Main application
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── uploaded_documents/      # Storage folder (auto-created)
│   ├── 20241016_143022_document.pdf
│   ├── 20241016_143022_notes.txt
│   └── ...
└── upload_metadata.json     # Upload tracking (auto-created)
```

## Security Notes

⚠️ **Important for Production:**
1. **Change the default admin password** in `app.py`
2. For better security, consider:
   - Using environment variables for passwords
   - Adding user authentication
   - Implementing rate limiting
   - Adding file size limits
   - Scanning uploaded files

## Deployment Guide

### Deploy to Streamlit Community Cloud (100% Free Forever)

1. **Create GitHub Repository**
   ```bash
   cd document_uploader
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

2. **Deploy to Streamlit**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Share Your URL**
   - You'll get a URL like: `https://your-app.streamlit.app`
   - Share this with anyone who needs to upload documents
   - You can view all uploads from the admin dashboard

## Troubleshooting

**Port already in use:**
```bash
streamlit run app.py --server.port 8502
```

**Can't access from other devices:**
- Make sure firewall allows incoming connections
- Use `--server.address 0.0.0.0`

**Files not showing up:**
- Check the `uploaded_documents/` folder exists
- Verify write permissions

## Support

For issues or questions:
1. Check the Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
2. Review uploaded files in the `uploaded_documents/` folder
3. Check `upload_metadata.json` for upload records

## License

Free to use and modify as needed.

