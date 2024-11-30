include "p16f84.inc" ; ���������� ���� � ��������� ���������
; ����������
Schet	EQU 10h	; ������� �������
ZMl  	EQU 11h	; ������� ���� ��������
ZSr 	EQU 12h	; ������� ���� ��������
ZSt	    EQU 13h	; ������� ���� ��������
Naj		EQU 14h	; ���������� �� ������
Star	EQU 15h	; ����� ������
ORG 0		; ������������� ������ ������
	GOTO Start
ORG 0004h   ; ������� �� ���������� �� �������
	GOTO Timer
; �������� ���������
Start
	BCF		STATUS, RP1
	BSF 	STATUS, RP0		; �������� ���� ������ 1
	MOVLW	B'00011111'		; ����� ����� �: 4-0 �����
	MOVWF	TRISA			; ������� ������������ ����� �
	MOVLW 	B'00000000'		; ����� ����� �: 7-0 ������
	MOVWF	TRISB			; ������� ������������ ����� �
	;����������� ������
	MOVLW	B'00000111'		
	MOVWF	OPTION_REG
	BCF  	 STATUS, RP0    ; �������� ���� ������ 0
	MOVLW	B'10100000'		;��������� ����������	
	MOVWF	INTCON
	MOVLW	 h'0' 			;���������� �������� � TMR0
	MOVWF	TMR0 			;��������� ������
	BCF		STATUS, RP0		; �������� ���� ������ 0
	CLRF	Star			; �������� ����� ������
	MOVLW 1
	MOVWF	Schet			; ������� 1 � �������
	MOVF	Schet, 0
	MOVWF	PORTB			; ������� ��� ��������
	;0 - ������ ������
	;1 - ������ �� ������
Start_1
	MOVF Star, 0 		;���������, ��������� �� �����
	XORLW 0
	BTFSS STATUS, Z
	GOTO Start_2_2		;���� ���������, �� ������ �����
	RRF 	Schet, 1	; �������� ������
	MOVF	Schet, 0
	MOVWF	PORTB		; ������� ����� ��������� 
	MOVLW	0x3			; ��������� ��������
	MOVWF	ZSt
	MOVLW	0x8
	MOVWF	ZSr
	MOVLW	0x7A
	MOVWF	ZMl
	CALL Zader
GOTO Start_1
Zader
	DECFSZ ZMl,1		; ��������� ������� ����, ���� �� �� ������ 0
	GOTO Zader
	DECFSZ ZSr,1		; ��������� ������� ����, ���� �� �� ������ 0
	GOTO Zader
	DECFSZ ZSt,1		; ��������� ������� ����, ���� �� �� ������ 0
	GOTO Zader	
RETURN
Start_1_1
	CLRF Star
	GOTO Start_1
Start_2_2
	CLRF Star
	GOTO Start_2
Start_2
	MOVF Star, 0 		;���������, ������� �� �����
	XORLW 0
	BTFSS STATUS, Z
	GOTO Start_1_1		;���� �������, �� ������ �����
	RLF	Schet, 1		; �������� �����
	MOVF	Schet, 0
	MOVWF	PORTB		; ������� ����� ���������
	MOVLW	0x3			; ��������� �������� 
	MOVWF	ZSt
	MOVLW	0x8
	MOVWF	ZSr
	MOVLW	0x7A
	MOVWF	ZMl
	CALL Zader
GOTO Start_2
Timer
	BTFSC PORTA, 3		;���������, ������ �� ������
	GOTO PROVERKA2  	;���� �� ������, ���������, �� ���� �� ������ �����
	GOTO Proverka1		;���� ��� ������, �� ������ ���������� � 1
Proverka1
	MOVLW 1				;���������� � Naj 1
	MOVWF Naj
	GOTO konetc
PROVERKA2
	MOVF Naj, 0			;���� Naj = 1 �� ������ ���� ������, ������ ��������� 
	XORLW 1				;������������ ������, ����� ��������� � �����
	BTFSC STATUS, Z
	GOTO izmen			
	GOTO konetc
izmen
	MOVLW 1 
	MOVWF Star
	MOVLW 0 
	MOVWF Naj
	GOTO konetc
konetc
	BCF INTCON,02h
RETFIE 
END
