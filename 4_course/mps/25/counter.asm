include "p16f84.inc"

PushCounter EQU 10h;Счетчик нажатий
Counter0 EQU 11h; Delay
Counter1 EQU 12h; Delay
Counter2 EQU 13h; Delay
org 0

GOTO Start
Start
BSF STATUS, RP0
MOVLW b'00011111'; А: 4-0 входы
MOVWF TRISA; Заносим конфигурацию порта А
MOVLW b'00000000'; В: 7-0 выходы
MOVWF TRISB; Заносим конфигурацию порта В
BCF STATUS, RP0; Выбираем банк памяти 0
MOVLW B'00000000'; инициализация порта B нулем
MOVWF PORTB
MOVLW 0x00; инициализация счетчика нулем
MOVWF PushCounter

CheckPushButton; проверка на нажатие 0 кнопки
BTFSC PORTA,RA0
GOTO CheckPushButton; если не нажата возвращаемся обратно
CALL Delay ; 10мс если нажата кнопка переходим на подпрограмму задержки(дребезг)
CheckReleaseButton; кнопка отпущена
BTFSS PORTA,RA0
GOTO CheckReleaseButton
INCF PushCounter; если кнопка отпущена инкрементируем счетчик
MOVFW PushCounter
MOVWF PORTB; вывод значения счетчика в порт B 
GOTO CheckPushButton

Delay
MOVLW 02h
MOVWF Counter0 ; мс
MOVLW 0Dh
MOVWF Counter1 ; мс
MOVLW 0FFh
MOVWF Counter2 ; мс
Count0
Count1
Count2
DECFSZ Counter2
GOTO Count2
DECFSZ Counter1
GOTO Count1
DECFSZ Counter0
GOTO Count0 ; мс
RETURN ; мс
END