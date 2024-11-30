include "p16f84.inc" ; подключаем файл с описанием регистров
; Переменные
Counter	EQU 10h				; Счетчик нажатий
DelJr  	EQU 11h				; Младший байт задержки
DelMl 	EQU 12h				; Средний байт задержки
DelSr   EQU 13h				; Старший байт задержки
ORG 0						; Устанавливаем вектор сброса
	GOTO Start
; Основная программа
Start
	BCF		STATUS, RP1
	BSF 	STATUS, RP0		; Выбираем банк памяти 1
	MOVLW	B'00011111'		; Маска порта А: 4-0 входы
	MOVWF	TRISA			; Заносим конфигурацию порта А
	MOVLW 	B'00000000'		; Маска порта В: 7-0 выходы
	MOVWF	TRISB			; Заносим конфигурацию порта В

	BCF		STATUS, RP0		; Выбираем банк памяти 0
	MOVLW	1
	MOVWF	Counter			; заносим 1 в счетчик
	MOVF	Counter, 0
	MOVWF	PORTB			; Выводим его значение
	;0 - кнопка нажата
	;1 - кнопка не нажата
	GOTO	Mode_1

; Режимы
Mode_1
b31
	btfsc	PORTA, 3
	goto	b41
	call	Anti_bounce
	goto	Mode_2	
b41
	btfsc	PORTA, 4
	goto	rez1
	call	Anti_bounce
	goto	Invert_mode_1

;	BTFSS	PORTA, 3
;	GOTO	Mode_2
;	BTFSS	PORTA, 4
;	GOTO	Invert_mode_1
rez1
	RRF 	Counter, 1		; Сдвигаем вправо
	MOVF	Counter, 0
	MOVWF	PORTB			; Выводим новое положение 
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Mode_1
Mode_2
;	BTFSS	PORTA, 3
;	GOTO	Mode_3
;	GOTO	Anti_bounce
;	BTFSS	PORTA, 4
;	GOTO	Invert_mode_2
;	GOTO	Anti_bounce

;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b32
	btfsc	PORTA, 3
	goto	b42
	call	Anti_bounce
	goto	Mode_3	
b42
	btfsc	PORTA, 4
	goto	rez2
	call	Anti_bounce
	goto	Invert_mode_2

rez2
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b322
	btfsc	PORTA, 3
	goto	b422
	call	Anti_bounce
	goto	Mode_3	
b422
	btfsc	PORTA, 4
	goto	rez22
	call	Anti_bounce
	goto	Invert_mode_2

rez22
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Mode_2
Mode_3
;	BTFSS	PORTA, 3
;	GOTO	Mode_4
;	BTFSS	PORTA, 4
;	GOTO	Invert_mode_3
;
;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b33
	btfsc	PORTA, 3
	goto	b43
	call	Anti_bounce
	goto	Mode_4
b43
	btfsc	PORTA, 4
	goto	rez3
	call	Anti_bounce
	goto	Invert_mode_3

rez3
	RRF 	Counter, 1	; Сдвигаем вправо
	RRF 	Counter, 1	; Сдвигаем вправо
	MOVF	Counter, 0
	MOVWF	PORTB		; Выводим новое положение 
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Mode_3
Mode_4
;	BTFSS	PORTA, 3
;	GOTO	Mode_5
;	BTFSS	PORTA, 4
;	GOTO	Invert_mode_4
;
;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b34
	btfsc	PORTA, 3
	goto	b44
	call	Anti_bounce
	goto	Mode_5
b44
	btfsc	PORTA, 4
	goto	rez4
	call	Anti_bounce
	goto	Invert_mode_4

rez4
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BCF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b342
	btfsc	PORTA, 3
	goto	b442
	call	Anti_bounce
	goto	Mode_5
b442
	btfsc	PORTA, 4
	goto	rez42
	call	Anti_bounce
	goto	Invert_mode_4

