; используем процессор PIC16F84, система исчисления десятичная
include "p16f84.inc" ; подключаем файл с описанием регистров
;Устанавливаем вектор сброса
ORG 0
GOTO Start
ORG 0004h
GOTO Timer
Timer:
DECFSZ 030h, 1
GOTO next
MOVLW B'00000000' ;запрещаем прерывания
MOVWF INTCON
next:
BCF INTCON,02h
RETFIE
Start
BCF STATUS, RP1
BSF STATUS, RP0 ; Выбираем банк памяти 1
;настраиваем таймер
MOVLW B'00000111'
MOVWF OPTION_REG
BCF STATUS, RP0 ; Выбираем банк памяти 0
MOVLW B'10100000' ;разрешаем прерывания
MOVWF INTCON
MOVLW h'98' ;записываем в ¤чейку 030 10
MOVWF 030h
MOVLW h'F0' ;записываем значение в TMR0
MOVWF TMR0 ;запускаем таймер
loop:
BTFSC INTCON, 5
GOTO loop
GOTO Start
END 