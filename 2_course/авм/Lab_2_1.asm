;LAB_2_1.asm
.MODEL small
.STACK 100h
.DATA
s1 db '',0dh,0ah,'S',0dh,0ah,' U',0dh,0ah,'  R',0dh,0ah,'   N',0dh,0ah,'    A',0dh,0ah,'     M',0dh,0ah,'      E',0dh,'$'
s3 db '',0dh,'PATRONYMIC$'	       
s2 db '',0dh,'                                       N',0dh,'                                       A',0dh,'                                       M',0dh,'                                       E',0dh,'$'
.CODE
	start: ; определяем сегмент кода
	mov ax,@data ; инициализируем сегмент данных.
	mov ds,ax ;в DS заносим адрес начала сегмента данных
	mov ah,00; уст видео режим
	mov al,1 ; заносим в ah номер функци 21-го прерывания
	int 10h
	klav:
	mov ah, 8
	int 21h
	cmp al, 5Bh
	je fam
	cmp al, 37h
	je nam
	cmp al, 71h
	je otch
	cmp al, 09h
	je exit
	jmp klav
 	fam:
	mov ah, 0
	mov al, 1
	mov ah, 02H
	mov dh, 8h
	mov dl,21h
	int 10h
	mov ah, 9
	mov dx, offset s1
	int 21h
	jmp klav
	nam:
	mov ah, 0
	mov al, 1
	mov ah, 02H
	mov dh, 0h
	mov dl,10h
	int 10h
	mov ah, 9
	mov dx, offset s2
	int 21h
	jmp klav
	otch:
	mov ah, 0
	mov al, 1
	mov ah, 02H	
	mov dh, 0h
	mov dl,28h
	int 10h
	mov ah, 9
	mov dx, offset s3
	int 21h
	jmp klav
	exit:
	mov ah, 4ch
	int 21h
END