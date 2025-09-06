
from flask import Flask, request, render_template, redirect, url_for, jsonify
import requests
import time
import os
import json
import random
import threading
from datetime import datetime, timedelta

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

# Default comments for auto-commenting feature
default_comments = [
    "Osm 😘",
    "Gorgeous 😍🥰",
    "I love it 😍🥳",
    "Amazing 😍",
    "Beautiful 💖",
    "Wow 😱",
    "Stunning 🔥",
    "Perfect 👌",
    "Love this 💕",
    "Incredible 🤩"
]

def auto_post_scheduler():
    """Background task for auto posting"""
    while True:
        try:
            # Check for auto post files
            for folder in os.listdir('.'):
                if folder.startswith('AutoPost_'):
                    auto_post_path = os.path.join(folder, 'auto_post.json')
                    if os.path.exists(auto_post_path):
                        with open(auto_post_path, 'r') as f:
                            data = json.load(f)
                        
                        if data.get('active', False):
                            token = data.get('token', '')
                            messages = data.get('messages', [])
                            
                            if messages:
                                message = random.choice(messages)
                                post_url = 'https://graph.facebook.com/v15.0/me/feed'
                                params = {
                                    'access_token': token,
                                    'message': message
                                }
                                
                                response = requests.post(post_url, json=params, headers=headers)
                                print(f"Auto post: {'Success' if response.ok else 'Failed'}")
            
            time.sleep(3600)  # Wait 1 hour
        except Exception as e:
            print(f"Auto post error: {e}")
            time.sleep(3600)

