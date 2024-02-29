NAME SUBB 
USING 0					;���� ���������

BIG EQU 22H
ZADER20_H EQU 20H
ZADER20_L EQU 21H
GR_TWO 	EQU  R7
COUNT_CADR EQU R0		;������� ������ � �������
SPEED EQU R1			;������� ��������� ��������
DELAY EQU R2			;���������� ��������� ��������
NOMER_EFECTA EQU R3		;����� �������
COUNT_GREEN EQU R4		;������� ��������� ��������


;������ ��������;
F1  SEGMENT CODE    	;������������� ������������ �������� ��������� ����� � ������������ ��������
F2  SEGMENT CODE
F3  SEGMENT CODE
F4  SEGMENT CODE
F5  SEGMENT CODE
F6  SEGMENT CODE
F7  SEGMENT CODE
F8  SEGMENT CODE
F9  SEGMENT CODE
F10 SEGMENT CODE
F11 SEGMENT CODE
F12 SEGMENT CODE
F13 SEGMENT CODE
F14 SEGMENT CODE
F15 SEGMENT CODE
F16 SEGMENT CODE


PROG SEGMENT CODE		;���������� �������� ���� ���������
STACK SEGMENT IDATA		;���������� �������� �����

RSEG STACK				;�������� ��������� ������������ ������� � ������ ��� ��������
DS 16H					;��� ���� ������������� 16 ����
        ;DB ����������� ����������� ���������� ���� � ������ ��������
RSEG F1  
	DB 55H, 0AAH, 55H, 0AAH, 55H, 0AAH, 55H, 0AAH 
  			;DB ����������� ����������� ���������� ���� � ������ ��������
RSEG F2  
	DB 3FH, 0CFH, 0F3H, 0FCH, 3FH, 0CFH, 0F3H, 0FCH 
  	
RSEG F3  
	DB 0CCH, 033H, 0CCH, 033H, 0CCH, 033H, 0CCH, 033H
	
RSEG F4  
	DB 0F0H, 0FH, 0F0H, 0FH, 0F0H, 0FH, 0F0H, 0FH

RSEG F5  
	DB 7FH, 0BFH, 0DFH, 0EFH, 0F7H, 0FBH, 0FDH, 0FEH   ;�������� ������
RSEG F6  
	DB 011H, 088H, 044H, 022H, 011H, 088H, 044H, 022H 
RSEG F7   
	DB 7EH, 3CH, 18H, 00H ,7EH, 3CH, 18H, 00H , 0FFH
RSEG F8   
 	DB 07EH, 03CH, 018H, 00H, 018H,03CH, 07EH, 00H
RSEG F9
	DB 00H, 018H, 03CH, 07EH, 0FFH, 07EH,03CH, 018H
RSEG F10
	DB 00H, 080H, 0C0H, 0E0H, 0F0H, 0F8H, 0FCH, 0FEH
RSEG F11
	DB 0FEH, 0FFH, 0FCH, 0FFH, 0F8H, 0FFH, 0F0H, 0FFH
RSEG F12
	DB 07FH, 0FFH, 03FH, 0FFH, 01FH, 0FFH, 0FH, 0FFH
RSEG F13
	DB  00H, 01H, 00H, 03H,00H, 07H, 00H, 0FH, 00H
RSEG F14
	DB 00H, 0FFH,00H, 0FFH, 00H, 0FFH, 00H, 0FFH,
RSEG F15
DB 080H, 0C0H, 0E0H, 0F0H, 0F8H, 0FCH, 0FEH, 0FFH

RSEG F16
 DB 018H, 081H, 03CH, 0C3H, 018H, 081H, 03CH, 0C3H
  
  
CSEG AT 0
   LJMP go					;��� ��������� ������� ����� ��������� ����������� ������� �� ����� START

;ORG - ������������ ��� �������� ���������� ������ ������� � ������   

ORG 0BH						;����� ������� ���������� �� �\�0
   CALL EFFECT				;������� ������������, ��������� ���� ������� 
   RETI
  
ORG 1BH						;����� ������ ���������� �� �\�1	
   CALL GREENOMER_EFECTA  	;������� ������������, �������������� �������� ������� ����������
   RETI

   
   
   
   
   
RSEG PROG					;������� ���� ���������:

