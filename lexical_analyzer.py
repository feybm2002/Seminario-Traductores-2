# Maria Fernanda Barroso Monroy
# Seminario de Traductores de Lenguajes 2
# Mini Analizador Lexico

import re                # Libreria paa tokens
import tkinter as tk     # Libreria para GUI
from tkinter import ttk  # Libreria para GUI

def analizador_lexico(sentencia):
    # Patrones para tokens
    patron_numero = r'\d+'
    patron_operador = r'[\+\-\*/]'
    patron_identificador = r'[a-zA-Z_]\w*'
    patron_caracter_especial = r'[\(\)\[\]\{\},;:.<>!@#$%^&*_+=?`~\'"]'

    # Combinar patrones
    patron_total = f'({patron_numero})|({patron_operador})|({patron_identificador})|({patron_caracter_especial})'

    # Buscar coincidencias en la sentencia
    coincidencias = re.findall(patron_total, sentencia)

    # Procesar las coincidencias y generar tokens
    tokens = []
    for numero, operador, identificador, caracter_especial in coincidencias:
        if numero:
            tokens.append(('NUMERO', int(numero)))
        elif operador:
            tokens.append(('OPERADOR', operador))
        elif identificador:
            tokens.append(('IDENTIFICADOR', identificador))
        elif caracter_especial:
            tokens.append(('CARACTER_ESPECIAL', caracter_especial))

    return tokens

def analizar():
    sentencia = entrada_texto.get()
    resultado = analizador_lexico(sentencia)
    resultado_texto.config(state=tk.NORMAL)
    resultado_texto.delete(1.0, tk.END)
    for token in resultado:
        resultado_texto.insert(tk.END, f"{token}\n")
    resultado_texto.config(state=tk.DISABLED)

# GUI
raiz = tk.Tk()
raiz.title("Analizador Léxico")


etiqueta_sentencia = ttk.Label(raiz, text="Ingresa la sentencia:")
etiqueta_sentencia.pack(pady=10)
entrada_texto = ttk.Entry(raiz, width=50)
entrada_texto.pack(pady=10)


boton_analizar = ttk.Button(raiz, text="Analizar", command=analizar)
boton_analizar.pack(pady=10)


resultado_texto = tk.Text(raiz, height=10, width=50, state=tk.DISABLED)
resultado_texto.pack(pady=10)

raiz.mainloop()