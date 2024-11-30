PUBLIC Init

Ini SEGMENT CODE 

RSEG Ini

Init:
	; Инициализация внешних прерываний
	SETB IE.7
	
	SETB IE.0
	SETB IE.2
	SETB IT0
	SETB IT1
	
	MOV TH0, #0FFH
	MOV TL0, #0FFH
	MOV TH1, #0FFH
	MOV TL1, #0FFH
	SETB ET0 ; Разрешаем прерывание от Timer 0
   SETB ET1
   MOV TMOD, #01010101B
   SETB TR0 ; Запускаем счетчик
   SETB TR1
RET
END


























































































































