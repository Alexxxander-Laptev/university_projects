include "p16f84.inc"

PushCounter EQU 10h;������� �������
Counter0 EQU 11h; Delay
Counter1 EQU 12h; Delay
Counter2 EQU 13h; Delay
org 0

GOTO Start
Start
BSF STATUS, RP0
MOVLW b'00011111'; �: 4-0 �����
MOVWF TRISA; ������� ������������ ����� �
MOVLW b'00000000'; �: 7-0 ������
MOVWF TRISB; ������� ������������ ����� �
BCF STATUS, RP0; �������� ���� ������ 0
MOVLW B'00000000'; ������������� ����� B �����
MOVWF PORTB
MOVLW 0x00; ������������� �������� �����
MOVWF PushCounter

CheckPushButton; �������� �� ������� 0 ������
BTFSC PORTA,RA0
GOTO CheckPushButton; ���� �� ������ ������������ �������
CALL Delay ; 10�� ���� ������ ������ ��������� �� ������������ ��������(�������)
CheckReleaseButton; ������ ��������
BTFSS PORTA,RA0
GOTO CheckReleaseButton
INCF PushCounter; ���� ������ �������� �������������� �������
MOVFW PushCounter
MOVWF PORTB; ����� �������� �������� � ���� B 
GOTO CheckPushButton

Delay
MOVLW 02h
MOVWF Counter0 ; ��
MOVLW 0Dh
MOVWF Counter1 ; ��
MOVLW 0FFh
MOVWF Counter2 ; ��
Count0
Count1
Count2
DECFSZ Counter2
GOTO Count2
DECFSZ Counter1
GOTO Count1
DECFSZ Counter0
GOTO Count0 ; ��
RETURN ; ��
END