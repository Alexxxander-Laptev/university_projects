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
	
VVOD:
	mov ah, 01h
	int 21h ;��������� ��������� � al
	mov dx, 3F8h
	out dx, al
VIHOD:
	cmp al, 1Bh ;��� ������� esc
	jne PROVERKA
	mov ah, 4Ch
	int 21h
PROVERKA:
	mov dx, 3FDh
	in al, dx
	and al, 00100000b
	cmp al, 00100000b	
	je VVOD
	jmp VVOD

END START
