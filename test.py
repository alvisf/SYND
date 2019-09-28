from googletrans import Translator

translator = Translator()
alv = "hi" 
#"नमस्ते"

testText = translator.translate(alv, dest='hi')
#translator.detect(alv).lang
#translator.translate(alv).text
print(testText)