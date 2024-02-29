.MODEL SMALL
.STACK 100h
.DATA
.CODE

START:
	mov ax, 80h ;������������ ���� �� ������ 3FB ����� �����. ���� � �������� � 7 ����
	mov dx, 3FBh
	out dx, al ;ax - AH ����� AL, ������ �� 8, � ����� 16

	mov ax, 0Ch ;AH=00h AL=0Ch �������� 9600�����
	mov dx, 3F8h
	out dx, al ;����� ������� ���� ���� �������� �������
	mov ax, 00h 
	mov dx, 3F9h
	out dx, al ;����� ������� ���� ���� �������� �������
	
	mov al, 00111011b
	mov dx, 3FBh
	out dx, al ;����� ����������� ����

VIVOD:
	mov dx, 3FDh ;������� ���������	
	in al, dx ; ��������� ��������� �����
	and al, 00000001b ;�������� �� ������
	cmp al, 00000001b
	jne VIHOD ;���� al=0 �� �������

	mov dx, 3F8h
	in al, dx ; ���������	

	mov ah, 02h
	mov dl, al
	int 21h ;�������� �� dl
	jmp VIHOD

VIHOD:
	mov ah, 01h
	int 16h
	jz VIVOD ;���� ������ �� ������

	xor ah, ah
	int 16h	;��������� ������� ������

	cmp al, 1Bh ;��� ������� esc
	jne VIVOD
	mov ah, 4Ch
	int 21h

END START