rez42
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BSF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Mode_4
Mode_5
;	BTFSS	PORTA, 3
;	GOTO	Mode_6
;	BTFSS	PORTA, 4
;	GOTO	Invert_mode_5

;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b35
	btfsc	PORTA, 3
	goto	b45
	call	Anti_bounce
	goto	Mode_6
b45
	btfsc	PORTA, 4
	goto	rez5
	call	Anti_bounce
	goto	Invert_mode_5

rez5
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b352
	btfsc	PORTA, 3
	goto	b452
	call	Anti_bounce
	goto	Mode_6
b452
	btfsc	PORTA, 4
	goto	rez52
	call	Anti_bounce
	goto	Invert_mode_5

rez52
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Mode_5
Mode_6
;	BTFSS	PORTA, 3
;	GOTO	Mode_7
;	BTFSS	PORTA, 4
;	GOTO	Invert_mode_6

;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b36
	btfsc	PORTA, 3
	goto	b46
	call	Anti_bounce
	goto	Mode_7	
b46
	btfsc	PORTA, 4
	goto	rez6
	call	Anti_bounce
	goto	Invert_mode_6

rez6
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b362
	btfsc	PORTA, 3
	goto	b462
	call	Anti_bounce
	goto	Mode_7	
b462
	btfsc	PORTA, 4
	goto	rez62
	call	Anti_bounce
	goto	Invert_mode_6

rez62
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Mode_6
Mode_7
;	BTFSS	PORTA, 3
;	GOTO	Mode_8
;	BTFSS	PORTA, 4
;	GOTO	Invert_mode_7
;
;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b37
	btfsc	PORTA, 3
	goto	b47
	call	Anti_bounce
	goto	Mode_8
b47
	btfsc	PORTA, 4
	goto	rez7
	call	Anti_bounce
	goto	Invert_mode_7

rez7
	BCF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b371
	btfsc	PORTA, 3
	goto	b471
	call	Anti_bounce
	goto	Mode_8
b471
	btfsc	PORTA, 4
	goto	rez71
	call	Anti_bounce
	goto	Invert_mode_7

rez71
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b372
	btfsc	PORTA, 3
	goto	b472
	call	Anti_bounce
	goto	Mode_8
b472
	btfsc	PORTA, 4
	goto	rez72
	call	Anti_bounce
	goto	Invert_mode_7

rez72
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b373
	btfsc	PORTA, 3
	goto	b473
	call	Anti_bounce
	goto	Mode_8
b473
	btfsc	PORTA, 4
	goto	rez73
	call	Anti_bounce
	goto	Invert_mode_7

rez73
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Mode_7
Mode_8
;	call	Anti_bounce
;	BTFSS	PORTA, 3
;	GOTO	Mode_3
;	BTFSS	PORTA, 4
;	GOTO	Invert_mode_2
;
;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b38
	btfsc	PORTA, 3
	goto	b48
	call	Anti_bounce
	goto	Mode_1
b48
	btfsc	PORTA, 4
	goto	rez8
	call	Anti_bounce
	goto	Invert_mode_8

rez8
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b382
	btfsc	PORTA, 3
	goto	b482
	call	Anti_bounce
	goto	Mode_1
b482
	btfsc	PORTA, 4
	goto	rez82
	call	Anti_bounce
	goto	Invert_mode_8

rez82
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b383
	btfsc	PORTA, 3
	goto	b483
	call	Anti_bounce
	goto	Mode_1
b483
	btfsc	PORTA, 4
	goto	rez83
	call	Anti_bounce
	goto	Invert_mode_8

rez83
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b384
	btfsc	PORTA, 3
	goto	b484
	call	Anti_bounce
	goto	Mode_1
b484
	btfsc	PORTA, 4
	goto	rez84
	call	Anti_bounce
	goto	Invert_mode_8

rez84
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Mode_8

; Обратные режимы
Invert_mode_1
b31i
	btfsc	PORTA, 3
	goto	b41i
	call	Anti_bounce
	goto	Mode_2	
