; используем процессор PIC16F84, система исчисления десятичная
include "p16f84.inc" ; подключаем файл с описанием регистров
address_data	EQU 24h
address_EE		EQU 25h
it				EQU 23h

DelimoeH		EQU 010h
DelimoeL		EQU 011h
DelitelH		EQU 020h
DelitelL 		EQU 021h
ChastnoeH		EQU 014h
ChastnoeL		EQU 013h

; Устанавливаем вектор сброса
ORG 		0
GOTO 		Start

Start:
BCF 		STATUS, RP1
BSF 		STATUS, RP0 ; Выбираем банк памяти 1
MOVLW		B'11111111' ; Настраиваем порт В как вход
MOVWF 		TRISB

; берем 2 байтовое число из порта B
BCF 		STATUS, RP0 ; Выбираем банк памяти 0
MOVF 		PORTB, 0
MOVWF 		DelitelH
MOVF 		PORTB, 0
MOVWF 		DelitelL

; берем второе число из EEPROM
BCF    STATUS, RP0    ; Bank 0
MOVLW  10h
MOVWF  EEADR          ; Address to read
BSF    STATUS, RP0    ; Bank 1
BSF    EECON1, RD     ; EE Read
BCF    STATUS, RP0    ; Bank 0
MOVF		EEDATA, 0
MOVWF		DelimoeH

BCF    STATUS, RP0    ; Bank 0
MOVLW  11h
MOVWF  EEADR          ; Address to read
BSF    STATUS, RP0    ; Bank 1
BSF    EECON1, RD     ; EE Read
BCF    STATUS, RP0    ; Bank 0
MOVF		EEDATA, 0
MOVWF		DelimoeL

GOTO 		Delenie

Delenie
	CLRF	ChastnoeH	; Обнуляем частное и остаток
	CLRF	ChastnoeL
Cycle	; Циклически отнимаем делитель из делимого
	MOVF	DelitelH,0	; Читаем значение делителя в W
	SUBWF	DelimoeH,1	; Вычитаем делитель из делимого, результат НЕ в W
	BTFSS	STATUS, C	; Если при вычитании мы не занимали, то пропускаем обработку старшего регистра
	GOTO	EndDiv

	MOVF	DelitelL,0	; Читаем значение делителя в W
	SUBWF	DelimoeL,1	; Вычитаем делитель из делимого, результат НЕ в W
	BTFSS	STATUS, C	; Если при вычитании мы не занимали, то пропускаем обработку старшего регистра
	GOTO	CheckHighByte	; Иначе переходим на обработку старшего байта
	RetCycle			; Метка возврата из CheckHighByte

	;GOTO	CheckBufferByte	; Иначе переходим на обработку старшего байта
	;ReturnCycle

	INCF	ChastnoeL,1	; Увеличиваем частное
	BTFSC	STATUS, Z   ; Если при увеличении произошло переполнение, то...
	INCF	ChastnoeH,1	; ...увеличиваем старший байт частного
GOTO Cycle	; Повторяем до посинения
CheckHighByte	; Проверка старшего байта
	MOVF	DelimoeH,1	; Проверяем, не является ли старший байт нулем
	BTFSC	STATUS, Z   ; Если старший байт - не ноль, то пропускаем переход
	GOTO	EndDiv		; Если старший байт - ноль (неоткуда занимать), то переходим в конец
	DECF	DelimoeH,1	; Уменьшаем старший байт делимого
GOTO RetCycle	; Возвращаемся обратно			
;CheckBufferByte:
;	MOVF	Buffer,1	; Проверяем, не является ли старший байт нулем
;	BTFSC	STATUS, Z   ; Если старший байт - не ноль, то пропускаем переход
;	GOTO	EndDiv		; Если старший байт - ноль (неоткуда занимать), то переходим в конец
;GOTO ReturnCycle	; Возвращаемся обратно			
EndDiv	; Действие, если мы проскакали 0 (отняли лишнего) (деление закончено)
	MOVF	DelitelL, 0	; Читаем значение делителя в W
	ADDWF	DelimoeL, 1	; Возвращаем лишнее отнятое, это будет остатком
	MOVF	DelitelH, 0
	;ADDLW	1
	ADDWF	DelimoeH, 1
	
Endless:
;Выводим результат 
MOVLW 		h'2'
MOVWF 		it
MOVLW 		h'11'
MOVWF 		address_EE
MOVLW 		h'13'
MOVWF 		address_data

Mark:
MOVF 		address_data, 0
MOVWF 		FSR
MOVF 		INDF, 0
MOVWF 		EEDATA
MOVF 		address_EE, 0
MOVWF 		EEADR
BCF 		STATUS, RP1 ; Выбираем банк памяти 1
BSF 		STATUS, RP0
bsf 		EECON1, 2
movlw 		h'55'
movwf 		EECON2
movlw 		h'AA'
movwf 		EECON2
bsf 		EECON1, WR ; установить WR бит, начать запись

Viv:
BTFSS 		EECON1, EEIF
GOTO 		Viv
BCF 		EECON1, EEIF
BCF 		STATUS, RP0 ; Выбираем банк памяти 0
INCF 		address_EE
INCF 		address_data
DECFSZ 		it, 1
GOTO 		Mark
END