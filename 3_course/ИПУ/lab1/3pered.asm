.MODEL SMALL
.STACK 100h
.DATA
	SAVE_CS dw 0
	SAVE_IP dw 0
.CODE

START:
	mov ax, @data
	mov ds, ax

	mov ah, 35h
	mov al, 0Fh
	int 21h
	mov SAVE_IP, bx
	mov SAVE_CS, es

	mov ds, ax
	mov ah, 25h
	mov al, 0Fh
	int 21h

	




	cli
	in al, 21h
	or al,00010000b
	out dx, al
	sti

	;int_hook proc far
		;iret
	;int_hook endp

	codeend:
		cli
		push ds
		mov dx, SAVE_IP
		mov ax, SAVE_CS
		mov ds, ax
		mov ah, 25h
		mov al, 1ch
		int 21h
		pop ds
		sti



	in al, 21h
	and al,11101111b
	out dx, al
	sti

exit:
	;cli
	mov dx, SAVE_IP
	mov ax, SAVE_CS
	mov ds, ax
	mov ah, 25h
	mov al, 0Fh
	int 21h
	;sti

	mov ax, 4ch
	int 21h
END START