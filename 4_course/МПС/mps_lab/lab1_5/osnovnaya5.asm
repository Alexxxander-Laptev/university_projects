NAME LAB1_5    
EXTRN CODE (zaderjka)
MAIN SEGMENT CODE
CSEG AT 0
CALL start
CSEG AT 0010H
JMP obrabotchik
USING 0
; �������� ���������
RSEG MAIN
start:
CALL zaderjka 		; ����� ������������ ������� �������
osnProg: 			;���������� �������� ��������� �� ����� ��������
CJNE A , #00h, loop1
JMP osnProg
loop1:
JMP start
obrabotchik:
	DJNZ R3, resetTimer	; ��������� �������, ���� �� �� ������ �����	
				; ���� ������� ���� �����, �� ��������� ������
	CLR TR1		; ������������� ������
	CLR IE.7	 	  ; ��������� ����������
	CLR ET1		; ��������� ���������� �� Timer 01
	CLR PT1		; ������� ��������� ��������� ���������� �� Timer 
	mov a, #05h	
	resetTimer:
RETI			; ������� �� ����������
END

























































