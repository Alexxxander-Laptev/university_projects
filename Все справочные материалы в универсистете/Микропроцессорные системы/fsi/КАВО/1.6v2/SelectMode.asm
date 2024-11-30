PUBLIC SelectMode
EXTRN CODE (Mode1, Mode2, Mode3, Mode4, Mode5, Mode6, Mode7, Mode8, Delay)
EXTRN CODE (Mode9, Mode10, Mode11, Mode12, MOde13, Mode14, Mode15, Mode16)
EXTRN DATA (ModeNumber, DelayDuration)
EXTRN BIT (WasChanged)
SlctMd SEGMENT CODE

RSEG SlctMd

; Определение выбранного режима 	
 SelectMode:
 
  IsItMode1:	
  	MOV R4, modeNumber
  	CJNE R4, #1, IsItMode2
  	CLR WasChanged
  	JMP Mode1
	
  IsItMode2:	
  	MOV R4, modeNumber
  	CJNE R4, #2, IsItMode3
  	CLR WasChanged
  	JMP Mode2
  	
  IsItMode3:	
  	MOV R4, modeNumber
  	CJNE R4, #3, IsItMode4
  	CLR WasChanged
  	JMP Mode3
  	
  IsItMode4:	
  	MOV R4, modeNumber
  	CJNE R4, #4, IsItMode5
  	CLR WasChanged
  	JMP Mode4
  	
  IsItMode5:	
  	MOV R4, modeNumber
  	CJNE R4, #5, IsItMode6
  	CLR WasChanged
  	JMP Mode5
	
  IsItMode6:	
  	MOV R4, modeNumber
  	CJNE R4, #6, IsItMode7
  	CLR WasChanged
  	JMP Mode6
  	
  IsItMode7:	
  	MOV R4, modeNumber
  	CJNE R4, #7, IsItMode8
  	CLR WasChanged
  	JMP Mode7
  	
  IsItMode8:	
  	MOV R4, modeNumber
  	CJNE R4, #8, IsItMode9
  	CLR WasChanged
  	JMP Mode8
  	
  IsItMode9:	
  	MOV R4, modeNumber
  	CJNE R4, #9, IsItMode10
  	CLR WasChanged
  	JMP Mode9
	
  IsItMode10:	
  	MOV R4, modeNumber
  	CJNE R4, #10, IsItMode11
  	CLR WasChanged
  	JMP Mode10
  	
  IsItMode11:	
  	MOV R4, modeNumber
  	CJNE R4, #11, IsItMode12
  	CLR WasChanged
  	JMP Mode11
  	
  IsItMode12:	
  	MOV R4, modeNumber
  	CJNE R4, #12, IsItMode13
  	CLR WasChanged
  	JMP Mode12
  	
  IsItMode13:	
  	MOV R4, modeNumber
  	CJNE R4, #13, IsItMode14
  	CLR WasChanged
  	JMP Mode13
	
  IsItMode14:	
  	MOV R4, modeNumber
  	CJNE R4, #14, IsItMode15
  	CLR WasChanged
  	JMP Mode14
  	
  IsItMode15:	
  	MOV R4, modeNumber
  	CJNE R4, #15, IsItMode16
  	CLR WasChanged
  	JMP Mode15
  	
  IsItMode16:
  	CLR WasChanged
  	JMP Mode16	
  	   	  	



















   
 Exit:
END  


























































































































































































































