PUBLIC Mode1, Mode2, Mode3, Mode4, Mode5, Mode6, Mode7, Mode8
PUBLIC Mode9, Mode10, Mode11, Mode12, MOde13, Mode14, Mode15, Mode16
EXTRN CODE (Init, T0Handler, T1Handler, SelectMode, Delay)
EXTRN DATA (ModeNumber, DelayDuration, TwentySec, ProgDelayDuration, GreenCounter, GreenDuration, PrevState3)
EXTRN BIT (AllowChangeFrame, ModeWasChanged, Direction, WasChanged) 
MAIN SEGMENT CODE
CSEG AT 0
	JMP start
CSEG AT 000BH
	CALL T0Handler
	RETI
CSEG AT 001BH
	CALL T1Handler
	RETI
USING 0
RSEG MAIN
start:
	
CALL Init

JMP Mode1

; ����� ������
CheckButtons:

	JB ModeWasChanged, NextMode
	
Mark1:

	MOV A, PrevState3
	MOV R5, P3
	XRL A, R5
		
	JB ACC.2, Mdec
		
Mark2:
	
	MOV A, PrevState3
	MOV R5, P3
	XRL A, R5
	
	JB ACC.3, Minc
	
Mark3:

	MOV A, PrevState3
	MOV R5, P3
	XRL A, R5
	
	JB ACC.4, Ddec
	
Mark4:

	MOV A, PrevState3
	MOV R5, P3
	XRL A, R5
	
	JB ACC.5, Dinc
	
  Re:	
   
RETI

NextMode:
	SETB WasChanged
	CLR ModeWasChanged
	RETI

Mdec:
	MOV A, PrevState3
	JNB ACC.2, GoNext1
	MOV PrevState3, P3
	CALL Delay
	JMP Mark2
 GoNext1:
	MOV PrevState3, P3 
	JMP ModeDecrement

Minc:
	MOV A, PrevState3
	JNB ACC.3, GoNext2
	MOV PrevState3, P3
	CALL Delay
	JMP Mark3
 GoNext2:
	MOV PrevState3, P3
	JMP ModeIncrement

Ddec:
	MOV A, PrevState3
	JNB ACC.4, GoNext3
	MOV PrevState3, P3
	CALL Delay
	JMP Mark4
 GoNext3:
	MOV PrevState3, P3
	JMP DurationDecrement

Dinc:
	MOV A, PrevState3
	JNB ACC.5, GoNext4
	MOV PrevState3, P3
	CALL Delay
	JMP Re
 GoNext4:
	MOV PrevState3, P3
	JMP DurationIncrement 

; ��������� ������ �� ������� 
ModeDecrement:
	; ���������� ��������
	MOV ProgDelayDuration, #1
	CALL Delay
 	CALL RstTmr1
 	MOV R3, ModeNumber
 	CJNE R3, #1, MdDec
 	
  	CLR P3.7
	MOV GreenDuration, #50
	MOV ProgDelayDuration, GreenDuration
	MOV GreenCounter, #4
	SETB TR0
	
 	RETI
 MdDec:
	DEC ModeNumber
	SETB WasChanged
	RETI 

; ��������� ������ �� �������	
ModeIncrement:
	; ���������� ��������
	MOV ProgDelayDuration, #1
	CALL Delay
	CALL RstTmr1
	MOV R3, ModeNumber
	CJNE R3, #16, MdInc
	
	CLR P3.7
	MOV GreenDuration, #50
	MOV ProgDelayDuration, GreenDuration
	MOV GreenCounter, #4
	SETB TR0
	 	 
	RETI
 MdInc:
	INC ModeNumber
	SETB WasChanged
	RETI

; ��������� ������� �� �������	
DurationDecrement:
	; ���������� ��������
	MOV ProgDelayDuration, #1
	CALL Delay	
	CALL RstTmr1
	MOV R3, DelayDuration
	CJNE R3, #1, DrtnDec
	
	CLR P3.7
	MOV GreenDuration, #100
	MOV ProgDelayDuration, GreenDuration
	MOV GreenCounter, #2
	SETB TR0
	
	RETI
 DrtnDec:
 	DEC DelayDuration
	MOV R3, DelayDuration
	CJNE R3, #1, Kek
	
	CLR P3.7
	MOV GreenDuration, #100
	MOV ProgDelayDuration, GreenDuration
	MOV GreenCounter, #2
	SETB TR0
	
  Kek:
RETI

; ��������� ������� �� �������	
DurationIncrement:
	; ���������� �������� 
	MOV ProgDelayDuration, #1
	CALL Delay
	
	CALL RstTmr1
	MOV R3, DelayDuration
	CJNE R3, #16, DrtnInc
	
	CLR P3.7
	MOV GreenDuration, #100
	MOV ProgDelayDuration, GreenDuration
	MOV GreenCounter, #2
	SETB TR0
	
	RETI
 DrtnInc:
	INC DelayDuration
	MOV R3, DelayDuration
	CJNE R3, #16, Lol
	
	CLR P3.7
	MOV GreenDuration, #100
	MOV ProgDelayDuration, GreenDuration
	MOV GreenCounter, #2
	SETB TR0
	
 Lol:
