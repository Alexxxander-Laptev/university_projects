NAME zaderjka
PUBLIC	zaderjka
zaderjka SEGMENT CODE
RSEG zaderjka
	MOV R3,  #05FH 
	MOV TH0, #064H
	MOV TL0, #0FFH				; ������������� ����� �� �������.
	SETB IE.7					; ��������� ����������
	SETB ET0					; ��������� ���������� �� Timer 0
	SETB PT0		; ������ ���������� �� Timer 0 ��������� ���������
	MOV TMOD, #00000001B		; Timer 0: ����� 1 (16-������ ������)
	SETB TR0						; ��������� ������
RET
END



