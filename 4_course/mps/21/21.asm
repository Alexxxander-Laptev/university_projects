include "p16f84.inc" ; подключаем файл с описанием регистров
;Переменные
First EQU 10h
;Устанавливаем вектор сброса
ORG 0
GOTO Start
Start
BCF STATUS, RP1
BSF STATUS, RP0 ; Выбираем банк памяти 1
MOVLW B'00011111' ; Настраиваем порт А как вход
MOVWF TRISA
MOVLW B'00000000' ; Настраиваем порт В как выход
MOVWF TRISB
BCF STATUS, RP0 ; Выбираем банк памяти 0
Metka:
CLRW
CLRF First
MOVF PORTA,0 ; Читаем старшую половину байта из порта А в W
ANDLW 0x0F ; Убираем старшую половину байта
MOVWF First ; Переносим значение в ячейку
SWAPF First, 1
MOVF PORTA,0 ; Читаем младшую половину байта
ANDLW 0x0F ; Убираем старшую половину байта
IORWF First,0 ; Собираем обе половины байта, результат в W
ADDLW 5 ; Складываем W с числом 5, результат в W
MOVWF PORTB ; Записываем результат в порт B
CLRW ; Очищаем регистр W
BTFSC STATUS,C
INCF W,0
MOVWF PORTB ; Записываем перенос в порт B
GOTO Metka
END