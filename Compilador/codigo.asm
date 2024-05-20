PAGE 60,132
TITLE PROG1.EXE
.MODEL SMALL
.STACK 64
;-----------------------------------
.DATA
x_global DW ?
y_global DW ?
z_global DW ?
w_global DW ?
v_global DW ?
hello_main DW ?
world_main DW ?
;-----------------------------------
.CODE
BEGIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV CX,4
MOV x_global , CX
MOV CX,3
MOV y_global , CX
MOV AX,x_global
MOV AX,y_global
MOV BX,y_global
MUL BX
SUB AX,BX
MOV z_global , AX
EXIT2:
MOV AX,x_global
MOV BX,4
CMP AX,BX
JA ETIQ_CUMP1
JMP ETIQ_NOCUMP1
ETIQ_CUMP1:
MOV AX,x_global
MOV BX,1
SUB AX,BX
MOV x_global , AX
JMP EXIT2
ETIQ_NOCUMP1:
MOV AX,4C00H
INT 21H
BEGIN ENDP
END BEGIN