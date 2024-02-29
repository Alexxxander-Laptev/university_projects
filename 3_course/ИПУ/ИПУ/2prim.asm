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
	mov ah, 02h	; принимаем символ
	mov dx, 0
	int 14h

	mov ah, 02h	; выводим его на экран
	mov dl, al	
	int 21h

	mov ah, 01h	; отправляем любой символ, иначе признак приема залипнет и не станет единицей
	mov dx, 0
	mov al, 0
	int 14h

exit:
	mov ah, 01h
	int 16h
	jz check ;если ничего не нажали

	int 21h	;считываем нажатый символ

	cmp al, 1bh ;код клавишы esc
	jne check
	mov ah, 4Ch
	int 21h

check:
	mov ah, 03h ; получаем статус порта
	mov dx, 0
	int 14h
	and ah, 00000001b	; проверяем, пришел ли байт
	cmp ah, 00000001b
	je output      ; если не пришел, то ждем дальше
	jmp output

END START
