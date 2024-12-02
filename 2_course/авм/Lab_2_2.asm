;LAB_2_2.asm
.MODEL small
.STACK 100h
.MODEL small
.STACK 100h
.DATA
	s db '',0dh,'                                       *',0dh,'                                       *',0dh,'                                       *',0dh,'                                       *',0dh,'                                       *',0dh,'$'
.CODE
start: ; определяем сегмент кода
	mov ax,@data ; инициализируем сегмент данных.
	mov ds,ax ;в DS заносим адрес начала сегмента данных
	mov ah,00; уст видео режим
	mov al,0 ; заносим в ah номер функци 21-го прерывания
	int 10h
	mov ah, 0
	mov al, 1
	mov ah, 02H
	mov dh, 0h
	mov dl,10h
	int 10h
	mov ah, 9
	mov dx, offset s
	int 21h
input:
	mov ah, 08h
	int 21h
	mov cl, 0
	cmp al, 09h
	je exit
output:
	mov ah, 02h
	mov dh, cl
	mov dl, 39
	int 10h
	mov dl, al
	mov ah, 02h
	int 21h
	inc cl
	cmp cl, 5
	jl output
	jmp input
exit:
	mov ah, 4ch
	int 21h
END