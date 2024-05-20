variables = []
funciones = []
num_if = 0
num_if_cump = 0
num_if_nocump = 0
exit_num = 1
return_num = 1
codigo_asm = ""

def evaluar_bloque(bloque):
    try:
        sentencias = bloque.Sentencias.extra
    except AttributeError:
        sentencias = bloque.Sentencias
    while(sentencias):
        sentencia = sentencias.Sentencia
        get_sentencia(sentencia)
        try:
            sentencias = sentencias.Sentencias.extra
        except AttributeError:
            sentencias = sentencias.Sentencias

def sentencia_bloque(sentencia_bloque):
    sentencia = None
    bloque = None
    try:
        sentencia = sentencia_bloque.Sentencia
    except AttributeError:
        bloque = sentencia_bloque.Bloque
    if(sentencia):
        get_sentencia(sentencia)
    elif(bloque):
        evaluar_bloque(bloque)
        # try:
        #     sentencias = bloque.Sentencias.extra
        # except AttributeError:
        #     sentencias = bloque.Sentencias
        # while(sentencias):
        #     sentencia = sentencias.Sentencia
        #     get_sentencia(sentencia)
        #     try:
        #         sentencias = sentencias.Sentencias.extra
        #     except AttributeError:
        #         sentencias = sentencias.Sentencias
    

def get_sentencia(sentencia_origen):
    global codigo_asm
    global num_if_cump
    global num_if_nocump
    global exit_num
    try:
        sentencia = sentencia_origen.identificador     ##Se verifica que se tenga una sentencia de asignacion
        sentencia = sentencia_origen
    except AttributeError:
        sentencia = None
    if(sentencia):
        id = sentencia.identificador
        ##########################ASIGNACIONES DIRECTAS#############################
        try:
            expresion = sentencia.Expresion.Termino
        except AttributeError:
            expresion = None
        if(expresion):
            for a in variables:
                if(a["id"]==id):
                    a["valor"] = get_termino(expresion)
                    codigo_asm = codigo_asm + "\nMOV CX," + str(get_termino(expresion))
                    codigo_asm = codigo_asm + "\nMOV " + id + "_" + a["contexto"] + " , CX"
        ###########################################################################

        #########################OPERACIONES ARITMETICAS###########################
        try:
            operacion = sentencia.Expresion.opSuma
            expresion = sentencia.Expresion
        except AttributeError:
            try:
                operacion = sentencia.Expresion.opMul
                expresion = sentencia.Expresion
            except AttributeError:
                operacion = None
                expresion = None
        if(operacion == "+"):
            for i in variables:
                if(i["id"] == id):
                    #i["valor"]=sum(expresion)
                    sum(expresion)
                    codigo_asm = codigo_asm + "\nMOV " + id + "_" + i["contexto"] + " , AX"
        elif(operacion == "-"):
            for i in variables:
                if(i["id"] == id):
                    #i["valor"]=res(expresion)
                    res(expresion)
                    codigo_asm = codigo_asm + "\nMOV " + id + "_" + i["contexto"] + " , AX"
        elif(operacion == "*"):
            for i in variables:
                if(i["id"] == id):
                    #i["valor"]=mul(expresion)
                    mul(expresion)
                    codigo_asm = codigo_asm + "\nMOV " + id + "_" + i["contexto"] + " , AX"
        elif(operacion == "/"):
            for i in variables:
                if(i["id"] == id):
                    #i["valor"]=div(expresion)
                    div(expresion)
                    codigo_asm = codigo_asm + "\nMOV " + id + "_" + i["contexto"] + " , AX"
        ###########################################################################

    try:
        sentencia = sentencia_origen.palabraif     ##Se verifica que se tenga una sentencia de if
        sentencia = sentencia_origen
    except AttributeError:
        sentencia = None
        ###############################IF##########################################
    if(sentencia):
        condicion = sentencia.Expresion
        try:
            operando = condicion.opOr
        except AttributeError:
            try:
                operando = condicion.opAnd
            except AttributeError:
                operando = None
        
        if(operando == "&&"):
            condicion_and(condicion,sentencia.SentenciaBloque)
        elif(operando == "||"):
            condicion_or(condicion,sentencia.SentenciaBloque)
        else:
            describir_if(condicion)
            num_if_cump+=1
            codigo_asm = codigo_asm + "\nETIQ_CUMP" + str(num_if_cump) + ":"
            sentencia_bloque(sentencia.SentenciaBloque)
            codigo_asm = codigo_asm + "\nJMP EXIT" + str(exit_num)
            num_if_nocump+=1
            codigo_asm = codigo_asm + "\nETIQ_NOCUMP" + str(num_if_nocump) + ":"
        if(sentencia.Otro):
            sentencia_bloque(sentencia.Otro.SentenciaBloque)
        codigo_asm = codigo_asm + "\nEXIT" + str(exit_num) + ":"
        exit_num+=1
        ###########################################################################
    try:
        sentencia = sentencia_origen.palabrawhile     ##Se verifica que se tenga una sentencia de while
        sentencia = sentencia_origen
    except AttributeError:
        sentencia = None
        ###############################WHILE########################################
    if(sentencia):
        condicion = sentencia.Expresion
        try:
            operando = condicion.opOr
        except AttributeError:
            try:
                operando = condicion.opAnd
            except AttributeError:
                operando = None
        
        if(operando == "&&"):
            condicion_and(condicion,sentencia.Bloque)
        elif(operando == "||"):
            condicion_or(condicion,sentencia.Bloque)
        else:
            exit_num+=1
            codigo_asm = codigo_asm + "\nEXIT" + str(exit_num) + ":"
            describir_if(condicion)
            num_if_cump+=1
            codigo_asm = codigo_asm + "\nETIQ_CUMP" + str(num_if_cump) + ":"
            evaluar_bloque(sentencia.Bloque)
            codigo_asm = codigo_asm + "\nJMP EXIT" + str(exit_num)
            num_if_nocump+=1
            codigo_asm = codigo_asm + "\nETIQ_NOCUMP" + str(num_if_nocump) + ":"
        ###########################################################################


