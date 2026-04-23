from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)

# ---------- INTENT ----------
def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in user_input for word in ["how are you", "how r u", "what's up"]):
        return "smalltalk"

    elif any(word in user_input for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"

    elif any(word in user_input for word in ["buy", "subscribe", "start", "want"]):
        return "high_intent"

    else:
        return "general"


# ---------- PRICING ----------
def get_pricing():
    return "Basic Plan: $29/month | Pro Plan: $79/month"


# ---------- SAVE CHAT ----------
def save_chat(user, bot):
    try:
        with open("chat_log.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([user, bot])
    except:
        pass


# ---------- SAVE LEAD ----------
def save_lead(name, email, platform):
    try:
        with open("leads.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, email, platform])
    except:
        pass


# ---------- STATE ----------
state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}


# ---------- HOME ----------
@app.route("/")
def home():
    return render_template("index.html")


# ---------- CHAT ----------
@app.route("/chat", methods=["POST"])
def chat():
    user = request.json.get("message", "").lower()

    if "instagram" in user:
        reply = "To grow Instagram:\n1. Post daily\n2. Use reels\n3. Follow trends\n4. Engage with audience"
    
    elif "youtube" in user:
        reply = "To grow YouTube:\n1. Consistent uploads\n2. Good thumbnails\n3. SEO titles\n4. Watch time focus"
    
    else:
        reply = "Hello! Ask me about Instagram or YouTube growth."

    return jsonify({"reply": reply})

    # ---------- LEAD FLOW ----------
    if state["intent"] == "high_intent":

        if state["name"] is None:
            state["name"] = user
            return jsonify({"reply": "Please provide your email."})

        elif state["email"] is None:
            state["email"] = user
            return jsonify({"reply": "Which platform do you create content on?"})

        elif state["platform"] is None:
            state["platform"] = user

            save_lead(state["name"], state["email"], state["platform"])

            state["intent"] = None
            state["name"] = None
            state["email"] = None
            state["platform"] = None

            return jsonify({"reply": "Lead saved! Our team will contact you."})

    # ---------- NORMAL FLOW ----------
    intent = detect_intent(user)

    if intent == "greeting":
        reply = "Hey there!"

    elif intent == "smalltalk":
        reply = "I'm doing great! How can I help you today?"

    elif intent == "pricing":
        reply = get_pricing()

    elif intent == "high_intent":
        state["intent"] = "high_intent"
        reply = "Great! What's your name?"

    else:
        # 🔥 YOUR CUSTOM LOGIC HERE
        if "instagram" in user:
            reply = "To grow Instagram:\n1. Post daily\n2. Use reels\n3. Follow trends\n4. Engage with audience"
        
        elif "youtube" in user:
            reply = "To grow YouTube:\n1. Consistent uploads\n2. Good thumbnails\n3. SEO titles\n4. Watch time focus"
        
        else:
            reply = "I can help you grow your social media. Ask about Instagram or YouTube!"

    # ✅ ALWAYS RETURN (IMPORTANT)
    save_chat(user, reply)
    print("REPLY:", reply)

    return jsonify({"reply": reply})
if __name__ == "__main__":
    app.run(debug=True)