print("Добро пожаловть в программу шифрования")
print('Нужно зашифровать(1) или расшифровать(-1) сообщение?')
variant = int(input())
print('Какой язык? Русский(ru)/Ангийский(en)')
language = input()
print('Шаг сдвига шифра известен?(да(y)/нет(n))')
know = input()
if know == 'y':
    print('Шаг сдвига шифра?')
    step = int(input())

alphabet_ru = ['а','б','в','г','д','е','ж','з','и','й',
               'к','л','м','н','о','п','р','с','т','у',
               'ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

alphabet_en = ['a','b','c','d','e','f','g','h','i','j',
               'k','l','m','n','o','p','q','r','s','t',
               'u','v','w','x','y','z']

punctuation = '!#$%&*+-=?@^_,."'

print('Введите сообщение')
message = input()

def caesar_cipher(message):
    stroka = message.split()
    result = []

    for i in range(len(stroka)):
        word_res = ''
        for j in range(len(stroka[i])):
            word = stroka[i]
            if word[j] not in punctuation:
                if language == 'ru':
                    position = alphabet_ru.index(word[j].lower())
                    position += step*variant
                    if position > 31: position -= 31
                    word_res += (alphabet_ru[position])
                elif language == 'en':
                    position = alphabet_en.index(word[j].lower())
                    position += step*variant
                    if position > 25: position -= 25
                    word_res += (alphabet_en[position])
            else: word_res += word[j]
        result.append(word_res)

    return result

if know != 'y':
    if language == 'en': stup = 26
    else: stup = 32
    for i in range(1, stup):
        step = i
        print(f'step = {i}')
        print(*caesar_cipher(message))
else: print(*caesar_cipher(message))