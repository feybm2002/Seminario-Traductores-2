import string

def analizador(cadena):
    elementos=[]
    estado=0
    contador=0
    cadena=cadena+'$'
    while(contador<=(len(cadena)-1)  and estado==0):  
            lexema=''
            token='error'
            num = -1
            while(contador<=(len(cadena)-1) and estado!=20):
                if estado==0:
                    if(cadena[contador].isspace()):
                        estado=0
                    elif cadena[contador].isalpha() or cadena[contador]=='_':
                        estado=4
                        lexema+=cadena[contador]
                        token='identificador'
                        num = 0
                    elif cadena[contador].isdigit():
                        estado=3
                        lexema+=cadena[contador]
                        token='entero'
                        num = 1
                    elif cadena[contador]=='$':
                        estado=20
                        lexema+=cadena[contador]
                        token='pesos'
                        num = 23
                    elif cadena[contador]=='=':
                        lexema+=cadena[contador]
                        token='asignación'
                        num = 18
                        estado=5
                    elif cadena[contador] == "(":
                        estado=20 
                        lexema+=cadena[contador]
                        token='parentesis izq'
                        num = 14
                    elif cadena[contador] == ")":
                        estado=20 
                        lexema+=cadena[contador]
                        token='parentesis der'
                        num = 15
                    elif cadena[contador] == "{":
                        estado=20 
                        lexema+=cadena[contador]
                        token='llave izq'
                        num = 16
                    elif cadena[contador] == "}":
                        estado=20 
                        lexema+=cadena[contador]
                        token='llave der'
                        num = 17
                    elif cadena[contador] == ";":
                        estado=20 
                        lexema+=cadena[contador]
                        token='punto y coma'
                        num = 12
                    elif cadena[contador] == ",":
                        estado=20 
                        lexema+=cadena[contador]
                        token='coma'
                        num = 13
                    elif cadena[contador] == "+" or cadena[contador] == "-":
                        estado=20 
                        lexema+=cadena[contador]
                        token='OpSuma'
                        num = 5
                    elif cadena[contador] == "*" or cadena[contador] == "/":
                        estado=20 
                        lexema+=cadena[contador]
                        token='OpMul'
                        num = 6
                    elif cadena[contador] == ">" or cadena[contador] == "<":
                        estado=6 
                        lexema+=cadena[contador]
                        token='OpRelacional'
                        num = 7
                    elif cadena[contador] == "!":
                        estado=7 
                        lexema+=cadena[contador]
                        token='OpNot'
                        num = 10
                    elif cadena[contador] == "|":
                        estado=8 
                        lexema+=cadena[contador]
                        token='OpOr'
                        num = 8
                    elif cadena[contador] == "&":
                        estado=9 
                        lexema+=cadena[contador]
                        token='OpAnd'
                        num = 9
                    else:
                        estado=20
                        token='error'
                        num = -1
                        lexema=cadena[contador]
                    contador+=1
                elif estado==2:
                    if cadena[contador].isdigit():
                        lexema+=cadena[contador]
                        token='real'
                        num = 2
                        contador+=1
                    else:
                        estado=20
                elif estado==3:
                    if cadena[contador].isdigit():
                        lexema+=cadena[contador]
                        token='entero'
                        num = 1
                        contador+=1
                    elif cadena[contador] == '.':
                        estado = 2
                        lexema+=cadena[contador]
                        token='error'
                        num = -1
                        contador+=1
                    else:
                        estado=20
                elif estado==4:
                    if cadena[contador].isdigit() or cadena[contador].isalpha() or cadena[contador]=='_':
                        estado=4
                        lexema+=cadena[contador]
                        token='identificador'
                        num = 0
                        contador+=1
                    else:
                        estado=20
                elif estado==5:
                    if cadena[contador]=='=':
                        estado=20
                        lexema+=cadena[contador]
                        token='opIgualdad'
                        num = 11
                        contador+=1
                    else:
                        estado=20
                elif estado==6:
                    if cadena[contador]=='=':
                        estado=20
                        lexema+=cadena[contador]
                        token='opRelacional'
                        num = 7
                        contador+=1
                    else:
                        estado=20
                elif estado==7:
                    if cadena[contador]=='=':
                        estado=20
                        lexema+=cadena[contador]
                        token='opIgualdad'
                        num = 11
                        contador+=1
                    else:
                        estado=20
                        token = 'error'
                elif estado==8:
                    if cadena[contador]=='|':
                        estado=20
                        lexema+=cadena[contador]
                        token='opOr'
                        num = 8
                        contador+=1
                    else:
                        estado=20
                        token = 'error'
                        num = -1
                elif estado==9:
                    if cadena[contador]=='&':
                        estado=20
                        lexema+=cadena[contador]
                        token='opAnd'
                        num = 9
                        contador+=1
                else:
                    estado=20
                    token = 'error'
                    num = -1
                        
                    
            estado=0
            elementos.append({'token':token,'lexema':lexema,'num':num})

    for elemento in elementos:
        if elemento['lexema']=="if":
            elemento['token']="condicional SI"
            elemento['num']=19
        if elemento['lexema']=="while":
            elemento['token']="While"
            elemento['num']=20
        if elemento['lexema']=="return":
            elemento['token']="Return"
            elemento['num']=21
        if elemento['lexema']=="else":
            elemento['token']="Else"
            elemento['num']=22
        if elemento['lexema']=="int":
            elemento['token']="Tipo de dato"
            elemento['num']=4
        if elemento['lexema']=="float":
            elemento['token']="Tipo de dato"
            elemento['num']=4
        if elemento['lexema']=="char":
            elemento['token']="Tipo de dato"
            elemento['num']=4
        if elemento['lexema']=="void":
            elemento['token']="Tipo de dato"
            elemento['num']=4

    return elementos