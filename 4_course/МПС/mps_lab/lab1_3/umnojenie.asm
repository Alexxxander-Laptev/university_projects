NAME Mull
PUBLIC  Mull
EXTRN data (wer,rty,uio,qwe) 
BITVAR	SEGMENT	data
RSEG  BITVAR
Mull_ROUTINES SEGMENT CODE
RSEG Mull_ROUTINES
JMP Mull
Mull:
;�������� ������� ���� ������� ����� �� ���� ������� � ���������� ��������� �� ��������� ������ 
	MOV A, R3
	MUL AB
	MOV R0, #qwe
	MOV @R0, A
	MOV A, B
	MOV R0, A
;�������� ������� ���� ������� ����� �� ���� ������� � ���������� ��������� �� ��������� ������	
	MOV A, R2
	MOV B, R4
	MUL AB
	ADD A, R0
	MOV R0, #wer
	MOV @R0, A
	MOV A, B
	ADDC A, #0
	MOV R0, A
;�������� ������� ���� ������� ����� �� ���� ������� � ���������� ��������� �� ��������� ������	
	MOV A, R1
	MOV B, R4
	MUL AB
	ADDC A, R0
	MOV R0, #rty
	MOV @R0, A
	MOV A, B
	ADDC A, #0
	MOV R0, #uio
	MOV @R0, A
RET
end























































































































































































