RETI

; ��������� 20� �������� �������		
RstTmr1:
	MOV TH1, #0D8H
	MOV TL1, #0F0H
	MOV TwentySec, #07H
	MOV TwentySec + 1, #0D0H
RETI

; ������
Mode1:
	MOV P1, #01010101B
	CLR P3.7
	MOV GreenDuration, #50
	MOV ProgDelayDuration, GreenDuration
	MOV GreenCounter, #4
	SETB TR0 	
 ChangeMode1:	
 	JB AllowChangeFrame, ChangeFrame1
 	CALL CheckButtons
 	JNB WasChanged, NoChange1 
 	JMP SelectMode
  NoChange1:
 	JMP ChangeMode1
  ChangeFrame1:
	MOV A, P1
	RR A
	MOV P1, A
	CLR AllowChangeFrame
	JMP ChangeMode1
	
Mode2:
	MOV P1, #01111111B
 ChangeMode2:
 	JB AllowChangeFrame, ChangeFrame2
 	CALL CheckButtons
 	JNB WasChanged, NoChange2 
 	JMP SelectMode
  NoChange2:
 	JMP ChangeMode2
  ChangeFrame2:
  	MOV A, P1
  	RR A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode2
  	
Mode3:
	MOV P1, #11111110B
 ChangeMode3:
 	JB AllowChangeFrame, ChangeFrame3

 	CALL CheckButtons
 	JNB WasChanged, NoChange3 
 	JMP SelectMode
  NoChange3:
 	JMP ChangeMode3
  ChangeFrame3:
  	MOV A, P1
  	RL A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode3

Mode4:
	MOV P1, #11110000B
 ChangeMode4:
 	JB AllowChangeFrame, ChangeFrame4

 	CALL CheckButtons
 	JNB WasChanged, NoChange4 
 	JMP SelectMode
  NoChange4:
 	JMP ChangeMode4
  ChangeFrame4:
  	MOV A, P1
  	SWAP A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode4

Mode5:
	MOV P1, #11110000B
 ChangeMode5:
 	JB AllowChangeFrame, ChangeFrame5

 	CALL CheckButtons
 	JNB WasChanged, NoChange5
 	JMP SelectMode
  NoChange5:
 	JMP ChangeMode5
  ChangeFrame5:
  	MOV A, P1
  	RL A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode5
		
Mode6:
	MOV P1, #00001111B
 ChangeMode6:
 	JB AllowChangeFrame, ChangeFrame6

 	CALL CheckButtons
 	JNB WasChanged, NoChange6 
 	JMP SelectMode
  NoChange6:
 	JMP ChangeMode6
  ChangeFrame6:
  	MOV A, P1
  	RR A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode6

Mode7:
	MOV P1, #00000000B
 ChangeMode7:
 	JB AllowChangeFrame, ChangeFrame7

 	CALL CheckButtons
 	JNB WasChanged, NoChange7 
 	JMP SelectMode
  NoChange7:
 	JMP ChangeMode7
  ChangeFrame7:
  	MOV A, P1
  	CPL A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode7

Mode8:
	MOV P1, #00000001B 
 ChangeMode8:
 	JB AllowChangeFrame, ChangeFrame8

 	CALL CheckButtons
 	JNB WasChanged, NoChange8 
 	JMP SelectMode
  NoChange8:
 	JMP ChangeMode8
  ChangeFrame8:
  	MOV A, P1
  	RL A
  	ADD A, #1
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode8

Mode9:
	MOV P1, #11111110B 
 ChangeMode9:
 	JB AllowChangeFrame, ChangeFrame9

 	CALL CheckButtons
 	JNB WasChanged, NoChange9 
 	JMP SelectMode
  NoChange9:
 	JMP ChangeMode9
  ChangeFrame9:
  	MOV A, P1
  	RL A
  	SUBB A, #1
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode9
  	
Mode10:
	MOV P1, #00011000B 
 ChangeMode10:
 	JB AllowChangeFrame, ChangeFrame10

 	CALL CheckButtons
 	JNB WasChanged, NoChange10 
 	JMP SelectMode
  NoChange10:
 	JMP ChangeMode10
  ChangeFrame10:
  	MOV R4, P1
  	CJNE R4, #10000001B, Nxt10
  	MOV P1, #00011000B
  	CLR AllowChangeFrame
  	JMP ChangeMode10 
  Nxt10:
  	MOV A, P1
  	ANL A, #11110000B
  	RL A
  	MOV R5, A
  	MOV A, P1
  	ANL A, #00001111B
  	RR A
  	MOV R6, A
  	MOV A, R5
  	ORL A, R6
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode10
	
