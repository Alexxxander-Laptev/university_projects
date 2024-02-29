NAME zaderjka
PUBLIC	zaderjka
zaderjka SEGMENT CODE
RSEG zaderjka
	MOV R3,  #05FH 
	MOV TH0, #064H
	MOV TL0, #0FFH				; Устанавливаем время по формуле.
	SETB IE.7					; Разрешаем прерывания
	SETB ET0					; Разрешаем прерывание от Timer 0
	SETB PT0		; Ставим прерыванию от Timer 0 наивысший приоритет
	MOV TMOD, #00000001B		; Timer 0: режим 1 (16-битный таймер)
	SETB TR0						; Запускаем таймер
RET
END



