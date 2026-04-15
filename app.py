from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="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")

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    user_msg = request.form.get("Body", "")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_msg}
        ]
    )

    reply_text = response.choices[0].message.content
    resp = MessagingResponse()
    resp.message(reply_text)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