Mode11:
	MOV P1, #10000001B 
 ChangeMode11:
 	JB AllowChangeFrame, ChangeFrame11

 	CALL CheckButtons
 	JNB WasChanged, NoChange11 
 	JMP SelectMode
  NoChange11:
 	JMP ChangeMode11
  ChangeFrame11:
  	MOV R4, P1
  	CJNE R4, #00011000B, Nxt11
  	MOV P1, #10000001B
  	CLR AllowChangeFrame
  	JMP ChangeMode11 
  Nxt11:
  	MOV A, P1
  	ANL A, #11110000B
  	RR A
  	MOV R5, A
  	MOV A, P1
  	ANL A, #00001111B
  	RL A
  	MOV R6, A
  	MOV A, R5
  	ORL A, R6
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode11

Mode12:
	MOV P1, #11111110B
	SETB Direction 
 ChangeMode12:
 	JB AllowChangeFrame, ChangeFrame12

 	CALL CheckButtons
 	JNB WasChanged, NoChange12 
 	JMP SelectMode
  NoChange12:
 	JMP ChangeMode12
  ChangeFrame12:
  	MOV A, P1
  	CLR C
  	SUBB A, #11111110B
  	JZ SetLeft
  	MOV A, P1
  	CLR C
  	SUBB A, #01111111B
  	JZ SetRight
  	JMP Mark12  
  SetRight:
  	SETB Direction
  	JMP Mark12
  SetLeft:
  	CLR Direction
  	JMP Mark12
  	
  
  Mark12:
  	MOV A, P1
  	JNB Direction, GoLeft12
  GoRight12: 
  	RR A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode12
  	
  GoLeft12:
  	RL A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode12

Mode13:
	MOV P1, #00000001B
	SETB Direction 
 ChangeMode13:
 	JB AllowChangeFrame, ChangeFrame13

 	CALL CheckButtons
 	JNB WasChanged, NoChange13 
 	JMP SelectMode
  NoChange13:
 	JMP ChangeMode13
  ChangeFrame13:
  	MOV A, P1
  	CLR C
  	SUBB A, #00000001B
  	JZ SetLeft13
  	MOV A, P1
  	CLR C
  	SUBB A, #10000000B
  	JZ SetRight13
  	JMP Mark13  
  SetRight13:
  	SETB Direction
  	JMP Mark13
  SetLeft13:
  	CLR Direction
  	JMP Mark13
  	
  
  Mark13:
  	MOV A, P1
  	JNB Direction, GoLeft13
  GoRight13: 
  	RR A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode13
  	
  GoLeft13:
  	RL A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode13

Mode14:
	MOV P1, #00111111B
	SETB Direction 
 ChangeMode14:
 	JB AllowChangeFrame, ChangeFrame14

 	CALL CheckButtons
 	JNB WasChanged, NoChange14 
 	JMP SelectMode
  NoChange14:
 	JMP ChangeMode14
  ChangeFrame14:
  	MOV A, P1
  	CLR C
  	SUBB A, #11111100B
  	JZ SetLeft14
  	MOV A, P1
  	CLR C
  	SUBB A, #00111111B
  	JZ SetRight14
  	JMP Mark14  
  SetRight14:
  	SETB Direction
  	JMP Mark14
  SetLeft14:
  	CLR Direction
  	JMP Mark14
  	
  
  Mark14:
  	MOV A, P1
  	JNB Direction, GoLeft14
  GoRight14: 
  	RR A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode14
  	
  GoLeft14:
  	RL A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode14

Mode15:
MOV P1, #11000000B
	SETB Direction 
 ChangeMode15:
 	JB AllowChangeFrame, ChangeFrame15

 	CALL CheckButtons
 	JNB WasChanged, NoChange15 
 	JMP SelectMode
  NoChange15:
 	JMP ChangeMode15
  ChangeFrame15:
  	MOV A, P1
  	CLR C
  	SUBB A, #00000011B
  	JZ SetLeft15
  	MOV A, P1
  	CLR C
  	SUBB A, #11000000B
  	JZ SetRight15
  	JMP Mark15  
  SetRight15:
  	SETB Direction
  	JMP Mark15
  SetLeft15:
  	CLR Direction
  	JMP Mark15
  	
  
  Mark15:
  	MOV A, P1
  	JNB Direction, GoLeft15
  GoRight15: 
  	RR A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode15
  	
  GoLeft15:
  	RL A
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode15


Mode16:
	MOV P1, #01010101B
	CLR P3.7
	MOV GreenDuration, #50
	MOV ProgDelayDuration, GreenDuration
	MOV GreenCounter, #4
	SETB TR0
 ChangeMode16:
 	JB AllowChangeFrame, ChangeFrame16
 	CALL CheckButtons
 	JNB WasChanged, NoChange16 
 	JMP SelectMode
  NoChange16:
 	JMP ChangeMode16
  ChangeFrame16:
  	MOV A, P1
  	CPL A
  	ANL A, #01010101B
  	MOV P1, A
  	CLR AllowChangeFrame
  	JMP ChangeMode16
	  

		 






























































































































































































