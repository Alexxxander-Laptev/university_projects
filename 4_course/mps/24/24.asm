; ���������� ��������� PIC16F84, ������� ���������� ����������
include "p16f84.inc" ; ���������� ���� � ��������� ���������
;������������� ������ ������
ORG 0
GOTO Start
ORG 0004h
GOTO Timer
Timer:
DECFSZ 030h, 1
GOTO next
MOVLW B'00000000' ;��������� ����������
MOVWF INTCON
next:
BCF INTCON,02h
RETFIE
Start
BCF STATUS, RP1
BSF STATUS, RP0 ; �������� ���� ������ 1
;����������� ������
MOVLW B'00000111'
MOVWF OPTION_REG
BCF STATUS, RP0 ; �������� ���� ������ 0
MOVLW B'10100000' ;��������� ����������
MOVWF INTCON
MOVLW h'98' ;���������� � ������ 030 10
MOVWF 030h
MOVLW h'F0' ;���������� �������� � TMR0
MOVWF TMR0 ;��������� ������
loop:
BTFSC INTCON, 5
GOTO loop
GOTO Start
END 