#-*-coding: utf8 -*-

MorseCode = [('A', '.-'), ('B', '-...'), ('W', '.--'), ('G', '--.'), ('D', '-..'), ('E', '.'), ('V', '...-'), ('Z', '--..'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'), ('F', '..-.'), ('H', '....'), ('C', '-.-.'), ('.', '......'), (',', '.-.-.-'), (':', '---...'), (';', '-.-.-.'), ('"', '-...-.'), ('-', '-....-'), ('?', '..--..'), ('!', '--..--'), ('1', '.----'), ('2', '..---'), ('3', '...--'),  ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'), ('8', '---..'), ('9', '----.'), ('0', '-----')]
MorseCode_rus = [('А', '.-'), ('Б', '-...'), ('В', '.--'), ('Г', '--.'), ('Д', '-..'), ('Е', '.'), ('Ё', '.'), ('Ж', '...-'), ('З', '--..'), ('И', '..'), ('Й', '.---'), ('К', '-.-'), ('Л', '.-..'), ('М', '--'), ('Н', '-.'), ('О', '---'), ('П', '.--.'), ('Р', '.-.'), ('С', '...'), ('Т', '-'), ('У', '..-'), ('Ф', '..-.'), ('Х', '....'), ('Ц', '-.-.'), ('Ч', '---.'), ('Ш', '----'), ('Щ', '--.-'), ('Ъ', '--.--'), ('Ы', '-.--'), ('Ь', '-..-'), ('Э', '..-..'), ('Ю', '..--'), ('Я', '.-.-')]

def main():
    global MorseCode_rus, MorseCode
    language = input('Russian/English (1/2): ')
    if language == '1':
        vocabulary = MorseCode_rus + MorseCode
    elif language == '2':
        vocabulary = MorseCode
    query = input('1- Кодировать, 2 - Декодировать : ')
    while query != '1' and query != '2':
        query = input('1- Кодировать, 2 - Декодировать : ')
    if query == '1':
        text = input('Введите текст: ')
        encodeToMorse(vocabulary, text)
    elif query == '2':
        code = input('Введите код: ')
        decodeFromMorse(vocabulary, code)
        
def findCodeByLetter(array, letter):
    for data in array:
        if data[0] == letter.lower() or data[0] == letter.upper():
            return data[1]
    return ''

def findLetterByCode(array, code):
    for data in array:
        if data[1] == code:
            return data[0]
    return ''
        
def encodeToMorse(vocabulary, text):
    encode_text = ''
    for i in range(len(text)):
        encode_text += findCodeByLetter(vocabulary, text[i]) + ' '
    print(encode_text)
    return encode_text

def decodeFromMorse(vocabulary, code):
    decode_text = ''
    for symbol in code.split():
        decode_text += findLetterByCode(vocabulary, symbol).lower()
    print(decode_text)
    return decode_text

main()