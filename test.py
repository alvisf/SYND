from twilio.rest import Client
from flask import Flask, request, render_template, url_for
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator
from reply import fetch_reply

from twilio.rest import Client
translator = Translator()

msg = "naamaste"
language = translator.detect(msg).lang
if(translator.detect(msg).lang != "en"):
    
    msg = translator.translate(msg).text
# phone_no = request.form.get('From')
reply = fetch_reply(msg, "000000")

# Create reply
if language != "en":
    reply = translator.translate(reply, dest=language).text
#resp = MessagingResponse()
print(reply)

