from flask import Flask, request, render_template, url_for
from twilio.twiml.messaging_response import MessagingResponse

from reply import fetch_reply

app = Flask(__name__, template_folder='templates')
@app.route("/")
def index():

    return render_template('index.html')


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = fetch_reply(msg, phone_no)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
