from googletrans import Translator

def translate_text(text, language_ru_or_en):
    translator = Translator()
    translated_text = translator.translate(text, dest=f'{language_ru_or_en}').text
    return translated_text

while True:
    choose = input("Translation from English into Russian (ru) or from Russian to English (en)")
    text = input("Enter your text that must be translated   ")
    translated_text = translate_text(text,choose)
    print(translated_text)
