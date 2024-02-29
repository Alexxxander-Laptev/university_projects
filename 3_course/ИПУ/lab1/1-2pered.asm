.MODEL SMALL
.STACK 100h
.DATA
.CODE

START:
	mov dx, 00h 
	mov al, 11111011b
	mov ah, 00h
	int 14h

exit:
	mov ah, 01h
	int 16h
	jz input
	cmp al, 1Bh ;код клавишы esc
	jne PROVERKA
	mov ah, 4Ch
	int 21h

input:
	mov ah, 1h;
	mov dx, 0;
	int 14h;

PROVERKA:
	mov ah, 03h ; получаем статус порта
	mov dx, 0
	int 14h
	and ah, 00000001b	; проверяем, пришел ли байт
	cmp ah, 00000001b
	je exit      ; если не пришел, то ждем дальше
	jmp exit

END START