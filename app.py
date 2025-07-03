from flask import Flask, request, redirect, render_template
import requests
import os

app = Flask(__name__)

BOT_TOKEN = "7869806890:AAEMCa1QDknkmWgMFZ97D2WIvkdBsL0c90E"
ADMIN_ID = "1722376406"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_to_telegram():
    if "screenshot" not in request.files:
        return "No file uploaded", 400

    screenshot = request.files["screenshot"]
    pubg_id = request.form.get("pubg_id", "ID kiritilmagan")

    files = {
        "photo": (screenshot.filename, screenshot.stream, screenshot.mimetype)
    }
    data = {
        "chat_id": ADMIN_ID,
        "caption": f"📥 Yangi buyurtma!\nPUBG ID: {pubg_id}"
    }
    response = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto", data=data, files=files)

    if response.status_code == 200:
        return redirect("/")
    else:
        return f"Xatolik yuz berdi: {response.text}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
