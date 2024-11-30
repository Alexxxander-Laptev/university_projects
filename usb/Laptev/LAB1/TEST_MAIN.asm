NAME LAB1_5    
EXTRN CODE (zaderjka)
MAIN SEGMENT CODE
CSEG AT 1
CALL start
CSEG AT 001bH
JMP obrabotchik
USING 1

RSEG MAIN
start:
CALL zaderjka 		
osnProg: 			
CJNE A , #00h, loop1
JMP osnProg
loop1:
JMP start
obrabotchik:
	DJNZ R3, resetTimer	
	CLR TR1		
	CLR IE.7	 	  
	CLR ET1		
	CLR PT1		
	mov a, #05h	
	resetTimer:
RETI			
END 