# Start background scheduler
threading.Thread(target=auto_post_scheduler, daemon=True).start()

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PREMIUM FB AUTOMATION SUITE</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
            font-family: 'Orbitron', monospace;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }
        
        /* Falling Stars Animation */
        .stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }
        
        .star {
            position: absolute;
            width: 2px;
            height: 2px;
            background: #00ffff;
            border-radius: 50%;
            animation: fall linear infinite;
            box-shadow: 0 0 10px #00ffff;
        }
        
        @keyframes fall {
            0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; }
            100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
        }
        
        .container {
            max-width: 900px;
            margin: 50px auto;
            padding: 30px;
            background: rgba(0, 0, 0, 0.8);
            border-radius: 20px;
            border: 2px solid #00ffff;
            box-shadow: 0 0 50px rgba(0, 255, 255, 0.3);
            backdrop-filter: blur(10px);
            position: relative;
            z-index: 2;
        }
        
        h1 {
            text-align: center;
            color: #00ffff;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 0 0 20px #00ffff;
            font-weight: 900;
        }
        
        .owner {
            text-align: center;
            color: #ffffff;
            font-size: 1.2em;
            margin-bottom: 30px;
            text-shadow: 0 0 10px #ffffff;
        }
        
        .nav-tabs {
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 30px;
            border-bottom: 2px solid #00ffff;
            gap: 2px;
        }
        
        .nav-tab {
            flex: 1;
            min-width: 120px;
            padding: 12px 8px;
            background: rgba(0, 255, 255, 0.1);
            color: #00ffff;
            text-align: center;
            cursor: pointer;
            border: none;
            border-bottom: 3px solid transparent;
            transition: all 0.3s ease;
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            font-size: 0.9em;
        }
        
        @media (max-width: 768px) {
            .nav-tab {
                flex: 1 1 45%;
                font-size: 0.8em;
                padding: 10px 5px;
            }
        }
        
        @media (max-width: 480px) {
            .nav-tab {
                flex: 1 1 100%;
                margin-bottom: 2px;
            }
        }
        
        .nav-tab:hover, .nav-tab.active {
            background: rgba(0, 255, 255, 0.2);
            border-bottom-color: #00ffff;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            color: #00ffff;
            margin-bottom: 8px;
            font-weight: 700;
            text-shadow: 0 0 5px #00ffff;
        }
        
        .form-control {
            width: 100%;
            padding: 12px;
            background: rgba(0, 0, 0, 0.7);
            border: 2px solid #00ffff;
            border-radius: 10px;
            color: #ffffff;
            font-family: 'Orbitron', monospace;
            transition: all 0.3s ease;
        }
        
        .form-control:focus {
            outline: none;
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
            border-color: #ffffff;
        }
        
        .btn {
            padding: 15px 30px;
            background: linear-gradient(45deg, #00ffff, #0080ff);
            color: #000000;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            text-transform: uppercase;
            transition: all 0.3s ease;
            width: 100%;
            margin-top: 10px;
        }
        
        .btn:hover {
            background: linear-gradient(45deg, #0080ff, #00ffff);
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.7);
            transform: translateY(-2px);
        }
        
        textarea {
            min-height: 100px;
            resize: vertical;
        }
    </style>
</head>
<body>
    <div class="stars" id="stars"></div>
    
    <div class="container">
        <h1>🚀 FB AUTOMATION SUITE 🚀</h1>
        <div class="owner">OWNER: KASHIF RAZA</div>
        
        <div class="nav-tabs">
            <button class="nav-tab active" onclick="showTab('convo')">Multi Convo</button>
            <button class="nav-tab" onclick="showTab('comment')">Auto Comment</button>
            <button class="nav-tab" onclick="showTab('message')">Bulk Message</button>
            <button class="nav-tab" onclick="showTab('share')">Auto Share</button>
            <button class="nav-tab" onclick="showTab('autopost')">Auto Post</button>
        </div>
        
        <!-- Multi Convo Tab -->
        <div id="convo" class="tab-content active">
            <form action="/convo" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label>Convo ID:</label>
                    <input type="text" class="form-control" name="threadId" required>
                </div>
                <div class="form-group">
                    <label>Tokens File:</label>
                    <input type="file" class="form-control" name="txtFile" accept=".txt" required>
                </div>
                <div class="form-group">
                    <label>Messages File:</label>
                    <input type="file" class="form-control" name="messagesFile" accept=".txt" required>
                </div>
                <div class="form-group">
                    <label>Sender Name:</label>
                    <input type="text" class="form-control" name="kidx" required>
                </div>
                <div class="form-group">
                    <label>Speed (seconds):</label>
                    <input type="number" class="form-control" name="time" value="60" required>
                </div>
                <button type="submit" class="btn">🚀 START CONVO BLAST</button>
            </form>
        </div>
        
        <!-- Auto Comment Tab -->
        <div id="comment" class="tab-content">
            <form action="/comment" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label>Facebook Token:</label>
                    <input type="text" class="form-control" name="token" required>
                </div>
                <div class="form-group">
                    <label>Post ID:</label>
                    <input type="text" class="form-control" name="postId" required>
                </div>
                <div class="form-group">
                    <label>Custom Comments JSON File (Optional):</label>
                    <input type="file" class="form-control" name="customCommentsFile" accept=".json">
                    <small style="color: #00ffff; opacity: 0.8;">If not provided, default comments will be used</small>
                </div>
                <div class="form-group">
                    <label>Number of Comments:</label>
                    <input type="number" class="form-control" name="commentCount" value="100" required>
                </div>
                <div class="form-group">
                    <label>Speed (seconds):</label>
                    <input type="number" class="form-control" name="speed" value="30" required>
                </div>
                <button type="submit" class="btn">💬 START AUTO COMMENT</button>
            </form>
        </div>
        
        <!-- Bulk Message Tab -->
        <div id="message" class="tab-content">
            <form action="/message" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label>Facebook Token:</label>
                    <input type="text" class="form-control" name="token" required>
                </div>
                <div class="form-group">
                    <label>Target ID (Group/Inbox):</label>
                    <input type="text" class="form-control" name="targetId" required>
                </div>
                <div class="form-group">
                    <label>Messages JSON File:</label>
                    <input type="file" class="form-control" name="messageFile" accept=".json" required>
                </div>
                <div class="form-group">
                    <label>Speed (seconds):</label>
                    <input type="number" class="form-control" name="speed" value="60" required>
                </div>
                <button type="submit" class="btn">📨 START BULK MESSAGING</button>
            </form>
        </div>
        
        <!-- Auto Share Tab -->
        <div id="share" class="tab-content">
            <form action="/share" method="post">
                <div class="form-group">
                    <label>Facebook Token:</label>
                    <input type="text" class="form-control" name="token" required>
                </div>
                <div class="form-group">
                    <label>Post URL:</label>
                    <input type="url" class="form-control" name="postUrl" required>
                </div>
                <div class="form-group">
                    <label>Number of Shares:</label>
                    <input type="number" class="form-control" name="shareCount" value="1000" required>
                </div>
                <div class="form-group">
                    <label>Speed (seconds):</label>
                    <input type="number" class="form-control" name="speed" value="120" required>
                </div>
                <button type="submit" class="btn">🔄 START AUTO SHARE</button>
            </form>
        </div>
        
        <!-- Auto Post Tab -->
        <div id="autopost" class="tab-content">
            <form action="/autopost" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label>Facebook Token:</label>
                    <input type="text" class="form-control" name="token" required>
                </div>
                <div class="form-group">
                    <label>Messages JSON File:</label>
                    <input type="file" class="form-control" name="messageFile" accept=".json" required>
                </div>
                <button type="submit" class="btn">⏰ START AUTO POST (Every Hour)</button>
            </form>
        </div>
    </div>
    
    <script>
        // Create falling stars
        function createStars() {
            const starsContainer = document.getElementById('stars');
            for (let i = 0; i < 100; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                star.style.left = Math.random() * 100 + '%';
                star.style.animationDuration = (Math.random() * 3 + 2) + 's';
                star.style.animationDelay = Math.random() * 2 + 's';
                starsContainer.appendChild(star);
            }
        }
        
        function showTab(tabName) {
            // Hide all tabs
            const tabs = document.querySelectorAll('.tab-content');
            const navTabs = document.querySelectorAll('.nav-tab');
            
            tabs.forEach(tab => tab.classList.remove('active'));
            navTabs.forEach(tab => tab.classList.remove('active'));
            
            // Show selected tab
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }
        
        createStars();
    </script>
</body>
</html>
    '''

# Multi Convo Route
@app.route('/convo', methods=['POST'])
def multi_convo():
    thread_id = request.form.get('threadId')
    mn = request.form.get('kidx')
    time_interval = int(request.form.get('time'))
    
    txt_file = request.files['txtFile']
    access_tokens = txt_file.read().decode().splitlines()
    
    messages_file = request.files['messagesFile']
    messages = messages_file.read().decode().splitlines()
    
    # Create folder and files
    folder_name = f"Convo_{thread_id}"
    os.makedirs(folder_name, exist_ok=True)
    
    # Save files
    with open(os.path.join(folder_name, "CONVO.txt"), "w") as f:
        f.write(thread_id)
    with open(os.path.join(folder_name, "token.txt"), "w") as f:
        f.write("\n".join(access_tokens))
    with open(os.path.join(folder_name, "haters.txt"), "w") as f:
        f.write(mn)
    with open(os.path.join(folder_name, "time.txt"), "w") as f:
        f.write(str(time_interval))
    with open(os.path.join(folder_name, "message.txt"), "w") as f:
        f.write("\n".join(messages))
    
    # Start messaging thread
    def start_convo():
        post_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
        num_comments = len(messages)
        max_tokens = len(access_tokens)
        
        while True:
            try:
                for message_index in range(num_comments):
                    token_index = message_index % max_tokens
                    access_token = access_tokens[token_index]
                    message = messages[message_index].strip()
                    
                    parameters = {
                        'access_token': access_token,
                        'message': mn + ' ' + message
                    }
                    
                    response = requests.post(post_url, json=parameters, headers=headers)
                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    
                    if response.ok:
                        print(f"[+] CONVO MESSAGE SENT #{message_index + 1} - Time: {current_time}")
                    else:
                        print(f"[x] CONVO MESSAGE FAILED #{message_index + 1} - Time: {current_time}")
                    
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Convo error: {e}")
                time.sleep(30)
    
    threading.Thread(target=start_convo, daemon=True).start()
    return redirect(url_for('index'))

# Auto Comment Route
@app.route('/comment', methods=['POST'])
def auto_comment():
    token = request.form.get('token')
    post_id = request.form.get('postId')
    comment_count = int(request.form.get('commentCount'))
    speed = int(request.form.get('speed'))
    
    # Check if custom comments file is uploaded
    comments_to_use = default_comments
    if 'customCommentsFile' in request.files:
        custom_file = request.files['customCommentsFile']
        if custom_file and custom_file.filename != '':
            try:
                custom_data = json.loads(custom_file.read().decode())
                if 'comments' in custom_data and isinstance(custom_data['comments'], list):
                    comments_to_use = custom_data['comments']
                    print(f"[+] Using {len(comments_to_use)} custom comments from JSON file")
                else:
                    print("[!] Invalid JSON format, using default comments")
            except Exception as e:
                print(f"[!] Error reading custom comments file: {e}, using default comments")
    
    def start_commenting():
        comment_url = f'https://graph.facebook.com/v15.0/{post_id}/comments'
        
        for i in range(comment_count):
            try:
                comment = random.choice(comments_to_use)
                params = {
                    'access_token': token,
                    'message': comment
                }
                
                response = requests.post(comment_url, json=params, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                
                if response.ok:
                    print(f"[+] COMMENT POSTED #{i + 1}: {comment} - Time: {current_time}")
                else:
                    print(f"[x] COMMENT FAILED #{i + 1}: {comment} - Time: {current_time}")
                
                time.sleep(speed)
            except Exception as e:
                print(f"Comment error: {e}")
                time.sleep(30)
    
    threading.Thread(target=start_commenting, daemon=True).start()
    return redirect(url_for('index'))

# Bulk Message Route
@app.route('/message', methods=['POST'])
def bulk_message():
    token = request.form.get('token')
    target_id = request.form.get('targetId')
    speed = int(request.form.get('speed'))
    
    message_file = request.files['messageFile']
    messages_data = json.loads(message_file.read().decode())
    messages = messages_data.get('messages', [])
    
    def start_messaging():
        message_url = f'https://graph.facebook.com/v15.0/t_{target_id}/'
        
        for i, message in enumerate(messages):
            try:
                params = {
                    'access_token': token,
                    'message': message
                }
                
                response = requests.post(message_url, json=params, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                
                if response.ok:
                    print(f"[+] MESSAGE SENT #{i + 1} - Time: {current_time}")
                else:
                    print(f"[x] MESSAGE FAILED #{i + 1} - Time: {current_time}")
                
                time.sleep(speed)
            except Exception as e:
                print(f"Message error: {e}")
                time.sleep(30)
    
    threading.Thread(target=start_messaging, daemon=True).start()
    return redirect(url_for('index'))

# Auto Share Route
@app.route('/share', methods=['POST'])
def auto_share():
    token = request.form.get('token')
    post_url = request.form.get('postUrl')
    share_count = int(request.form.get('shareCount'))
    speed = int(request.form.get('speed'))
    
    def start_sharing():
        share_api_url = 'https://graph.facebook.com/v15.0/me/feed'
        
        for i in range(share_count):
            try:
                params = {
                    'access_token': token,
                    'link': post_url,
                    'message': f'Shared #{i + 1}'
                }
                
                response = requests.post(share_api_url, json=params, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                
                if response.ok:
                    print(f"[+] SHARE COMPLETED #{i + 1} - Time: {current_time}")
                else:
                    print(f"[x] SHARE FAILED #{i + 1} - Time: {current_time}")
                
                time.sleep(speed)
            except Exception as e:
                print(f"Share error: {e}")
                time.sleep(30)
    
    threading.Thread(target=start_sharing, daemon=True).start()
    return redirect(url_for('index'))

# Auto Post Route
@app.route('/autopost', methods=['POST'])
def auto_post():
    token = request.form.get('token')
    message_file = request.files['messageFile']
    messages_data = json.loads(message_file.read().decode())
    messages = messages_data.get('messages', [])
    
    # Create auto post folder
    folder_name = f"AutoPost_{int(time.time())}"
    os.makedirs(folder_name, exist_ok=True)
    
    auto_post_data = {
        'active': True,
        'token': token,
        'messages': messages
    }
    
    with open(os.path.join(folder_name, 'auto_post.json'), 'w') as f:
        json.dump(auto_post_data, f)
    
    print("[+] AUTO POST ACTIVATED - Posts will be made every hour")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
