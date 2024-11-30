include "p16f84.inc" ; подключаем файл с описанием регистров
; Переменные
Schet	EQU 10h	; Счетчик нажатий
ZMl  	EQU 11h	; Младший байт задержки
ZSr 	EQU 12h	; Средний байт задержки
ZSt	    EQU 13h	; Старший байт задержки
Naj		EQU 14h	; Нажималась ли кнопка
Star	EQU 15h	; Номер режима
ORG 0		; Устанавливаем вектор сброса
	GOTO Start
ORG 0004h   ; Реакция на прерывание от таймера
	GOTO Timer
; Основная программа
Start
	BCF		STATUS, RP1
	BSF 	STATUS, RP0		; Выбираем банк памяти 1
	MOVLW	B'00011111'		; Маска порта А: 4-0 входы
	MOVWF	TRISA			; Заносим конфигурацию порта А
	MOVLW 	B'00000000'		; Маска порта В: 7-0 выходы
	MOVWF	TRISB			; Заносим конфигурацию порта В
	;настраиваем таймер
	MOVLW	B'00000111'		
	MOVWF	OPTION_REG
	BCF  	 STATUS, RP0    ; Выбираем банк памяти 0
	MOVLW	B'10100000'		;разрешаем прерывания	
	MOVWF	INTCON
	MOVLW	 h'0' 			;записываем значение в TMR0
	MOVWF	TMR0 			;запускаем таймер
	BCF		STATUS, RP0		; Выбираем банк памяти 0
	CLRF	Star			; Обнуляем номер режима
	MOVLW 1
	MOVWF	Schet			; заносим 1 в счетчик
	MOVF	Schet, 0
	MOVWF	PORTB			; Выводим его значение
	;0 - кнопка нажата
	;1 - кнопка не нажата
Start_1
	MOVF Star, 0 		;проверяем, изменился ли режим
	XORLW 0
	BTFSS STATUS, Z
	GOTO Start_2_2		;Если изменился, то меняем режим
	RRF 	Schet, 1	; Сдвигаем вправо
	MOVF	Schet, 0
	MOVWF	PORTB		; Выводим новое положение 
	MOVLW	0x3			; Загружаем задержку
	MOVWF	ZSt
	MOVLW	0x8
	MOVWF	ZSr
	MOVLW	0x7A
	MOVWF	ZMl
	CALL Zader
GOTO Start_1
Zader
	DECFSZ ZMl,1		; Уменьшаем младший байт, пока он не станет 0
	GOTO Zader
	DECFSZ ZSr,1		; Уменьшаем средний байт, пока он не станет 0
	GOTO Zader
	DECFSZ ZSt,1		; Уменьшаем старший байт, пока он не станет 0
	GOTO Zader	
RETURN
Start_1_1
	CLRF Star
	GOTO Start_1
Start_2_2
	CLRF Star
	GOTO Start_2
Start_2
	MOVF Star, 0 		;Проверяем, менялся ли режим
	XORLW 0
	BTFSS STATUS, Z
	GOTO Start_1_1		;Если менялся, то меняем режим
	RLF	Schet, 1		; Сдвигаем влево
	MOVF	Schet, 0
	MOVWF	PORTB		; Выводим новое положение
	MOVLW	0x3			; Загружаем задержку 
	MOVWF	ZSt
	MOVLW	0x8
	MOVWF	ZSr
	MOVLW	0x7A
	MOVWF	ZMl
	CALL Zader
GOTO Start_2
Timer
	BTFSC PORTA, 3		;проверяем, нажата ли кнопка
	GOTO PROVERKA2  	;если не нажата, проверяем, не была ли надата ранее
	GOTO Proverka1		;если она нажата, то ставим переменную в 1
Proverka1
	MOVLW 1				;записываем в Naj 1
	MOVWF Naj
	GOTO konetc
PROVERKA2
	MOVF Naj, 0			;Если Naj = 1 то кнопка была нажата, значит выполняем 
	XORLW 1				;переключение режима, иначе переходим в конец
	BTFSC STATUS, Z
	GOTO izmen			
	GOTO konetc
izmen
	MOVLW 1 
	MOVWF Star
	MOVLW 0 
	MOVWF Naj
	GOTO konetc
konetc
	BCF INTCON,02h
RETFIE 
END
