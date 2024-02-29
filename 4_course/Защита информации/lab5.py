"""
Задания:
1. Создать копию «Модели угроз», разработанной в предыдущей лабораторной работе.
2. Согласно Варианту написать программу на любом языке программирования, которая
зашифрует текст в вашем файле.
Вариант вычисляется по формуле: N%2+1= K, где N – номер студента в списке группы, K
– номер варианта. Вариант 1 реализует Шифр Цезаря, Вариант 2 – Шифр Виженера.
Требования
1. Программа считывает данные из файла. Допускается предварительный перевод файла
в удобный для работы формат.
2. Программа спрашивает «ключ» у пользователя.
3. Программа создаёт новый файл, помещая в него шифротекст, из которого удалены
знаки препинания, отступы, пробелы.
4. Программа «умеет» расшифровывать текст по запросу.
5. Программа не использует готовые криптографические библиотеки.
3. С использованием любого языка программирования написать программу, подбирающую
ключ к шифротексту методом подбора или с помощью частотного анализа.
"""

#   Определение варианта -  вариант 2
# N = 5
# K = N % 2 + 1
# print(K)


def coder():
    buffer_char = []
    key = int(input("Введите ключ: "))
    while key < 0:
        key = int(input("Введите ключ: "))

    with open("input.txt", "r") as input_file:
        while True:
            char = input_file.read(1)
            if not char:
                break
            for i in range(len(alphabet)):
                if char == alphabet[i]:
                    bias = i + key
                    if 0 <= i <= 25:
                        if bias <= 25:
                            coder_char = alphabet[bias]
                        else:
                            coder_char = alphabet[bias - 26]
                    elif 26 <= i <= 51:
                        if bias <= 51:
                            coder_char = alphabet[bias]
                        else:
                            coder_char = alphabet[bias - 26]
                    elif 52 <= i <= 84:
                        if bias <= 84:
                            coder_char = alphabet[bias]
                        else:
                            coder_char = alphabet[bias - 33]
                    else:
                        if bias <= len(alphabet) - 1:
                            coder_char = alphabet[bias]
                        else:
                            coder_char = alphabet[bias - 33]
                    buffer_char.append(coder_char)
                    break

    with open("output.txt", "w") as output_file:
        for i in range(len(buffer_char)):
            output_file.write(buffer_char[i])


def decoder():
    buffer_char = []
    with open("output.txt", "r") as input_file:
        while True:
            char = input_file.read(1)
            if not char:
                break
            buffer_char.append(char)

    right_text = False
    key = 0
    while right_text == False:
        key += 1
        new_buffer_char = []
        for j in range(len(buffer_char)):
            for i in range(len(alphabet)):
                if buffer_char[j] == alphabet[i]:
                    subb = i - key
                    if 0 <= i <= 25:
                        if subb >= 0:
                            decoder_char = alphabet[subb]
                        else:
                            bias = 0 - subb
                            decoder_char = alphabet[26 - bias]
                    elif 26 <= i <= 51:
                        if subb >= 26:
                            decoder_char = alphabet[subb]
                        else:
                            bias = 26 - subb
                            decoder_char = alphabet[52 - bias]
                    elif 52 <= i <= 84:
                        if subb >= 52:
                            decoder_char = alphabet[subb]
                        else:
                            bias = 52 - subb
                            decoder_char = alphabet[85 - bias]
                    else:
                        if subb >= 85:
                            decoder_char = alphabet[subb]
                        else:
                            bias = 85 - subb
                            decoder_char = alphabet[len(alphabet) - bias]
                    new_buffer_char.append(decoder_char)
                    break
        print(new_buffer_char)

        check = str(input("Расшифрован ли текст в файле? Y/N\t"))
        if check == "Y" or check == "y" or check == "Yes" or check == "yes" or check == "YES":
            right_text == True
            break
        elif check == "N" or check == "n" or check == "No" or check == "no" or check == "NO":
            right_text == False
        # else:
        #     check = str(input("Расшифрован ли текст в файле? Y/N\t"))
        #     key -= 1

    with open("input_new.txt", "w") as output_file:
        for i in range(len(new_buffer_char)):
            output_file.write(new_buffer_char[i])


if __name__ == '__main__':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
                'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
                'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    print("1. Кодирование шифром Цезаря.")
    print("2. Декодирование шифра Цезаря.")
    variant = int(input("Введите вариант работы программы: "))
    while variant < 1 or variant > 2:
        variant = int(input("Введите вариант работы программы: "))

    if variant == 1:
        coder()
    elif variant == 2:
        decoder()
