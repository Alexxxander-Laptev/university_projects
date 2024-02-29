NAME zadanie3
EXTRN 	CODE 	(zadanie3, Mull, Summa,Vivod)
EXTRN data (qwe,wer,ltp,addr1,addr2,addr3,rumnog1_1,rumnog1_2,rumnog1_3,rumnog1_4,rumnog1_5,rumnog1_6,rumnog1_7,rumnog1_8,rumnog1_9,rumnog1_10,rumnog1_11,rumnog1_12,umnog1_1,umnog1_2,umnog1_3,umnog1_4,vivod1,vivod2,vivod3,vivod4,vivod5,vivod6,summ1,summ2,summ3,summ4)
MAIN SEGMENT CODE
CSEG AT 0
PROG	SEGMENT	CODE
CONST	SEGMENT	CODE
STACK	SEGMENT	IDATA
RSEG  STACK
	DS    10H 
	CSEG  AT   0
	USING	0  
JMP start
;RSEG  PROG
start:
; Загружаем данные из внешней памяти
MOV DPTR, #addr1
	MOVX A, @DPTR	
	MOV R1, A			
	MOV DPTR, #addr2	
	MOVX A, @DPTR
	MOV R2, A	
	MOV DPTR, #addr3
	MOVX A, @DPTR
	MOV R3, A	
; Получаем 3 байта из порта 2, от старшего к младшему
	MOV R5, P2
	MOV R6, P2
	MOV R7, P2
; Переносим  младший байт второго числа в регистры
	MOV B, R7
	MOV R4, B
	CALL Mull
	;переносим результат из временных ячеек
   MOV R0, #umnog1_1
	MOV A, @R0
	MOV R0, #rumnog1_1
	MOV @R0, A
	MOV R0, #umnog1_2
	MOV A, @R0
	MOV R0, #rumnog1_2
	MOV @R0, A
	MOV R0, #umnog1_3
	MOV A, @R0
	MOV R0, #rumnog1_3
	MOV @R0, A
	MOV R0, #umnog1_4
	MOV A, @R0
	MOV R0, #rumnog1_4
	MOV @R0, A
	; Переносим  средний байт второго числа в регистры
	MOV B, R6
	MOV R4, B
	CALL Mull				;вызываем подпрограмму умножения
	;переносим результат из временных ячеек
	MOV R0, #umnog1_1
	MOV A, @R0
	MOV R0, #rumnog1_5
	MOV @R0, A
	MOV R0, #umnog1_2
	MOV A, @R0
	MOV R0, #rumnog1_6
	MOV @R0, A
	MOV R0, #umnog1_3
	MOV A, @R0
	MOV R0, #rumnog1_7
	MOV @R0, A
	MOV R0, #umnog1_4
	MOV A, @R0
	MOV R0, #rumnog1_8
	MOV @R0, A
	; Переносим  старший  байт второго числа в регистры
	MOV B, R5
	MOV R4, B
	CALL Mull	;вызываем подпрограмму умножения
	;переносим результат из временных ячеек
	MOV R0, #umnog1_1
	MOV A, @R0
	MOV R0, #rumnog1_9
	MOV @R0, A
	MOV R0, #umnog1_2
	MOV A, @R0
	MOV R0, #rumnog1_10
	MOV @R0, A
	MOV R0, #umnog1_3
	MOV A, @R0
	MOV R0, #rumnog1_11
	MOV @R0, A
	MOV R0, #umnog1_4
	MOV A, @R0
	MOV R0, #rumnog1_12
	MOV @R0, A
	;записываем результат первого и второго умножения в регистры
	MOV R0, #rumnog1_3
   MOV A, @R0
   MOV R1, A
   MOV R0, #rumnog1_2
   MOV A, @R0
   MOV R3, A
   MOV R0, #rumnog1_1
   MOV A, @R0
   MOV R5, A
   MOV R0, #rumnog1_8
   MOV A, @R0
   MOV R2, A
   MOV R0, #rumnog1_7
   MOV A, @R0
   MOV R4, A
   MOV R0, #rumnog1_6
   MOV A, @R0
   MOV R6, A
   MOV R0, #rumnog1_5
   MOV A, @R0
   MOV R7, A
;записываем младший байт конечного результата
   MOV R0, #rumnog1_4
   MOV A, @R0
   MOV R0, #vivod1
   MOV @R0, A
   CALL Summa;вызываем подпрограмму сложения
;записываем следующий байт конечного результата
   MOV R0, #summ1
   MOV A, @R0
   MOV R0, #vivod2
   MOV @R0, A	
;записываем результат суммирования и третьего умножения в регистры
MOV R0, #rumnog1_12
   MOV A, @R0
   MOV R1, A
   MOV R0, #rumnog1_11
   MOV A, @R0
   MOV R3, A
   MOV R0, #rumnog1_10
   MOV A, @R0
   MOV R5, A

   MOV R0, #rumnog1_9 
   MOV A, @R0
   MOV R7, A  
   MOV R0, #summ2
   MOV A, @R0
   MOV R2, A    
   MOV R0, #summ3
   MOV A, @R0
   MOV R4, A
   MOV R0, #summ4
   MOV A, @R0
   MOV R6, A	
	CALL Summa;вызываем подпрограмму сложения
   ;записываем байты конечного результата	
   MOV R0, #summ4
   MOV A, @R0
   MOV R0, #vivod6
   MOV @R0, A
   MOV R0, #summ3
   MOV A, @R0
   MOV R0, #vivod5
   MOV @R0, A
   MOV R0, #summ2
   MOV A, @R0
   MOV R0, #vivod4
   MOV @R0, A
   MOV R0, #summ1
   MOV A, @R0
   MOV R0, #vivod3 
   MOV @R0, A
    ; Включаем UART
 ; Используем TIMER 1 для генерации опорной частоты
   MOV   TMOD,#00100000B		;C/T = 0, Mode = 3 режим таймера с автоперезагрузкой
	MOV   TH1, #0F8H; перегружаемое число
	SETB  TR1;разрешаем таймер
	MOV  PCON, #01011100B;SMOD=1	
	MOV   SCON,#01010010B;Режим 9-разрядной посылки
	;последовательно начиная со старшего байта выводим результат
	MOV R0, #vivod6
    MOV A, @R0	
	CALL Vivod	
	MOV R0, #vivod5                             	
    MOV A, @R0
	CALL Vivod	
	MOV R0, #vivod4
    MOV A, @R0
	CALL Vivod	
	MOV R0, #vivod3
    MOV A, @R0
	CALL Vivod	
	MOV R0, #vivod2
    MOV A, @R0
	CALL Vivod	
	MOV R0, #vivod1
    MOV A, @R0
	CALL Vivod 	
	JMP start	
END
































