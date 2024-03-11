class EP:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        cadena = self.name
        cadena = cadena + "\n"
        try:
            cadena = cadena + str(self.Definiciones)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.Definicion)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.DefVar)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.DefFunc)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.puntoycoma)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.ListaVar)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.identificador)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.coma)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.BloqFunc)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.parentesiscerrar)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.Parametros)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.parentesisabrir)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.tipo)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.ListaParam)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.llavecerrar)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.DefLocales)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.llaveabrir)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.DefLocal)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.Sentencia)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.Sentencias)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.Expresion)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.igual)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.Otro)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.SentenciaBloque)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.palabraif)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.Bloque)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.palabrawhile)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.ValorRegresa)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.palabrareturn)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.LlamadaFunc)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.palabraelse)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.ListaArgumentos)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.entero)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.real)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.cadena)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.Argumentos)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.opSuma)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.opNot)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.opMul)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.opRelac)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.opIgualdad)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.opAnd)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.opOr)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.Termino)
        except AttributeError:
            pass
        try:
            cadena = cadena + str(self.extra)
        except AttributeError:
            pass

        
        return cadena