DELAY1:						;��������
	MOV BIG, #05
	MOV R5, #0FFH           
	MMMM1:
		MOV R6, #0FFH   
		MMMM2:
		DJNZ R6, MMMM2 
	DJNZ R5, MMMM1
	MOV R5, #0FFH
	DJNZ BIG, MMMM1
RET


GREENOMER_EFECTA:				;�������� �� �������� �������� ����������
	CLR TCON.6               
   MOV TH1, #03CH           
   MOV TL1, #0AFH
   DJNZ COUNT_GREEN, ST_GREEN   
     
	   CJNE GR_TWO, #02H, LIGHT 
		 MOV COUNT_GREEN, #5
		 DEC GR_TWO    
		 SETB P3.7
	   LJMP ST_GREEN    
	   LIGHT:  
	   CJNE GR_TWO, #01H, OUT
		 MOV COUNT_GREEN, #10
		 DEC GR_TWO  
		 CLR P3.7  
	   LJMP ST_GREEN  
	   OUT:  
	   CJNE GR_TWO, #00H, END_GREEN
		SETB P3.7                                                                                                                                                                               
		LJMP END_GREEN 
           
   ST_GREEN:                         
     SETB TCON.6                 
 END_GREEN:      
RET

SET_EFFECT:							;����� �������
     CJNE NOMER_EFECTA, #1, L1		;��������� ������������ � ��������������� ������ � �������, ���� �� �����
         MOV DPTR, #F1 -  1			;DPTR �������� ��������
L1:  CJNE NOMER_EFECTA, #2, L2      
         MOV DPTR, #F2 -  1
L2:  CJNE NOMER_EFECTA, #3, L3      
         MOV DPTR, #F3 -  1
L3:  CJNE NOMER_EFECTA, #4, L4      
         MOV DPTR, #F4 -  1
L4:  CJNE NOMER_EFECTA, #5,L5      
         MOV DPTR, #F5 -  1
L5:  CJNE NOMER_EFECTA, #6, L6      
         MOV DPTR, #F6 -  1
L6:  CJNE NOMER_EFECTA, #7, L7      
         MOV DPTR, #F7 -  1
L7:  CJNE NOMER_EFECTA, #8, L8      
         MOV DPTR, #F8 -  1
L8:  CJNE NOMER_EFECTA, #9, L9      
         MOV DPTR, #F9 -  1
L9:  CJNE NOMER_EFECTA, #10,L10      
         MOV DPTR, #F10 - 1
L10: CJNE NOMER_EFECTA, #11,L11      
         MOV DPTR, #F11 - 1
L11: CJNE NOMER_EFECTA, #12,L12      
         MOV DPTR, #F12 - 1
L12: CJNE NOMER_EFECTA, #13,L13      
         MOV DPTR, #F13 - 1
L13: CJNE NOMER_EFECTA, #14,L14      
         MOV DPTR, #F14 - 1
L14: CJNE NOMER_EFECTA, #15, L15      
         MOV DPTR, #F15 - 1
L15: CJNE NOMER_EFECTA, #16, L16   
         MOV DPTR, #F16 - 1        
L16: RET      



EFFECT:						;����� �����:
 	DJNZ ZADER20_L,SKIP
 		MOV ZADER20_L, #255
 		DJNZ ZADER20_H,SKIP
 		
 		INC NOMER_EFECTA
 		MOV ZADER20_L,#190
 		MOV ZADER20_H,#2
 		
 		CJNE NOMER_EFECTA, #17, M11   		;���� ����� ������� �� ����� 17 �� �������       
    		MOV NOMER_EFECTA, #16            
		M11:   
		   CJNE NOMER_EFECTA, #16, SKIP     
			MOV COUNT_GREEN, #10
			MOV GR_TWO, #02H
			CLR P3.7							;������ ��������� �������� ���������
			SETB TCON.6							;����������� ������ ������ 	
 	SKIP:
   CALL SET_EFFECT			;����� ������
   DJNZ DELAY, END_CADR		;��������� ������� �������� (��������� �������� � �������, ���� �� ����)
   MOV A, SPEED				;���� ������� �������� ������ ����, ����������� ��� ��������� ��������
   MOV DELAY, A
   MOV A, DPL					
   ADD A, COUNT_CADR 		;���������� � �������� ������ ������� ������� ������, �������� ����� �������� �����
   MOV DPL, A
   MOV A, DPH
   ADDC A,#0
   MOV DPH, A  
   CLR A							;����� ������������
   MOVC  A, @A+DPTR    		;! 
     MOV P1, A					;������� ����
   INC COUNT_CADR
   CJNE COUNT_CADR, #9, END_CADR     
   MOV COUNT_CADR, #1
