NAME LAB1_5    
EXTRN CODE (zaderjka)
MAIN SEGMENT CODE
CSEG AT 0
CALL start
CSEG AT 0010H
JMP obrabotchik
USING 0
; Основная программа
RSEG MAIN
start:
CALL zaderjka 		; Вызов подпрограммы запуска таймера
osnProg: 			;Выполнение основной программы во время задержки
CJNE A , #00h, loop1
JMP osnProg
loop1:
JMP start
obrabotchik:
	DJNZ R3, resetTimer	; Уменьшаем счетчик, пока он не станет нулем	
				; Если счетчик стал нулем, то отключаем таймер
	CLR TR1		; Останавливаем таймер
	CLR IE.7	 	  ; Запрещаем прерывания
	CLR ET1		; Запрещаем прерывание от Timer 01
	CLR PT1		; Убираем наивысший приоритет прерывания от Timer 
	mov a, #05h	
	resetTimer:
RETI			; Возврат из прерывания
END

























































