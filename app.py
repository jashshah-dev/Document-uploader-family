import streamlit as st
import os
from datetime import datetime
import pandas as pd
from pathlib import Path
import json

# Configuration
UPLOAD_FOLDER = "uploaded_documents"
METADATA_FILE = "upload_metadata.json"

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize metadata file if it doesn't exist
if not os.path.exists(METADATA_FILE):
    with open(METADATA_FILE, 'w') as f:
        json.dump([], f)

def save_metadata(name, filename, file_size, timestamp):
    """Save upload metadata to JSON file"""
    try:
        with open(METADATA_FILE, 'r') as f:
            metadata = json.load(f)
    except:
        metadata = []
    
    metadata.append({
        'name': name,
        'filename': filename,
        'file_size': file_size,
        'timestamp': timestamp
    })
    
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=2)

def load_metadata():
    """Load all upload metadata"""
    try:
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def format_file_size(size_bytes):
    """Format file size in human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def main():
    st.set_page_config(
        page_title="Document Upload Center",
        page_icon="📁",
        layout="wide"
    )
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select Page", ["📤 Upload Document", "🔐 Admin Dashboard"])
    
    if page == "📤 Upload Document":
        upload_page()
    else:
        admin_page()

def upload_page():
    """Public upload page"""
    st.title("📤 Document Upload Center")
    st.markdown("---")
    
    st.write("Welcome! Please upload your document below.")
    
    # Input for name
    uploader_name = st.text_input("Your Name *", placeholder="Enter your name")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a file to upload",
        type=None,  # Accept all file types
        help="Upload any type of document"
    )
    
    # Additional notes (optional)
    notes = st.text_area("Notes (optional)", placeholder="Add any notes about this document")
    
    # Upload button
    if st.button("Upload Document", type="primary"):
        if not uploader_name:
            st.error("⚠️ Please enter your name")
        elif not uploaded_file:
            st.error("⚠️ Please select a file to upload")
        else:
            try:
                # Create timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                
                # Create filename with timestamp
                original_filename = uploaded_file.name
                safe_filename = f"{timestamp}_{original_filename}"
                file_path = os.path.join(UPLOAD_FOLDER, safe_filename)
                
                # Save file
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Save metadata
                save_metadata(
                    name=uploader_name,
                    filename=original_filename,
                    file_size=uploaded_file.size,
                    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                
                # Save notes if provided
                if notes:
                    notes_file = os.path.join(UPLOAD_FOLDER, f"{timestamp}_notes.txt")
                    with open(notes_file, 'w') as f:
                        f.write(f"Uploader: {uploader_name}\n")
                        f.write(f"File: {original_filename}\n")
                        f.write(f"Timestamp: {timestamp}\n\n")
                        f.write(f"Notes:\n{notes}")
                
                st.success(f"✅ Document uploaded successfully!")
                st.balloons()
                
                st.info(f"""
                **Upload Details:**
                - Name: {uploader_name}
                - File: {original_filename}
                - Size: {format_file_size(uploaded_file.size)}
                - Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                """)
                
            except Exception as e:
                st.error(f"❌ Error uploading file: {str(e)}")
    
    # Information section
    st.markdown("---")
    st.markdown("""
    ### ℹ️ Information
    - All file types are accepted
    - Files are stored securely
    - Your upload will be reviewed by the administrator
    """)

def admin_page():
    """Admin dashboard to view all uploads"""
    st.title("🔐 Admin Dashboard")
    st.markdown("---")
    
    # Password protection (basic)
    password = st.text_input("Enter Admin Password", type="password")
    
    # Simple password check (you can change this)
    ADMIN_PASSWORD = "admin123"  # Change this to your preferred password
    
    if password == ADMIN_PASSWORD:
        st.success("✅ Access Granted")
        
        # Load metadata
        metadata = load_metadata()
        
        if metadata:
            st.subheader(f"📊 Total Uploads: {len(metadata)}")
            
            # Convert to DataFrame for better display
            df = pd.DataFrame(metadata)
            df['file_size'] = df['file_size'].apply(format_file_size)
            
            # Display statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Documents", len(metadata))
            with col2:
                unique_uploaders = len(set([m['name'] for m in metadata]))
                st.metric("Unique Uploaders", unique_uploaders)
            with col3:
                total_size = sum([m['file_size'] for m in load_metadata()])
                st.metric("Total Size", format_file_size(total_size))
            
            st.markdown("---")
            
            # Filter options
            st.subheader("🔍 Filter & Search")
            search_name = st.text_input("Search by name", "")
            
            if search_name:
                df = df[df['name'].str.contains(search_name, case=False, na=False)]
            
            # Display table
            st.subheader("📋 All Uploads")
            st.dataframe(
                df,
                use_container_width=True,
                column_config={
                    'name': 'Uploader Name',
                    'filename': 'File Name',
                    'file_size': 'File Size',
                    'timestamp': 'Upload Time'
                }
            )
            
            # Download options
            st.markdown("---")
            st.subheader("📥 Download Options")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Export metadata as CSV
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📄 Download Metadata (CSV)",
                    data=csv,
                    file_name=f"upload_metadata_{datetime.now().strftime('%Y%m%d')}.csv",
                    mime="text/csv"
                )
            
            with col2:
                # Show upload folder location
                abs_path = os.path.abspath(UPLOAD_FOLDER)
                st.info(f"📁 Files Location: `{abs_path}`")
            
            # Individual file download
            st.markdown("---")
            st.subheader("📂 Browse Files")
            
            files = sorted([f for f in os.listdir(UPLOAD_FOLDER) if not f.endswith('_notes.txt')], reverse=True)
            
            if files:
                for file in files[:20]:  # Show latest 20 files
                    file_path = os.path.join(UPLOAD_FOLDER, file)
                    file_size = os.path.getsize(file_path)
                    
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.text(file)
                    with col2:
                        st.text(format_file_size(file_size))
                    with col3:
                        with open(file_path, 'rb') as f:
                            st.download_button(
                                label="⬇️",
                                data=f,
                                file_name=file,
                                key=file
                            )
                
                if len(files) > 20:
                    st.info(f"Showing latest 20 files. Total files: {len(files)}")
        else:
            st.info("📭 No uploads yet")
            
    elif password:
        st.error("❌ Invalid password")
    else:
        st.warning("🔒 Please enter the admin password to view uploads")

if __name__ == "__main__":
    main()