def get_termino(termino):
    global variables
    try:
        valor = termino.entero
        valor = int(valor)
    except AttributeError:
        try:
            valor = termino.real
            valor = float(valor)
        except AttributeError:
            try:
                valor = termino.cadena
            except AttributeError:
                for b in variables:
                    if(b["id"]==termino.identificador):
                        #valor = b["valor"]
                        valor = termino.identificador + "_" + b["contexto"]
    return valor

def sum(expresion):
    global codigo_asm
    a=0
    b=0
    termino = expresion.Expresion.Termino
    a = get_termino(termino)
    codigo_asm = codigo_asm + "\nMOV AX," + str(a)
    
    try:
        termino = expresion.Expresion2.Termino
        sub_op = None
        codigo_asm = codigo_asm + "\nMOV BX," + str(get_termino(termino))
    except AttributeError:
        try:
            sub_op = expresion.Expresion2.opSum
        except AttributeError:
            try:
                sub_op = expresion.Expresion2.opMul
            except AttributeError:
                sub_op = None
    if(sub_op == "+"):
        #b = sum(expresion.Expresion2)
        sum(expresion.Expresion2)
    elif(sub_op == "-"):
        #b = res(expresion.Expresion2)
        res(expresion.Expresion2)
    elif(sub_op == "*"):
        #b = mul(expresion.Expresion2)
        mul(expresion.Expresion2)
    elif(sub_op == "/"):
        #b = div(expresion.Expresion2)
        div(expresion.Expresion2)
    codigo_asm = codigo_asm + "\nADD AX,BX"
    #return(a+b)

def res(expresion):
    global codigo_asm
    a=0
    b=0
    termino = expresion.Expresion.Termino
    a = get_termino(termino)
    codigo_asm = codigo_asm + "\nMOV AX," + str(a)

    try:
        termino = expresion.Expresion2.Termino
        sub_op = None
        codigo_asm = codigo_asm + "\nMOV BX," + str(get_termino(termino))
    except AttributeError:
        try:
            sub_op = expresion.Expresion2.opSum
        except AttributeError:
            try:
                sub_op = expresion.Expresion2.opMul
            except AttributeError:
                sub_op = None
    if(sub_op == "+"):
        #b = sum(expresion.Expresion2)
        sum(expresion.Expresion2)
    elif(sub_op == "-"):
        #b = res(expresion.Expresion2)
        res(expresion.Expresion2)
    elif(sub_op == "*"):
        #b = mul(expresion.Expresion2)
        mul(expresion.Expresion2)
    elif(sub_op == "/"):
        #b = div(expresion.Expresion2)
        div(expresion.Expresion2)
    
    codigo_asm = codigo_asm + "\nSUB AX,BX"
    #return(a-b)

