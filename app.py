from twilio.rest import Client
from flask import Flask, request, render_template, url_for
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator
from reply import fetch_reply

from twilio.rest import Client
translator = Translator()
# phn = 919677051645

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC77ca0614a6d1238cffaac5e095139f83'
auth_token = '749bf3da242c6716be74bf2e1465805f'
client = Client(account_sid, auth_token)


def send_msg(x,y):
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN

    # this is the Twilio sandbox testing number
    from_whatsapp_number = 'whatsapp:+14155238886',
    # print(from_whatsapp_number)
    # replace this number with your own WhatsApp Messaging number
    if y is None:
        to_whatsapp_number = 'whatsapp:+919677051645'
    else:
        to_whatsapp_number = 'whatsapp:+91'+ str(y)

    client.messages.create(body=x,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number,media_url=["https://demo.twilio.com/owl.png"] )


app = Flask(__name__, template_folder='templates')
@app.route("/")
def index():

    return render_template('index.html')


@app.route("/", methods=['POST'])
def sendingmsg():
    phnum = None
    msg = request.form['text']
    phnum = request.form['text']
    send_msg(msg,phnum)
    return render_template('index.html')

int num_media
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')


    num_media = int(request.values.get("NumMedia"))
    resp = MessagingResponse()
    if not num_media:
        msg = resp.message("Send us an image!")
    else:
        msg = resp.message("Thanks for the image(s).")
    msg.media(num_media)


    language = translator.detect(msg).lang
    if(translator.detect(msg).lang != "en"):
        msg = translator.translate(msg).text
    phone_no = request.form.get('From')
    reply = fetch_reply(msg, phone_no)

    # Create reply
    if language != "en":
        reply = translator.translate(reply, dest=language).text
    #resp = MessagingResponse()
    resp.message(reply)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
