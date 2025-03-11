# 🚀 Auto-Tweet Bot  
> **AI-powered automated tweeting bot using OpenAI & X API**  

---

## 📌 Overview  
This project automates the process of generating and posting tweets using **ChatGPT (GPT-4-Turbo)** and the **Twitter (X) API**. It allows seamless scheduling of AI-powered tweets on X (Twitter) without manual intervention.  

### ✨ Features  
✅ AI-generated tweets using **OpenAI API**  
✅ Auto-post tweets via **X API**  
✅ Secure API key storage using **dotenv**  
✅ Free automation via **GitHub Actions** or **Crontab**  

---

## 📂 Project Structure  
```
auto-tweet-bot/
│── scripts/
│   ├── auto_tweet.py       # Main script for generating & posting tweets
│   ├── test_openai.py      # Test script for OpenAI API connection
│── .gitignore              # Ignore unnecessary files
│── .env                    # Stores API keys (not tracked by Git)
│── requirements.txt        # Project dependencies
│── README.md               # Documentation
│── venv/                   # (Optional) Virtual environment
```

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/itxcrusher/auto-tweet-bot.git
cd auto-tweet-bot
```

### 2️⃣ Create & Activate Virtual Environment  
```bash
# Create Virtual Environment
python -m venv venv  

# Activate (Windows - Git Bash)
source venv/Scripts/activate

# Activate (Windows - CMD/PowerShell)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup  

### 4️⃣ Configure `.env` File  
1. Create a `.env` file in the project root.  
2. Add the following lines and replace with your actual keys:  

```
OPENAI_API_KEY=your_openai_api_key
X_API_KEY=your_X_api_key
X_API_SECRET=your_x_api_secret
X_ACCESS_TOKEN=your_x_access_token
X_ACCESS_SECRET=your_x_access_secret
```

---

## 📝 Usage  

### 5️⃣ Test OpenAI API Connection  
```bash
python scripts/test_openai.py
```
✅ If successful, it will generate a sample AI-powered tweet.  

### 6️⃣ Run Auto-Tweet Script Manually  
```bash
python scripts/auto_tweet.py
```
✅ This will generate and post a tweet automatically.  

---

## ⏳ Automate Tweeting  

### **Option 1: GitHub Actions (Cloud-Based, Free)**  
1. Push the project to GitHub.  
2. Add API keys in **GitHub Secrets**.  
3. Use the `tweet_schedule.yml` workflow to automate tweeting.  

### **Option 2: Crontab (Local Automation)**  
1. Open terminal and edit crontab:  
```bash
crontab -e
```
2. Add this line to schedule the script daily at 10 AM:  
```
0 10 * * * /usr/bin/python3 /path/to/scripts/auto_tweet.py
```

---

## 💡 Next Steps  
🔹 Extend to **generate X threads**  
🔹 Improve tweet **quality & engagement**  
🔹 Add **reply automation** for increased interaction  

🚀 **Happy Tweeting!** 🎯  

---

## 📜 License  
This project is **open-source** and free to use.  
Feel free to contribute and improve it!  

---