def mul(expresion):
    global codigo_asm
    a=0
    b=0
    termino = expresion.Expresion.Termino
    a = get_termino(termino)
    codigo_asm = codigo_asm + "\nMOV AX," + str(a)

    try:
        termino = expresion.Expresion2.Termino
        sub_op = None
        codigo_asm = codigo_asm + "\nMOV BX," + str(get_termino(termino))
    except AttributeError:
        try:
            sub_op = expresion.Expresion2.opSum
        except AttributeError:
            try:
                sub_op = expresion.Expresion2.opMul
            except AttributeError:
                sub_op = None
    if(sub_op == "+"):
        #b = sum(expresion.Expresion2)
        sum(expresion.Expresion2)
    elif(sub_op == "-"):
        #b = res(expresion.Expresion2)
        res(expresion.Expresion2)
    elif(sub_op == "*"):
        #b = mul(expresion.Expresion2)
        mul(expresion.Expresion2)
    elif(sub_op == "/"):
        #b = div(expresion.Expresion2)
        div(expresion.Expresion2)
    codigo_asm = codigo_asm + "\nMUL BX"
    #return(a*b)

def div(expresion):
    global codigo_asm
    a=0
    b=0
    termino = expresion.Expresion.Termino
    a = get_termino(termino)
    codigo_asm = codigo_asm + "\nMOV AX," + str(a)

    try:
        termino = expresion.Expresion2.Termino
        sub_op = None
        codigo_asm = codigo_asm + "\nMOV BX," + str(get_termino(termino))
    except AttributeError:
        try:
            sub_op = expresion.Expresion2.opSum
        except AttributeError:
            try:
                sub_op = expresion.Expresion2.opMul
            except AttributeError:
                sub_op = None
    if(sub_op == "+"):
        #b = sum(expresion.Expresion2)
        sum(expresion.Expresion2)
    elif(sub_op == "-"):
        #b = res(expresion.Expresion2)
        res(expresion.Expresion2)
    elif(sub_op == "*"):
        #b = mul(expresion.Expresion2)
        mul(expresion.Expresion2)
    elif(sub_op == "/"):
        #b = div(expresion.Expresion2)
        div(expresion.Expresion2)
    
    codigo_asm = codigo_asm + "\nDIV BX"
    #return(a*b)

def describir_if(condicion):
    global codigo_asm
    global num_if
    num_if+=1
    try:
        operando = condicion.opIgualdad
    except AttributeError:
        try:
            operando = condicion.opRelac
        except AttributeError:
            operando = None

    a = get_termino(condicion.Expresion.Termino)
    b = get_termino(condicion.Expresion2.Termino)
    codigo_asm = codigo_asm + "\nMOV AX," + str(a)
    codigo_asm = codigo_asm + "\nMOV BX," + str(b)
    codigo_asm = codigo_asm + "\nCMP AX,BX"
    
    if(operando == "=="):
        codigo_asm = codigo_asm + "\nJE ETIQ_CUMP" + str(num_if)
        codigo_asm = codigo_asm + "\nJMP ETIQ_NOCUMP" + str(num_if)
    elif(operando == ">"):
        codigo_asm = codigo_asm + "\nJA ETIQ_CUMP" + str(num_if)
        codigo_asm = codigo_asm + "\nJMP ETIQ_NOCUMP" + str(num_if)
    elif(operando == ">="):
        codigo_asm = codigo_asm + "\nJAE ETIQ_CUMP" + str(num_if)
        codigo_asm = codigo_asm + "\nJMP ETIQ_NOCUMP" + str(num_if)
    elif(operando == "<"):
        codigo_asm = codigo_asm + "\nJB ETIQ_CUMP" + str(num_if)
        codigo_asm = codigo_asm + "\nJMP ETIQ_NOCUMP" + str(num_if)
    elif(operando == "<="):
        codigo_asm = codigo_asm + "\nJBE ETIQ_CUMP" + str(num_if)
        codigo_asm = codigo_asm + "\nJMP ETIQ_NOCUMP" + str(num_if)

