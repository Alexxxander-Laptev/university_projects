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
	
VVOD:
	mov ah, 01h
	int 21h ;считываем введенное в al
	mov dx, 3F8h
	out dx, al
VIHOD:
	cmp al, 1Bh ;код клавишы esc
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
