NAME vivod

PUBLIC	vivod 
vivod_ROUTINES SEGMENT CODE
RSEG vivod_ROUTINES
JMP vivod
vivod:
	JNB  TI,$		; ����, ���� �������� ���� ���������� �����������
	CLR  TI			; ������� ���� ���������� �����������
	MOV  SBUF,A		; ���������� ���� � ����� ��������
	mov A, #0 
RET
END
































































































































