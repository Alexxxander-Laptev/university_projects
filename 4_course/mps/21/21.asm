include "p16f84.inc" ; ���������� ���� � ��������� ���������
;����������
First EQU 10h
;������������� ������ ������
ORG 0
GOTO Start
Start
BCF STATUS, RP1
BSF STATUS, RP0 ; �������� ���� ������ 1
MOVLW B'00011111' ; ����������� ���� � ��� ����
MOVWF TRISA
MOVLW B'00000000' ; ����������� ���� � ��� �����
MOVWF TRISB
BCF STATUS, RP0 ; �������� ���� ������ 0
Metka:
CLRW
CLRF First
MOVF PORTA,0 ; ������ ������� �������� ����� �� ����� � � W
ANDLW 0x0F ; ������� ������� �������� �����
MOVWF First ; ��������� �������� � ������
SWAPF First, 1
MOVF PORTA,0 ; ������ ������� �������� �����
ANDLW 0x0F ; ������� ������� �������� �����
IORWF First,0 ; �������� ��� �������� �����, ��������� � W
ADDLW 5 ; ���������� W � ������ 5, ��������� � W
MOVWF PORTB ; ���������� ��������� � ���� B
CLRW ; ������� ������� W
BTFSC STATUS,C
INCF W,0
MOVWF PORTB ; ���������� ������� � ���� B
GOTO Metka
END