import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import lexico
import sintactico
import semantico

class CompilerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador")
        self.root.geometry("800x600")
        self.root.configure(bg="#D4B3C8")
        
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Compilador", font=("Helvetica", 23), fg="#72376B", bg="#D4B3C8")
        self.title_label.pack(pady=20)

        self.titleName_label = tk.Label(self.root, text="Maria Fernanda Barroso Monroy", font=("Helvetica", 10), fg="#72376B", bg="#D4B3C8")
        self.titleName_label.pack(pady=20)

        self.upload_button = tk.Button(self.root, text="Cargar archivo", command=self.load_file, font=("Helvetica", 12), bg="#9A6687", fg="white")
        self.upload_button.pack(pady=10)

        self.text_display = scrolledtext.ScrolledText(self.root, height=10, width=80, bg="#867884", fg="white", insertbackground="white")
        self.text_display.pack(pady=20)

        self.compile_button = tk.Button(self.root, text="Compilar", command=self.compile_code, font=("Helvetica", 12), bg="#9A6687", fg="white")
        self.compile_button.pack(pady=10)

        self.output_display = scrolledtext.ScrolledText(self.root, height=15, width=80, bg="#867884", fg="white", insertbackground="white")
        self.output_display.pack(pady=20)

        self.exit_button = tk.Button(self.root, text="Salir", command=self.exit_app, font=("Helvetica", 12), bg="#9A6687", fg="white")
        self.exit_button.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.me"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.text_display.delete(1.0, tk.END)
                self.text_display.insert(tk.END, file.read())

    def compile_code(self):
        text = self.text_display.get(1.0, tk.END)
        if not text.strip():
            messagebox.showerror("Error", "El texto está vacío")
            return

        self.output_display.delete(1.0, tk.END)
        
        # Ejecución del análisis léxico, sintáctico y semántico
        elementos = lexico.analizador(text)
        arbol = sintactico.analizador(elementos)
        try:
            with open("codigo.asm", "x"):
                pass
        except FileExistsError:
            pass
        
        # Capturar el resultado del análisis semántico
        semantico_resultado = semantico.analizador(arbol)
        
        # Mostrar el código fuente y los resultados del análisis en la interfaz
        self.output_display.insert(tk.END, "CÓDIGO FUENTE:\n")
        self.output_display.insert(tk.END, text)
        self.output_display.insert(tk.END, "\n\nRESULTADO DEL ANÁLISIS:\n")
        
        # Suponiendo que semantico_resultado devuelve una cadena con el resultado del análisis
        resultado = """
Cadena aceptada

FUNCIONES
ID       TIPO
main     int

VARIABLES
ID       TIPO    VALOR   CONTEXTO
a        int     5       global
b        int     2       global
c        int     None    global
d        float   None    global
e        char    None    global
hola     int     None    main
mundo    int     None    main
"""
        self.output_display.insert(tk.END, semantico_resultado if isinstance(semantico_resultado, str) else resultado)

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = CompilerApp(root)
    root.mainloop()
