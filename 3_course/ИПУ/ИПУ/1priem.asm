.MODEL SMALL
.STACK 100h
.DATA
.CODE

START:
	mov ax, 80h ;»нциализаци€ ”јѕѕ по адресу 3FB пишем управ. байт с единицой в 7 бите
	mov dx, 3FBh
	out dx, al ;ax - AH затем AL, каждый по 8, в сумме 16

	mov ax, 0Ch ;AH=00h AL=0Ch скорость 9600бит¬с
	mov dx, 3F8h
	out dx, al ;пишем младший байт кода делител€ частоты
	mov ax, 00h 
	mov dx, 3F9h
	out dx, al ;пишем старший байт кода делител€ частоты
	
	mov al, 00111011b
	mov dx, 3FBh
	out dx, al ;пишем управл€ющий байт

VIVOD:
	mov dx, 3FDh ;регистр состо€ний	
	in al, dx ; принимаем состо€ние линии
	and al, 00000001b ;по€вилис ли данные
	cmp al, 00000001b
	jne VIHOD ;если al=0 то переход

	mov dx, 3F8h
	in al, dx ; принимаем	

	mov ah, 02h
	mov dl, al
	int 21h ;вывводим из dl
	jmp VIHOD

VIHOD:
	mov ah, 01h
	int 16h
	jz VIVOD ;если ничего не нажали

	xor ah, ah
	int 16h	;считываем нажатый символ

	cmp al, 1Bh ;код клавишы esc
	jne VIVOD
	mov ah, 4Ch
	int 21h

END START