b41i
	btfsc	PORTA, 4
	goto	rez1i
	call	Anti_bounce
	goto	Mode_1

;	BTFSS	PORTA, 3
;	GOTO	Mode_2
;	BTFSS	PORTA, 4
;	GOTO	Mode_1

;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay
rez1i
	RLF 	Counter, 1		; Сдвигаем вправо
	MOVF	Counter, 0
	MOVWF	PORTB			; Выводим новое положение 
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Invert_mode_1
Invert_mode_2
;	BTFSS	PORTA, 3
;	GOTO	Mode_4
;	BTFSS	PORTA, 4
;	GOTO	Mode_3

;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b32i
	btfsc	PORTA, 3
	goto	b42i
	call	Anti_bounce
	goto	Mode_3	
b42i
	btfsc	PORTA, 4
	goto	rez2i
	call	Anti_bounce
	goto	Mode_2

rez2i
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b322i
	btfsc	PORTA, 3
	goto	b422i
	call	Anti_bounce
	goto	Mode_3	
b422i
	btfsc	PORTA, 4
	goto	rez22i
	call	Anti_bounce
	goto	Mode_2

rez22i
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Invert_mode_2
Invert_mode_3
;	BTFSS	PORTA, 3
;	GOTO	Mode_1
;	BTFSS	PORTA, 4
;	GOTO	Mode_8

;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b33i
	btfsc	PORTA, 3
	goto	b43i
	call	Anti_bounce
	goto	Mode_4
b43i
	btfsc	PORTA, 4
	goto	rez3i
	call	Anti_bounce
	goto	Mode_3

rez3i
	RLF		Counter, 1		; Сдвигаем влево
	RLF		Counter, 1		; Сдвигаем влево
	MOVF	Counter, 0
	MOVWF	PORTB		; Выводим новое положение
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Invert_mode_3
Invert_mode_4
;	BTFSS	PORTA, 3
;	GOTO	Mode_5
;	BTFSS	PORTA, 4
;	GOTO	Mode_4
;
;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b34i
	btfsc	PORTA, 3
	goto	b44i
	call	Anti_bounce
	goto	Mode_5
b44i
	btfsc	PORTA, 4
	goto	rez4i
	call	Anti_bounce
	goto	Mode_4

rez4i
	BCF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BCF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2			; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b342i
	btfsc	PORTA, 3
	goto	b442i
	call	Anti_bounce
	goto	Mode_5
b442i
	btfsc	PORTA, 4
	goto	rez42i
	call	Anti_bounce
	goto	Mode_4

rez42i
	BSF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BSF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2			; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Invert_mode_4
Invert_mode_5
;	BTFSS	PORTA, 3
;	GOTO	Mode_6
;	BTFSS	PORTA, 4
;	GOTO	Mode_5

;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b35i
	btfsc	PORTA, 3
	goto	b45i
	call	Anti_bounce
	goto	Mode_6
b45i
	btfsc	PORTA, 4
	goto	rez5i
	call	Anti_bounce
	goto	Mode_5

rez5i
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b352i
	btfsc	PORTA, 3
	goto	b452i
	call	Anti_bounce
	goto	Mode_6
b452i
	btfsc	PORTA, 4
	goto	rez52i
	call	Anti_bounce
	goto	Mode_5

rez52i
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Invert_mode_5
Invert_mode_6
;	BTFSS	PORTA, 3
;	GOTO	Mode_7
;	BTFSS	PORTA, 4
;	GOTO	Mode_6

;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b36i
	btfsc	PORTA, 3
	goto	b46i
	call	Anti_bounce
	goto	Mode_7	
b46i
	btfsc	PORTA, 4
	goto	rez6i
	call	Anti_bounce
	goto	Mode_6

rez6i
	BSF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b362i
	btfsc	PORTA, 3
	goto	b462i
	call	Anti_bounce
	goto	Mode_7	
b462i
	btfsc	PORTA, 4
	goto	rez62i
	call	Anti_bounce
	goto	Mode_6

rez62i
	BCF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Invert_mode_6
