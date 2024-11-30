
PUBLIC OutUART

OUT SEGMENT CODE 

RSEG OUT

OutUART:
    JNB  TI,$        ; Ждем, пока появится флаг прерывания передатчика
    CLR  TI            ; Очищаем флаг прерывания передатчика
    MOV  SBUF,A        ; Отправляем байт в буфер передачи
RET 

END







































































