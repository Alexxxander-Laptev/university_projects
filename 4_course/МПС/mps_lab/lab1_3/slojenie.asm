NAME Summa
EXTRN	data   (summ1,summ2,summ3,summ4)
PUBLIC	Summa
SUM_ROUTINES SEGMENT CODE
RSEG SUM_ROUTINES
JMP Summa
Summa:
	;складываем младшие байты
	MOV A, R1
	ADD A, R2
	MOV R0, #summ1
	MOV @R0, A
	;складываем средние байты
	MOV A, R3
	ADDC A, R4
	MOV R0, #summ2
	MOV @R0, A
  	;складываем следующий байт	
	MOV A, R5
	ADDC A, R6
	MOV R0, #summ3
	MOV @R0, A
  ;складываем старший байт второго числа с переносом от предыдущего сложения
	MOV A, R7
	ADDC A, #0
	MOV R0, #summ4
	MOV @R0, A
RET
END 




























































































































































































































