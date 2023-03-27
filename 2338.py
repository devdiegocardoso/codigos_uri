N = int(input())

START_CODE = 97
TOTAL_LETTERS = 26
letras = [x for x in range(START_CODE,START_CODE+TOTAL_LETTERS)]
#letras.append(ord(' '))

morse = [
    '=.===','===.=.=.=','===.=.===.=','===.=.=',
    '=','=.=.===.=','===.===.=','=.=.=.=',
    '=.=','=.===.===.===','===.=.===','=.===.=.=',
    '===.===','===.=','===.===.===','=.===.===.=',
    '===.===.=.===','=.===.=','=.=.=','===',
    '=.=.===','=.=.=.===','=.===.===','===.=.=.===',
    '===.=.===.===','===.===.=.='
    ]

def trade_index(index):
    return START_CODE + index

for i in range(N):
    morse_message = input()
    words = morse_message.split('.......')
    translated_word = ''
    for word in words:
        chars = word.split('...')
        for char in chars:
            translated_word += chr(letras[morse.index(char)])
        if len(words) > 1:
            translated_word += ' '
    print(translated_word.strip())