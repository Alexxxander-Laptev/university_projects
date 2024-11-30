PUBLIC T0Handler, T1Handler
EXTRN DATA (ModeNumber, DelayDuration, TwentySec, ProgDelayDuration, GreenCounter, GreenDuration, Temp)
EXTRN BIT (AllowChangeFrame, ModeWasChanged)
IntHndlrs SEGMENT CODE

RSEG IntHndlrs

T0Handler:
	MOV Temp, A
	DJNZ ProgDelayDuration, ResetTimer0
	DEC GreenCounter
	MOV A, GreenCounter
	JZ StopTimer0
	CPL P3.7
	MOV ProgDelayDuration, GreenDuration
 ResetTimer0:
 	MOV TH0, #0D8H
	MOV TL0, #0F0H
	MOV A, Temp
RETI
 StopTimer0:
 	CLR TR0
 	MOV A, Temp		
RETI

T1Handler:
	MOV Temp, A
	DJNZ R0, Next
	SETB AllowChangeFrame ; Установка фалга разрешения смены кадра 
	MOV A, DelayDuration
	MOV B, #10
	MUL AB
	MOV R0, A
 Next:
	CLR C
	MOV A, TwentySec + 1
	SUBB A, #1
	MOV TwentySec + 1, A
	MOV A, TwentySec
	SUBB A, #0
	MOV TwentySec, A
	MOV R1, TwentySec + 1
	MOV R2, TwentySec 
	CJNE R1, #0, ResetTimer1
	CJNE R2, #0, ResetTimer1
	
	MOV R1, ModeNumber
	CJNE R1, #16, ModInc
	MOV ModeNumber, #1
	SETB ModeWasChanged
	JMP ResetT1
  ModInc:
  	INC ModeNumber
  	SETB ModeWasChanged
  	
 ResetT1:
	MOV TwentySec, #0BH
	MOV TwentySec + 1, #0B8H
 ResetTimer1:
 	MOV TH1, #0D8H
	MOV TL1, #0F0H
	MOV A, Temp
RETI		
	  	
 	 	 
	
	

	


























































































































































































































