; ���������� ��������� PIC16F84, ������� ���������� ����������
include "p16f84.inc" ; ���������� ���� � ��������� ���������
address_data	EQU 24h
address_EE		EQU 25h
it				EQU 23h

DelimoeH		EQU 010h
DelimoeL		EQU 011h
DelitelH		EQU 020h
DelitelL 		EQU 021h
ChastnoeH		EQU 014h
ChastnoeL		EQU 013h

; ������������� ������ ������
ORG 		0
GOTO 		Start

Start:
BCF 		STATUS, RP1
BSF 		STATUS, RP0 ; �������� ���� ������ 1
MOVLW		B'11111111' ; ����������� ���� � ��� ����
MOVWF 		TRISB

; ����� 2 �������� ����� �� ����� B
BCF 		STATUS, RP0 ; �������� ���� ������ 0
MOVF 		PORTB, 0
MOVWF 		DelitelH
MOVF 		PORTB, 0
MOVWF 		DelitelL

; ����� ������ ����� �� EEPROM
BCF    STATUS, RP0    ; Bank 0
MOVLW  10h
MOVWF  EEADR          ; Address to read
BSF    STATUS, RP0    ; Bank 1
BSF    EECON1, RD     ; EE Read
BCF    STATUS, RP0    ; Bank 0
MOVF		EEDATA, 0
MOVWF		DelimoeH

BCF    STATUS, RP0    ; Bank 0
MOVLW  11h
MOVWF  EEADR          ; Address to read
BSF    STATUS, RP0    ; Bank 1
BSF    EECON1, RD     ; EE Read
BCF    STATUS, RP0    ; Bank 0
MOVF		EEDATA, 0
MOVWF		DelimoeL

GOTO 		Delenie

Delenie
	CLRF	ChastnoeH	; �������� ������� � �������
	CLRF	ChastnoeL
Cycle	; ���������� �������� �������� �� ��������
	MOVF	DelitelH,0	; ������ �������� �������� � W
	SUBWF	DelimoeH,1	; �������� �������� �� ��������, ��������� �� � W
	BTFSS	STATUS, C	; ���� ��� ��������� �� �� ��������, �� ���������� ��������� �������� ��������
	GOTO	EndDiv

	MOVF	DelitelL,0	; ������ �������� �������� � W
	SUBWF	DelimoeL,1	; �������� �������� �� ��������, ��������� �� � W
	BTFSS	STATUS, C	; ���� ��� ��������� �� �� ��������, �� ���������� ��������� �������� ��������
	GOTO	CheckHighByte	; ����� ��������� �� ��������� �������� �����
	RetCycle			; ����� �������� �� CheckHighByte

	;GOTO	CheckBufferByte	; ����� ��������� �� ��������� �������� �����
	;ReturnCycle

	INCF	ChastnoeL,1	; ����������� �������
	BTFSC	STATUS, Z   ; ���� ��� ���������� ��������� ������������, ��...
	INCF	ChastnoeH,1	; ...����������� ������� ���� ��������
GOTO Cycle	; ��������� �� ���������
CheckHighByte	; �������� �������� �����
	MOVF	DelimoeH,1	; ���������, �� �������� �� ������� ���� �����
	BTFSC	STATUS, Z   ; ���� ������� ���� - �� ����, �� ���������� �������
	GOTO	EndDiv		; ���� ������� ���� - ���� (�������� ��������), �� ��������� � �����
	DECF	DelimoeH,1	; ��������� ������� ���� ��������
GOTO RetCycle	; ������������ �������			
;CheckBufferByte:
;	MOVF	Buffer,1	; ���������, �� �������� �� ������� ���� �����
;	BTFSC	STATUS, Z   ; ���� ������� ���� - �� ����, �� ���������� �������
;	GOTO	EndDiv		; ���� ������� ���� - ���� (�������� ��������), �� ��������� � �����
;GOTO ReturnCycle	; ������������ �������			
EndDiv	; ��������, ���� �� ���������� 0 (������ �������) (������� ���������)
	MOVF	DelitelL, 0	; ������ �������� �������� � W
	ADDWF	DelimoeL, 1	; ���������� ������ �������, ��� ����� ��������
	MOVF	DelitelH, 0
	;ADDLW	1
	ADDWF	DelimoeH, 1
	
Endless:
;������� ��������� 
MOVLW 		h'2'
MOVWF 		it
MOVLW 		h'11'
MOVWF 		address_EE
MOVLW 		h'13'
MOVWF 		address_data

Mark:
MOVF 		address_data, 0
MOVWF 		FSR
MOVF 		INDF, 0
MOVWF 		EEDATA
MOVF 		address_EE, 0
MOVWF 		EEADR
BCF 		STATUS, RP1 ; �������� ���� ������ 1
BSF 		STATUS, RP0
bsf 		EECON1, 2
movlw 		h'55'
movwf 		EECON2
movlw 		h'AA'
movwf 		EECON2
bsf 		EECON1, WR ; ���������� WR ���, ������ ������

Viv:
BTFSS 		EECON1, EEIF
GOTO 		Viv
BCF 		EECON1, EEIF
BCF 		STATUS, RP0 ; �������� ���� ������ 0
INCF 		address_EE
INCF 		address_data
DECFSZ 		it, 1
GOTO 		Mark
END