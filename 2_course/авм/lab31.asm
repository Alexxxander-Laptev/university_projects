.386
.MODEL small
STACK 100h
data segment use16
array7 db 3 dup(0)
array20 db 3 dup(0)
data ends
text segment use16
assume CS:text, DS:data;10

begin:
mov ax, data
mov ds, ax
mov si, 0

input:
mov ah, 01h
int 21h
mov array7[si], al
sub array7[si], 30h
cmp array7[si], 6
jg exit
cmp si, 2
je ckl1
inc si
jmp input

ckl1:
mov si, 0
mov al, 49
mov dx, 0

des:
mov bl, al
mul array7[si]
add dx, ax
cmp si, 2
je ckl2
inc si
mov al, bl
mov bl, 7
mov ah, 0
div bl
jmp des

ckl2:
mov si, 0
mov ax, dx
mov dl, 20

dvad:
div dl
mov array20[si], ah
cmp si, 2
je stroka
inc si
mov ah, 0
jmp dvad

stroka:
mov bx, 4
mov ah, 02h
mov dl, 0ah
int 21h

view:
cmp array20[si], 9
ja AJ

ckl3:
add array20[si], 30h
mov dl, array20[si]
mov ah, 02h
int 21h
cmp si, 0
je exit
dec si
jmp view

AJ:
add array20[si], 7h
jmp ckl3

exit:
mov bx, 4
mov ah, 02h
mov dl, 0ah
int 21h
mov ah, 4ch
int 21h
text ends
end begin