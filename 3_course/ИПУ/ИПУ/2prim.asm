.MODEL SMALL
.STACK 100h
.DATA
.CODE
START:
	mov dx, 00h 
	mov al, 11111011b
	mov ah, 00h
	int 14h

output:
	mov ah, 02h	; ��������� ������
	mov dx, 0
	int 14h

	mov ah, 02h	; ������� ��� �� �����
	mov dl, al	
	int 21h

	mov ah, 01h	; ���������� ����� ������, ����� ������� ������ �������� � �� ������ ��������
	mov dx, 0
	mov al, 0
	int 14h

exit:
	mov ah, 01h
	int 16h
	jz check ;���� ������ �� ������

	int 21h	;��������� ������� ������

	cmp al, 1bh ;��� ������� esc
	jne check
	mov ah, 4Ch
	int 21h

check:
	mov ah, 03h ; �������� ������ �����
	mov dx, 0
	int 14h
	and ah, 00000001b	; ���������, ������ �� ����
	cmp ah, 00000001b
	je output      ; ���� �� ������, �� ���� ������
	jmp output

END START
