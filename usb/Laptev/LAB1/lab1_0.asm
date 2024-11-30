NAME LAB1

MAIN SEGMENT CODE
CSEG AT 0

LJMP start
USING 0
RSEG MAIN

start:

MOV A, #5                             
ADD A, 78H 
MOV DPTR, #1
MOVX @DPTR, A  
CLR A
ADDC A, #0
MOV DPTR, #0
MOVX @DPTR, A  

LJMP start
  
END
