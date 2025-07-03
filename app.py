from flask import Flask, request, redirect, render_template
import requests

app = Flask(__name__)

BOT_TOKEN = "7869806890:AAEMCa1QDknkmWgMFZ97D2WIvkdBsL0c90E"
ADMIN_ID = "1722376406"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_to_telegram():
    if "screenshot" not in request.files:
        return "No file uploaded", 400

    screenshot = request.files["screenshot"]
    pubg_id = request.form.get("pubg_id", "ID kiritilmagan")

    # Buyurtmani yuborish
    files = {
        "photo": (screenshot.filename, screenshot.stream, screenshot.mimetype)
    }
    caption = f"📥 Yangi buyurtma!\nPUBG ID: {pubg_id}"
    response = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
        data={"chat_id": ADMIN_ID, "caption": caption},
        files=files
    )

    if response.status_code == 200:
        # Xabar ID sini olish
        result = response.json()
        message_id = result["result"]["message_id"]

        # Inline tugmalar bilan javob variantlarini yuborish
        keyboard = {
            "inline_keyboard": [[
                {"text": "✅ UC tushdi", "callback_data": f"uc_tushdi:{pubg_id}"},
                {"text": "❌ UC tushmadi", "callback_data": f"uc_tushmadi:{pubg_id}"}
            ]]
        }
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": ADMIN_ID,
                "text": "Buyurtmaga javob bering:",
                "reply_to_message_id": message_id,
                "reply_markup": keyboard
            }
        )

        return redirect("/")
    else:
        return f"Xatolik yuz berdi: {response.text}", 500

if __name__ == "__main__":
    app.run(debug=True)
