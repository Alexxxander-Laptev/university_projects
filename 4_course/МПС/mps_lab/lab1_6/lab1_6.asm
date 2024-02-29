NAME SUBB 
USING 0					;банк регистров

BIG EQU 22H
ZADER20_H EQU 20H
ZADER20_L EQU 21H
GR_TWO 	EQU  R7
COUNT_CADR EQU R0		;счётчик кадров в эффекте
SPEED EQU R1			;счётчик временных задержек
DELAY EQU R2			;количество временных задержек
NOMER_EFECTA EQU R3		;номер эффекта
COUNT_GREEN EQU R4		;счётчик временных задержек


;эфекты гирлядны;
F1  SEGMENT CODE    	;декларировать перемещаемые сегменты различных типов в пространстве программ
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


PROG SEGMENT CODE		;объявление сегмента кода программы
STACK SEGMENT IDATA		;объявление сегмента стека

RSEG STACK				;выбирает описанный перемещаемый сегмент и делает его активным
DS 16H					;под стек резервируется 16 байт
        ;DB резервирует необходимое количество байт в памяти программ
RSEG F1  
	DB 55H, 0AAH, 55H, 0AAH, 55H, 0AAH, 55H, 0AAH 
  			;DB резервирует необходимое количество байт в памяти программ
RSEG F2  
	DB 3FH, 0CFH, 0F3H, 0FCH, 3FH, 0CFH, 0F3H, 0FCH 
  	
RSEG F3  
	DB 0CCH, 033H, 0CCH, 033H, 0CCH, 033H, 0CCH, 033H
	
RSEG F4  
	DB 0F0H, 0FH, 0F0H, 0FH, 0F0H, 0FH, 0F0H, 0FH

RSEG F5  
	DB 7FH, 0BFH, 0DFH, 0EFH, 0F7H, 0FBH, 0FDH, 0FEH   ;мергание одного
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
   LJMP go					;при включении питания будет произведён безусловный переход на метку START

;ORG - используется для указания ассемблеру адреса объекта в памяти   

ORG 0BH						;адрес вектора прерываний от Т\С0
   CALL EFFECT				;вызвать подпрограмму, выводящую кадр эффекта 
   RETI
  
ORG 1BH						;адрес ветора прерываний от Т\С1	
   CALL GREENOMER_EFECTA  	;вызвать подпрограмму, обрабатывающую свечение зелёного светодиода
   RETI

   
   
   
   
   
RSEG PROG					;сегмент кода программы:

DELAY1:						;ЗАДЕРЖКА
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


GREENOMER_EFECTA:				;задержка на свечение зеленого светодиода
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

SET_EFFECT:							;ВЫБОР ЭФФЕКТА
     CJNE NOMER_EFECTA, #1, L1		;Сравнение аккумулятора с прямоадресуемым байтом и переход, если не равно
         MOV DPTR, #F1 -  1			;DPTR адресные регистры
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



EFFECT:						;вывод кадра:
 	DJNZ ZADER20_L,SKIP
 		MOV ZADER20_L, #255
 		DJNZ ZADER20_H,SKIP
 		
 		INC NOMER_EFECTA
 		MOV ZADER20_L,#190
 		MOV ZADER20_H,#2
 		
 		CJNE NOMER_EFECTA, #17, M11   		;если номер эффекта не равен 17 то переход       
    		MOV NOMER_EFECTA, #16            
		M11:   
		   CJNE NOMER_EFECTA, #16, SKIP     
			MOV COUNT_GREEN, #10
			MOV GR_TWO, #02H
			CLR P3.7							;зелёный светодиод начинает светиться
			SETB TCON.6							;запускается первый таймер 	
 	SKIP:
   CALL SET_EFFECT			;вызов эфекта
   DJNZ DELAY, END_CADR		;уменьшаем счётчик задержек (Декремент регистра и переход, если не нуль)
   MOV A, SPEED				;если счётчик задержек достиг нуля, присваиваем ему начальное значение
   MOV DELAY, A
   MOV A, DPL					
   ADD A, COUNT_CADR 		;прибавляем к базовому адресу эффекта счётчик кадров, получаем адрес текущего кадра
   MOV DPL, A
   MOV A, DPH
   ADDC A,#0
   MOV DPH, A  
   CLR A							;Сброс аккумулятора
   MOVC  A, @A+DPTR    		;! 
     MOV P1, A					;выводим кадр
   INC COUNT_CADR
   CJNE COUNT_CADR, #9, END_CADR     
   MOV COUNT_CADR, #1
