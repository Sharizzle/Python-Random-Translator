from googletrans import Translator, LANGUAGES
from random import choice

translator = Translator()


def translate(phrase, n=20):
    current_lang = ''
    current_phrase = ''
    for i in range(n-1):
        dest = choice(list(LANGUAGES.keys()))
        if i == 0:
            translated = translator.translate(phrase, src="en", dest=dest)
            current_lang = dest
            current_phrase = translated.text
        else:
            translated = translator.translate(
                current_phrase, src=current_lang, dest=dest)
            current_lang = dest
            current_phrase = translated.text

    final = translator.translate(current_phrase, src=current_lang, dest="en")

    return final.text


phrase = input("Enter the sentence here: ")
number = int(input("Enter the number of times to translate the sentence: "))

print(f"Output: {translate(phrase, number)}")