def condicion_or(sentencia,sentencia_bloque_var):
    global codigo_asm
    global num_if_nocump
    global num_if_cump
    global exit_num
    condicion1 = sentencia.Expresion
    describir_if(condicion1)
    num_if_nocump+=1
    codigo_asm = codigo_asm + "\nETIQ_NOCUMP" + str(num_if_nocump) + ":"

    condicion2 = sentencia.Expresion2
    try:
        operando = condicion2.opOr
    except AttributeError:
        try:
            operando = condicion2.opAnd
        except AttributeError:
            operando = None
    
    if(operando == "&&"):
        condicion_and(condicion2)
    elif(operando == "||"):
        condicion_or(condicion2)
    else:
        describir_if(condicion2)
        while(num_if_cump<=num_if_nocump):
            num_if_cump+=1
            codigo_asm = codigo_asm + "\nETIQ_CUMP" + str(num_if_cump) + ":"
        sentencia_bloque(sentencia_bloque_var)
        codigo_asm = codigo_asm + "\nJMP EXIT" + str(exit_num)
        num_if_nocump+=1
        codigo_asm = codigo_asm + "\nETIQ_NOCUMP" + str(num_if_nocump) + ":"





def condicion_and(sentencia,sentencia_bloque_var):
    global codigo_asm
    global num_if_nocump
    global num_if_cump
    global exit_num
    condicion1 = sentencia.Expresion
    describir_if(condicion1)
    num_if_cump+=1
    codigo_asm = codigo_asm + "\nETIQ_CUMP" + str(num_if_cump) + ":"

    condicion2 = sentencia.Expresion2
    try:
        operando = condicion2.opOr
    except AttributeError:
        try:
            operando = condicion2.opAnd
        except AttributeError:
            operando = None
    
    if(operando == "&&"):
        condicion_and(condicion2)
    elif(operando == "||"):
        condicion_or(condicion2)
    else:
        describir_if(condicion2)
        num_if_cump+=1
        codigo_asm = codigo_asm + "\nETIQ_CUMP" + str(num_if_cump) + ":"
        sentencia_bloque(sentencia_bloque_var)
        codigo_asm = codigo_asm + "\nJMP EXIT" + str(exit_num)
        num_if_nocump+=1
        while(num_if_nocump<=num_if_cump):
            codigo_asm = codigo_asm + "\nETIQ_NOCUMP" + str(num_if_nocump) + ":"
            num_if_nocump+=1


