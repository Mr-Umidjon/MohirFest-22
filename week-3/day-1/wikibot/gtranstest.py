from googletrans import Translator

translator = Translator()

translation = translator.translate('Mening ismim Umidjon', src='uz', dest='ko')

print(translation)
print(translation.text)