Invert_mode_7
;	BTFSS	PORTA, 3
;	GOTO	Mode_8
;	BTFSS	PORTA, 4
;	GOTO	Mode_7
;
;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay


b37i
	btfsc	PORTA, 3
	goto	b47i
	call	Anti_bounce
	goto	Mode_8
b47i
	btfsc	PORTA, 4
	goto	rez7i
	call	Anti_bounce
	goto	Mode_7

rez7i
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b371i
	btfsc	PORTA, 3
	goto	b471i
	call	Anti_bounce
	goto	Mode_8
b471i
	btfsc	PORTA, 4
	goto	rez71i
	call	Anti_bounce
	goto	Mode_7

rez71i
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b372i
	btfsc	PORTA, 3
	goto	b472i
	call	Anti_bounce
	goto	Mode_8
b472i
	btfsc	PORTA, 4
	goto	rez72i
	call	Anti_bounce
	goto	Mode_7

rez72i
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b373i
	btfsc	PORTA, 3
	goto	b473i
	call	Anti_bounce
	goto	Mode_8
b473i
	btfsc	PORTA, 4
	goto	rez73i
	call	Anti_bounce
	goto	Mode_7

rez73i
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BCF		PORTB, RB6
	BCF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Invert_mode_7
Invert_mode_8
;	BTFSS	PORTA, 3
;	GOTO	Mode_3
;	BTFSS	PORTA, 4
;	GOTO	Mode_2

;	MOVLW	02h				; Загружаем задержку
;	MOVWF	DelSr
;	MOVLW	0Dh
;	MOVWF	DelMl
;	MOVLW	0FFh
;	MOVWF	DelJr
;	CALL	Delay

b38i
	btfsc	PORTA, 3
	goto	b48i
	call	Anti_bounce
	goto	Mode_1
b48i
	btfsc	PORTA, 4
	goto	rez8i
	call	Anti_bounce
	goto	Mode_8

rez8i
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BCF		PORTB, RB4
	BCF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b382i
	btfsc	PORTA, 3
	goto	b482i
	call	Anti_bounce
	goto	Mode_1
b482i
	btfsc	PORTA, 4
	goto	rez82i
	call	Anti_bounce
	goto	Mode_8

rez82i
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BCF		PORTB, RB2
	BCF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b383i
	btfsc	PORTA, 3
	goto	b483i
	call	Anti_bounce
	goto	Mode_1
b483i
	btfsc	PORTA, 4
	goto	rez83i
	call	Anti_bounce
	goto	Mode_8

rez83i
	BCF		PORTB, RB0
	BCF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay

b384i
	btfsc	PORTA, 3
	goto	b484i
	call	Anti_bounce
	goto	Mode_1
b484i
	btfsc	PORTA, 4
	goto	rez84i
	call	Anti_bounce
	goto	Mode_8

rez84i
	BSF		PORTB, RB0
	BSF		PORTB, RB1
	BSF		PORTB, RB2
	BSF		PORTB, RB3	
	BSF		PORTB, RB4
	BSF		PORTB, RB5
	BSF		PORTB, RB6
	BSF		PORTB, RB7
	MOVLW	0x2				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0x8
	MOVWF	DelMl
	MOVLW	0x7A
	MOVWF	DelJr
	CALL	Delay
	GOTO	Invert_mode_8

; Задержка
Delay
	DECFSZ DelJr,1		; Уменьшаем младший байт, пока он не станет 0
	GOTO Delay
	DECFSZ DelMl,1		; Уменьшаем средний байт, пока он не станет 0
	GOTO Delay
	DECFSZ DelSr,1		; Уменьшаем старший байт, пока он не станет 0
	GOTO Delay
RETURN

Anti_bounce
	MOVLW	02h				; Загружаем задержку
	MOVWF	DelSr
	MOVLW	0Dh
	MOVWF	DelMl
	MOVLW	0FFh
	MOVWF	DelJr
	CALL	Delay
RETURN

END