def analizador(arbol):
    #print(arbol)
    global variables
    global funciones
    global num_if_cump
    global num_if_nocump
    global codigo_asm
    arbol_2 = arbol
    codigo_asm = codigo_asm + "PAGE 60,132"
    codigo_asm = codigo_asm + "\nTITLE PROG1.EXE"
    codigo_asm = codigo_asm + "\n.MODEL SMALL"
    codigo_asm = codigo_asm + "\n.STACK 64"
    codigo_asm = codigo_asm + "\n;-----------------------------------"
    codigo_asm = codigo_asm + "\n.DATA"
    if (arbol):
        arbol = arbol.Definiciones
        while(arbol):                   ##PARA DESPLAZARSE EN DEFINICIONES
            definicion = arbol.Definicion
            #######################################VARIABLES GLOBALES############################################
            defvar = None
            try:
                defvar = definicion.DefVar
            except AttributeError:
                pass
            if(defvar):
                tipo = defvar.tipo
                while(defvar):
                    variables.append({'id':defvar.identificador,'tipo':tipo,'valor':None,'contexto':"global"})
                    codigo_asm = codigo_asm + "\n" + str(defvar.identificador) + "_global DW ?"
                    try:
                        defvar = defvar.ListaVar.extra
                    except AttributeError:
                        defvar = defvar.ListaVar
            ####################################################################################################

            ###################################FUNCIONES Y SUS VARIABLES########################################
            deffun = None
            try:
                deffun = definicion.DefFunc
            except AttributeError:
                pass
            if(deffun):
                funcion = deffun.identificador
                funciones.append({'id':deffun.identificador,'tipo':deffun.tipo})
                try:
                    param = deffun.Parametros.extra     ##Se verifica que si haya parametros
                except AttributeError:
                    param = deffun.Parametros
                while(param):
                    variables.append({'id':param.identificador,'tipo':param.tipo,'valor':None,'contexto':funcion})
                    codigo_asm = codigo_asm + "\n" + str(param.identificador) + "_" + funcion + " DW ?"
                    try:
                        param = param.ListaParam.extra
                    except AttributeError:
                        param = param.ListaParam
                bloc = deffun.BloqFunc
                try:
                    bloc = bloc.DefLocales.extra        ##Se verifica que exista algo dentro de la funcion
                except AttributeError:
                    bloc = bloc.DefLocales
                while(bloc):
                    try:
                        defvar = bloc.DefLocal.DefVar     ##Se verifica que se definan variables
                    except AttributeError:
                        defvar = None
                    if(defvar):
                        tipo = defvar.tipo
                        while(defvar):
                            variables.append({'id':defvar.identificador,'tipo':tipo,'valor':None,'contexto':funcion})
                            codigo_asm = codigo_asm + "\n" + str(defvar.identificador) + "_" + funcion + " DW ?"
                            try:
                                defvar = defvar.ListaVar.extra
                            except AttributeError:
                                defvar = defvar.ListaVar

                    try:
                        bloc = bloc.DefLocales.extra
                    except AttributeError:
                        bloc = bloc.DefLocales
            ###################################################################################################

            try:
                arbol = arbol.Definiciones.extra
            except AttributeError:
                arbol = arbol.Definiciones

    codigo_asm = codigo_asm + "\n;-----------------------------------"
    codigo_asm = codigo_asm + "\n.CODE"
    codigo_asm = codigo_asm + "\nBEGIN PROC FAR"
    codigo_asm = codigo_asm + "\nMOV AX,@DATA"
    codigo_asm = codigo_asm + "\nMOV DS,AX"

    if(arbol_2):
        arbol_2 = arbol_2.Definiciones
        while(arbol_2):                   ##PARA DESPLAZARSE EN DEFINICIONES
            definicion = arbol_2.Definicion
            ###################################ASIGNACIONES DE VARIABLES########################################
            deffun = None
            try:
                deffun = definicion.DefFunc
            except AttributeError:
                pass
            if(deffun):
                funcion = deffun.identificador
                bloc = deffun.BloqFunc
                try:
                    bloc = bloc.DefLocales.extra        ##Se verifica que exista algo dentro de la funcion
                except AttributeError:
                    bloc = bloc.DefLocales
                while(bloc):
                    try:
                        get_sentencia(bloc.DefLocal.Sentencia)
                    except AttributeError:
                        pass
                    try:
                        bloc = bloc.DefLocales.extra
                    except AttributeError:
                        bloc = bloc.DefLocales
            ###################################################################################################

            try:
                arbol_2 = arbol_2.Definiciones.extra
            except AttributeError:
                arbol_2 = arbol_2.Definiciones

    codigo_asm = codigo_asm + "\nMOV AX,4C00H"
    codigo_asm = codigo_asm + "\nINT 21H"
    codigo_asm = codigo_asm + "\nBEGIN ENDP"
    codigo_asm = codigo_asm + "\nEND BEGIN"
    
    print("\n")
    print("FUNCIONES")
    print("ID","\t","TIPO")
    for a in funciones:
        print(a["id"],"\t",a["tipo"])

    print("\n")
    print("VARIABLES")
    print("ID","\t","TIPO","\t","VALOR","\t","CONTEXTO")
    for a in variables:
        print(a["id"],"\t",a["tipo"],"\t",a["valor"],"\t",a["contexto"])

    f = open("codigo.asm","w")
    f.write(codigo_asm)
    f.close()


#Sigue sentencia bloque del if... D: