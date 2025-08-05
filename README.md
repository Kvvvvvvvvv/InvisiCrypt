# 🔐 InvisiCrypt - Advanced Steganography Platform

> **🚀 Live Flask Web Application** | **🐍 Run with:** `python app.py`

![InvisiCrypt Logo](static/logo.webp)

## ⚡ Quick Demo

```bash
# 1. Clone and setup
git clone https://github.com/Kvvvvvvvvv/InvisiCrypt.git
cd InvisiCrypt
pip install -r requirements.txt

# 2. Run the web application
python app.py

# 3. Open browser: http://localhost:5000
```

## 🎯 **Main Application: `app.py`**

**Flask-based steganography web server** with cyberpunk UI for hiding secret messages in images.

### 🔥 Core Features in `app.py`:
- **LSB Steganography Algorithm** - Hides messages in image pixels
- **Password Protection** - Secure encryption/decryption
- **SQLite Database** - Tracks encrypted images
- **Web Interface** - Beautiful cyberpunk-themed UI
- **File Management** - Upload, encrypt, download functionality

## 🚀 Technology Stack

- **Backend**: Python Flask
- **Image Processing**: OpenCV
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Security**: Cryptographic hashing
- **Design**: Responsive cyberpunk theme

## 📋 Requirements

```
Flask
opencv-python
numpy
```

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kvvvvvvvvv/InvisiCrypt.git
   cd InvisiCrypt
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to `http://localhost:5000`

## 📁 Project Structure

```
InvisiCrypt/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface
├── static/
│   ├── style.css         # Cyberpunk styling
│   └── logo.webp         # Application logo
├── uploads/              # Encrypted images storage
├── requirements.txt      # Python dependencies
├── stego.py             # Standalone steganography script
├── Enc.py               # Encryption utility
├── Decry.py             # Decryption utility
└── README.md            # This file
```

## 💻 Core Application Code

The main steganography logic is implemented in `app.py`:

### Key Functions:
- `embed_message()` - Embeds secret messages using LSB technique
- `extract_message()` - Extracts hidden messages from images
- `hash_password()` - Secure password hashing
- Flask routes for encryption/decryption web interface

## 🎯 How It Works

### Encryption Process
1. Upload an image file
2. Enter your secret message
3. Set a strong password
4. Click "Encrypt & Download"
5. Download the steganographically modified image

### Decryption Process
1. Upload the encrypted image
2. Enter the correct password
3. Click "Decrypt Message"
4. View your hidden message

## 🔬 Technical Details

InvisiCrypt uses LSB (Least Significant Bit) steganography to embed messages:
- Modifies the least significant bits of RGB color channels
- Stores up to 3 bits of data per pixel
- Maintains excellent image quality while hiding data
- Uses password verification for secure extraction

## 🌟 Future Enhancements

- 🎵 Audio Steganography
- 📹 Video Steganography  
- 🔐 Blockchain Integration
- 🤖 AI-Powered Detection
- 📱 Mobile Application
- ☁️ Cloud Integration

## 👨‍💻 Developer

**Keerthivasan E**  
Computer Science Student, VIT Chennai  
Email: keerthivasaneofficial@gmail.com

## 🏛️ Organization

**Open Source Programming Club (OSPC) - VIT Chennai**  
- Website: [ospcvitc.club](https://ospcvitc.club/)
- Email: opensourceprogrammingclub.vitc@gmail.com
- Instagram: [@ospc_vitc](https://www.instagram.com/ospc_vitc/)

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📞 Support

For technical support or questions:
- Create an issue on GitHub
- Email: opensourceprogrammingclub.vitc@gmail.com
- Visit our website: [ospcvitc.club](https://ospcvitc.club/)

---

**InvisiCrypt v2.0** - Advanced Steganography Platform  
Published by OSPC Club | Developed by Keerthivasan E
