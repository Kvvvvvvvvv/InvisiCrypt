# InvisiCrypt - Advanced Steganography Platform

![InvisiCrypt Logo](static/logo.webp)

## 🔒 About InvisiCrypt

InvisiCrypt is an advanced steganography platform that allows you to hide secret messages within images using sophisticated LSB (Least Significant Bit) techniques. This project was developed by **Keerthivasan E** from VIT Chennai as part of the Open Source Programming Club (OSPC) initiative.

## 🚀 Quick Start

### Run the Application
```bash
python app.py
```
Then open your browser and go to `http://localhost:5000`

### Core Files
- **`app.py`** - Main Flask application with steganography logic
- **`templates/index.html`** - Beautiful cyberpunk-themed web interface
- **`static/style.css`** - Modern responsive styling
- **`requirements.txt`** - Python dependencies

## 🌟 Features

- **🔐 Advanced LSB Steganography**: Hide messages in image pixels imperceptibly
- **🛡️ Password Protection**: Secure your hidden messages with password encryption
- **📊 Database Tracking**: SQLite database to track encrypted images
- **🎨 Modern UI/UX**: Cyberpunk-themed responsive web interface
- **📱 Multi-format Support**: Works with various image formats
- **🗑️ File Management**: Easy deletion of encrypted image records

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
