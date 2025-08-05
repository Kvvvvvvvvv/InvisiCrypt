import cv2
import numpy as np
from flask import Flask, request, render_template, send_file, flash, redirect, url_for, session
import os
import sqlite3
import hashlib
import secrets
from datetime import datetime

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def init_db():
    conn = sqlite3.connect('stego.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS encrypted_images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_filename TEXT NOT NULL,
            encrypted_filename TEXT NOT NULL,
            message_preview TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, password_hash):
    return hash_password(password) == password_hash

def embed_message(img, msg, password):
    # Add password as prefix to message for verification
    full_message = f"PASSWORD:{password}:MESSAGE:{msg}"
    n, m, z = 0, 0, 0
    for char in full_message:
        img[n, m, z] = ord(char)
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1
    # Add a null terminator
    img[n, m, z] = 0
    return img

def extract_message(img):
    message = ""
    n, m, z = 0, 0, 0
    while True:
        pixel_value = img[n, m, z]
        if pixel_value == 0:
            break
        message += chr(pixel_value)
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1
    return message

def parse_extracted_message(extracted_text):
    try:
        if extracted_text.startswith("PASSWORD:"):
            parts = extracted_text.split(":MESSAGE:")
            if len(parts) == 2:
                password_part = parts[0].replace("PASSWORD:", "")
                message_part = parts[1]
                return password_part, message_part
    except:
        pass
    return None, None

@app.route('/')
def index():
    # Get list of encrypted images from database
    conn = sqlite3.connect('stego.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, original_filename, message_preview, created_at FROM encrypted_images ORDER BY created_at DESC')
    encrypted_images = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', encrypted_images=encrypted_images)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    if 'image' not in request.files or 'message' not in request.form or 'password' not in request.form:
        flash('Missing image, message, or password', 'error')
        return redirect(url_for('index'))

    image_file = request.files['image']
    message = request.form['message']
    password = request.form['password']
    
    if not message.strip() or not password.strip():
        flash('Message and password cannot be empty', 'error')
        return redirect(url_for('index'))
    
    # Read the image
    npimg = np.fromfile(image_file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        flash('Error: Could not decode image', 'error')
        return redirect(url_for('index'))

    # Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    original_filename = image_file.filename
    encrypted_filename = f"encrypted_{timestamp}.png"
    
    encrypted_img = embed_message(img.copy(), message, password)
    
    encrypted_image_path = os.path.join(app.config['UPLOAD_FOLDER'], encrypted_filename)
    cv2.imwrite(encrypted_image_path, encrypted_img)
    
    # Store in database
    conn = sqlite3.connect('stego.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO encrypted_images (original_filename, encrypted_filename, message_preview, password_hash)
        VALUES (?, ?, ?, ?)
    ''', (original_filename, encrypted_filename, message[:50] + "..." if len(message) > 50 else message, hash_password(password)))
    conn.commit()
    conn.close()
    
    flash('Message encrypted successfully!', 'success')
    return send_file(encrypted_image_path, as_attachment=True, download_name=encrypted_filename)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    if 'image' not in request.files or 'password' not in request.form:
        flash('Missing image or password', 'error')
        return redirect(url_for('index'))

    image_file = request.files['image']
    password = request.form['password']
    
    if not password.strip():
        flash('Password cannot be empty', 'error')
        return redirect(url_for('index'))
    
    # Read the image
    npimg = np.fromfile(image_file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        flash('Error: Could not decode image', 'error')
        return redirect(url_for('index'))
    
    extracted_text = extract_message(img)
    stored_password, message = parse_extracted_message(extracted_text)
    
    if stored_password and stored_password == password:
        flash('Message decrypted successfully!', 'success')
        return render_template('index.html', decrypted_message=message, encrypted_images=get_encrypted_images())
    else:
        flash('Incorrect password or no message found', 'error')
        return redirect(url_for('index'))

def get_encrypted_images():
    conn = sqlite3.connect('stego.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, original_filename, message_preview, created_at FROM encrypted_images ORDER BY created_at DESC')
    encrypted_images = cursor.fetchall()
    conn.close()
    return encrypted_images

@app.route('/delete/<int:image_id>', methods=['POST'])
def delete_image(image_id):
    conn = sqlite3.connect('stego.db')
    cursor = conn.cursor()
    cursor.execute('SELECT encrypted_filename FROM encrypted_images WHERE id = ?', (image_id,))
    result = cursor.fetchone()
    
    if result:
        filename = result[0]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        
        cursor.execute('DELETE FROM encrypted_images WHERE id = ?', (image_id,))
        conn.commit()
        flash('Image deleted successfully!', 'success')
    else:
        flash('Image not found!', 'error')
    
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True) 