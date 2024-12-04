translatedText = ''
def translate(text):
    global translatedText
    invalidletters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', '.', ',', '-', '?', '!']
    string = ''
    for i in range(len(text)):
        if not text[i].lower() in invalidletters:
            string += text[i]
    if ' ' in string:
        string = ' '.join(string.split())
    translatedText += string