END_CADR:
   RET 
   
   
   
go:                       ; �������� ���������:
	MOV GR_TWO, #02H
   MOV SP, #STACK-1       ; ������������� �����!
   MOV ZADER20_L, #40
   MOV ZADER20_H, #2
   MOV TMOD, #11H         ; �/�0 � �/�1 �������� � ������ 16-������ ��������
   SETB IE.7              ; ����������� ����������
   SETB IE.1              ; ����������� ���������� �� �������� �������
   SETB IE.3              ; ����������� ���������� �� ������� �������
   MOV TH0, #0H         
   MOV TL0, #0H
   SETB TCON.4          
   CLR  TCON.6          
   MOV TH1, #03CH        
   MOV TL1, #0AFH   
   MOV NOMER_EFECTA, #1         ;��������������� ����� ������� - ������
   MOV SPEED, #1         		;��������������� ���������� ��������� ��������
   MOV DELAY, #1         		;������������� ������� �������� 
   MOV COUNT_CADR,  #1   		;������������� ������� ������
   
   

KN1:                     
	JB P3.2, KN2    					;���� �� ������ ������ ������, ������ � ������ ������
	CALL DELAY1
	JNB P3.2, $							;���� �� �������� � 0 �� ������� �� ����
	MOV ZADER20_L, #40
   MOV ZADER20_H, #2
   
	DEC  NOMER_EFECTA                    
	CJNE NOMER_EFECTA, #0, M			;���� ����� ������� �� ����� ���� �� �������             
	MOV NOMER_EFECTA, #1              
	M:  
		CJNE NOMER_EFECTA, #1, KN1			;���� ����� ������� �� ����� 1 �� ������� KN1 � ������ ���������� ��� ������   
		MOV GR_TWO, #02H ;��� �������� ��������         
		MOV COUNT_GREEN, #10  
		CLR P3.7							;������ ��������� �������� ���������
		SETB TCON.6							;����������� ������ ������
         
KN2:
	JB P3.3, KN3						;���� �� ������ ������ ������, ������ � ������ �������
	CALL DELAY1
    JNB P3.3, $ 						;���� �� �������� � 0 �� ������� �� ��������� ����� 
     
   MOV ZADER20_L, #40
   MOV ZADER20_H, #2
      
	INC  NOMER_EFECTA                   
    CJNE NOMER_EFECTA, #17, M1   		;���� ����� ������� �� ����� 17 �� �������       
    MOV NOMER_EFECTA, #16            
	M1:   
		CJNE NOMER_EFECTA, #16, KN2 		;���� ����� ������� �� ����� 6 �� ������� KN2 � ������ ���������� ��� ������    
		MOV GR_TWO, #02H;��� �������� ��������     
		MOV COUNT_GREEN, #10 
		CLR P3.7							;������ ��������� �������� ���������
		SETB TCON.6							;����������� ������ ������
	  
KN3:
	JB P3.4, KN4  						
	CALL DELAY1
    JNB P3.4, $ 
    
   MOV ZADER20_L, #40
   MOV ZADER20_H, #2  
     
	DEC SPEED      
    CJNE SPEED, #0, LL   
    MOV SPEED, #1
LL:  CJNE SPEED, #1, KN3    
		MOV GR_TWO, #0;��� ���������� �������� ��������     
     MOV COUNT_GREEN, #20 
     CLR P3.7; ������ ��������� �������� ���������
     SETB TCON.6; ����������� ������ ������
        

KN4:
   JB P3.5, KN1; ���� �� ������ �������� ������, ������ � ������ ������
   CALL DELAY1
       JNB P3.5, $
       
       MOV ZADER20_L, #40
   		MOV ZADER20_H, #2
                          
       INC SPEED
       CJNE SPEED, #17, LL1    
       MOV SPEED, #16
LL1:   CJNE SPEED, #16, KN4  
		 MOV GR_TWO, #0;��� ���������� �������� ��������       
       MOV COUNT_GREEN, #20 
       CLR P3.7; ������ ��������� �������� ���������
       SETB TCON.6; ����������� ������ ������
       JMP KN1
JMP go      
END
