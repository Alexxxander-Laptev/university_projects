MAIN SEGMENT CODE 
CSEG AT 0
JMP start
USING 0
RSEG MAIN
start:
	MOV DPTR, #0030h ; ������� � DPTR ����� ������ ������� ������
	MOVX A, @DPTR ; ������� � ����������� �������� �� ������ ������� ������
	CLR C ; ���������� ���� �������� 
	SUBB A, #5 ; �������� 5 �� ������������ 
	MOV R0, #21h ; ������� � ������� R0 ����� 21h 
	MOV @R0, A ; ������� � ������ �� ������ 21h ���������� ������������
	CLR A ; ���������� �����������
	SUBB A, #0 ; �������� �� ������������ ���� �������� 
	DEC R0 ; ��������� �������� R0, ��� ����������� ������ � ���������� ������ 
	MOV @R0, A ; ������� �������� ������������ � ���������� ������ ������
	JMP start
END
	 






