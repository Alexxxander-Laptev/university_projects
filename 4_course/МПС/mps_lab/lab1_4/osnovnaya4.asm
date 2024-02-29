 NAME zadanie4
EXTRN CODE 	(zaderjka)
MAIN SEGMENT CODE
CSEG AT 0
jmp start
PROG	SEGMENT	CODE
CONST	SEGMENT	CODE
STACK	SEGMENT	IDATA
RSEG  STACK
	DS    10H  ; 16 Bytes Stack
	CSEG  AT   0
	USING	0  ; Register-Bank 0BITVAR	SEGMENT	BIT
RSEG  PROG
start:
mov R1, #030h
mov R2, #020h
mov R3, #101h
call zaderjka              
jmp start
END   

