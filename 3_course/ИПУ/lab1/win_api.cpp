#include <windows.h>
#include <iostream>

using namespace std;

HANDLE com;

int main()
{
    //�������������
    LPCTSTR NamePort = "COM1";
    com = CreateFileA(NamePort, GENERIC_READ | GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL);
    if (com == INVALID_HANDLE_VALUE)
    {
        MessageBox(NULL, "���������� ������� ���������������� ����", "Error", MB_OK);
        ExitProcess(1);
    }

    //������


    //������


    CloseHandle(com);
}
