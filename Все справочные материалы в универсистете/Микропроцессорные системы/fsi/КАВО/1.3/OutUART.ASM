
PUBLIC OutUART

OUT SEGMENT CODE 

RSEG OUT

OutUART:
    JNB  TI,$        ; ����, ���� �������� ���� ���������� �����������
    CLR  TI            ; ������� ���� ���������� �����������
    MOV  SBUF,A        ; ���������� ���� � ����� ��������
RET 

END







































































