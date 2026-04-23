import csv
import json

# Load knowledge base
def load_knowledge():
    with open("knowledge.json", "r") as file:
        return json.load(file)

kb = load_knowledge()


# Get pricing info (RAG)
def get_pricing():
    basic = kb["pricing"]["basic"]
    pro = kb["pricing"]["pro"]

    return f"""
📦 Basic Plan: {basic['price']}
   - {', '.join(basic['features'])}

🚀 Pro Plan: {pro['price']}
   - {', '.join(pro['features'])}
"""


# Intent detection
def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in user_input for word in ["price", "cost", "plan", "pricing"]):
        return "pricing"

    elif any(word in user_input for word in ["buy", "subscribe", "start", "try", "want", "interested"]):
        return "high_intent"

    else:
        return "general"


# Mock API function
def mock_lead_capture(name, email, platform):
    with open("leads.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, platform])

    print(f"\n✅ Lead saved: {name}, {email}, {platform}")

# State management
state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}


# Chat loop
while True:
    user = input("\nYou: ")

    # ✅ Exit condition (FIRST)
    if user.lower().strip() in ["exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break

    # ✅ If collecting details
    if state["intent"] == "high_intent":

        if state["name"] is None:
            state["name"] = user
            print("Bot: Please provide your email.")
            continue

        elif state["email"] is None:
            if "@" not in user:
                print("Bot: Please enter a valid email.")
                continue

            state["email"] = user
            print("Bot: Which platform do you create content on? (YouTube, Instagram, etc.)")
            continue

        elif state["platform"] is None:
            state["platform"] = user

            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )

            print("Bot: Thanks! Our team will contact you soon. 🚀")

            # Reset state
            state = {
                "intent": None,
                "name": None,
                "email": None,
                "platform": None
            }
            continue

    # Detect intent
    intent = detect_intent(user)

    if intent == "greeting":
        print("Bot: Hi! 👋 I can help you with AutoStream pricing or getting started.")

    elif intent == "pricing":
        print("Bot:", get_pricing())

    elif intent == "high_intent":
        state["intent"] = "high_intent"
        print("Bot: Great! Can I have your name?")

    else:
        print("Bot: Can you clarify?")