; 12 ���
MAIN SEGMENT CODE
CSEG AT 0
JMP start ; 0,002 ��
USING 0
RSEG MAIN
start:
	call Delay ; 0,002 �� 
	JMP start
Delay:	
MOV R0, #69  ; 0,001 ��
MOV R1, #102 ; 0,001 ��
MOV R2, #112 ; 0,001 ��
Count0:	
	Count1: 
		Count2: 
			DJNZ R2, Count2 ; 0,002 ��   
		DJNZ R1, Count1 ; 0,002 ��
	DJNZ R0, Count0 ; 0,002 ��
	NOP	
RET ; 0,002 ��                                       
END

















