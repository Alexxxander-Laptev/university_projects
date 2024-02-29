NAME PEREMENNAYA
PUBLIC qwe,wer, rty, uio,summ1,summ2,summ3,summ4,addr1,addr2,addr3,rumnog1_1,rumnog1_2,rumnog1_3,rumnog1_4,rumnog1_5,rumnog1_6,rumnog1_7,rumnog1_8,rumnog1_9,rumnog1_10,rumnog1_11,rumnog1_12, umnog1_1,umnog1_2,umnog1_3,umnog1_4,vivod1,vivod2,vivod3,vivod4,vivod5,vivod6
BITVAR	SEGMENT	data
RSEG  BITVAR
;адреса внешней пам€ти
addr1 equ 0000h
addr2 equ addr1+1
addr3 equ addr2+1
; временные значени€ умножени€
qwe equ 01fh  
wer equ 01eh
rty equ 01dh
uio equ 01ch  
; временные значени€ суммы
summ1 equ 056h
summ2 equ 055h
summ3 equ 054h
summ4 equ 053h
;временное хранение результата умножени€  младших байтов
rumnog1_1 equ 034h 
rumnog1_2 equ rumnog1_1+1	 ;035
rumnog1_3 equ rumnog1_2+1   ;036
rumnog1_4 equ rumnog1_3+1	 ;037
;временное хранение результата умножени€  средних байтов
rumnog1_5 equ 03Bh 
rumnog1_6 equ rumnog1_5+1    ;03c
rumnog1_7 equ rumnog1_6+1    ;03d
rumnog1_8 equ rumnog1_7+1    ;03e
;временное хранение результата умножени€  старших байтов
rumnog1_9 equ 042h 
rumnog1_10 equ rumnog1_9+1   		;043
rumnog1_11 equ rumnog1_10+1     	;044
rumnog1_12 equ rumnog1_11+1      ;045
;считывание результатов умножени€ байтов
umnog1_1 equ 01CH  
umnog1_2 equ umnog1_1+1      	   ;01d
umnog1_3 equ umnog1_2+1          ;01e
umnog1_4 equ umnog1_3+1          ;01f
;¬ывод                                         
vivod1 equ 04Fh
vivod2 equ 04Eh 
vivod3 equ 04Dh 
vivod4 equ 04Ch  
vivod5 equ 04Bh 
vivod6 equ 04Ah                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
END 
















































































































































