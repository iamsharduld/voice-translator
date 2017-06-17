import translator, textTospeech, speechTotext


speechTotext = speechTotext.run()

data = translator.translator(speechTotext)
textTospeech.run(data)


