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


def send_msg(x,y,z):
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN

    # this is the Twilio sandbox testing number
    from_whatsapp_number = 'whatsapp:+14155238886',
    # print(from_whatsapp_number)
    # replace this number with your own WhatsApp Messaging number
    media_url_link=z
    if type(y) is not int:
        to_whatsapp_number = 'whatsapp:+919677051645'
    else:
        to_whatsapp_number = 'whatsapp:+91'+ str(y)

    client.messages.create(body=x,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number,
                           media_url=[media_url_link])


app = Flask(__name__, template_folder='templates')
@app.route("/")
def index():

    return render_template('index.html')


@app.route("/", methods=['POST'])
def sendingmsg():
    msg = request.form['text']
    phnum = request.form['phno']
    murl = request.form['murl']
    send_msg(msg,phnum,murl)
    return render_template('index.html')


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    language = translator.detect(msg).lang
    if(translator.detect(msg).lang != "en"):
        msg = translator.translate(msg).text
    phone_no = request.form.get('From')
    reply = fetch_reply(msg, phone_no)

    # Create reply
    if language != "en":
        reply = translator.translate(reply, dest=language).text
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

@app.route("/appstat", methods=['POST'])
def appstats():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    
    reply = msg.status

    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