END_CADR:
   RET 
   
   
   
go:                       ; основная программа:
	MOV GR_TWO, #02H
   MOV SP, #STACK-1       ; инициализация стека!
   MOV ZADER20_L, #40
   MOV ZADER20_H, #2
   MOV TMOD, #11H         ; Т/С0 и Т/С1 работают в режиме 16-битных таймеров
   SETB IE.7              ; разрешаются прерывания
   SETB IE.1              ; разрешается прерывание от нулевого таймера
   SETB IE.3              ; разрешается прерывание от первого таймера
   MOV TH0, #0H         
   MOV TL0, #0H
   SETB TCON.4          
   CLR  TCON.6          
   MOV TH1, #03CH        
   MOV TL1, #0AFH   
   MOV NOMER_EFECTA, #1         ;устанавливается номер эффекта - первый
   MOV SPEED, #1         		;устанавливается количество временных задержек
   MOV DELAY, #1         		;устанавливаем счётчик задержек 
   MOV COUNT_CADR,  #1   		;устанавливаем счётчик кадров
   
   

KN1:                     
	JB P3.2, KN2    					;если не нажата первая кнопка, перйти к опросу второй
	CALL DELAY1
	JNB P3.2, $							;если не подтянут к 0 то переход на СЕБЯ
	MOV ZADER20_L, #40
   MOV ZADER20_H, #2
   
	DEC  NOMER_EFECTA                    
	CJNE NOMER_EFECTA, #0, M			;если номер эффекта не равен нулю то переход             
	MOV NOMER_EFECTA, #1              
	M:  
		CJNE NOMER_EFECTA, #1, KN1			;если номер эффекта не равен 1 то переход KN1 и дальше опрашиваем все кнопки   
		MOV GR_TWO, #02H ;для двойного мерцания         
		MOV COUNT_GREEN, #10  
		CLR P3.7							;зелёный светодиод начинает светиться
		SETB TCON.6							;запускается первый таймер
         
KN2:
	JB P3.3, KN3						;если не нажата вторая кнопка, перйти к опросу третьей
	CALL DELAY1
    JNB P3.3, $ 						;если не подтянут к 0 то переход на последнюю метку 
     
   MOV ZADER20_L, #40
   MOV ZADER20_H, #2
      
	INC  NOMER_EFECTA                   
    CJNE NOMER_EFECTA, #17, M1   		;если номер эффекта не равен 17 то переход       
    MOV NOMER_EFECTA, #16            
	M1:   
		CJNE NOMER_EFECTA, #16, KN2 		;если номер эффекта не равен 6 то переход KN2 и дальше опрашиваем все кнопки    
		MOV GR_TWO, #02H;для двойного мерцания     
		MOV COUNT_GREEN, #10 
		CLR P3.7							;зелёный светодиод начинает светиться
		SETB TCON.6							;запускается первый таймер
	  
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
		MOV GR_TWO, #0;для отключения двойного мерцания     
     MOV COUNT_GREEN, #20 
     CLR P3.7; зелёный светодиод начинает светиться
     SETB TCON.6; запускается первый таймер
        

KN4:
   JB P3.5, KN1; если не нажата четвёртая кнопка, перйти к опросу первой
   CALL DELAY1
       JNB P3.5, $
       
       MOV ZADER20_L, #40
   		MOV ZADER20_H, #2
                          
       INC SPEED
       CJNE SPEED, #17, LL1    
       MOV SPEED, #16
LL1:   CJNE SPEED, #16, KN4  
		 MOV GR_TWO, #0;для отключения двойного мерцания       
       MOV COUNT_GREEN, #20 
       CLR P3.7; зелёный светодиод начинает светиться
       SETB TCON.6; запускается первый таймер
       JMP KN1
JMP go      
END
