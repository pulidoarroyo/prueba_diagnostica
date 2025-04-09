# Para un programa en un lenguaje L, dado un cadena C escrito en L, muestre y cuente la ocurrencia de la palabra E en C

import tkinter as tk
from tkinter import scrolledtext, messagebox


# Clase Aplicacion para crear la interfaz gráfica (ventana, botones, etiquetas) con la libreria "tkinter"

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Ocurrencias de Palabras en Código")
        self.root.geometry("900x700")
        
        # Crear y colocar los widgets
        self.crear_widgets()
        
    def crear_widgets(self):
        # Etiqueta para el área de código
        tk.Label(self.root, text="Pegue su código fuente aquí:", font=("Arial", 10)).pack(pady=(10, 5), anchor="w", padx=10)
        
        # Área de texto para el código con scroll
        self.area_codigo = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=100, height=15)
        self.area_codigo.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Frame para la palabra a buscar
        frame_busqueda = tk.Frame(self.root)
        frame_busqueda.pack(pady=10, fill=tk.X, padx=10)
        
        tk.Label(frame_busqueda, text="Palabra a buscar:").pack(side=tk.LEFT, padx=(0, 5))
        
        self.entrada_palabra = tk.Entry(frame_busqueda, width=30)
        self.entrada_palabra.pack(side=tk.LEFT, padx=5)
        
        # Botón de búsqueda
        self.boton_buscar = tk.Button(frame_busqueda, text="Buscar", command=self.buscar_palabra)
        self.boton_buscar.pack(side=tk.LEFT, padx=5)
        
        # Etiqueta para mostrar el total de ocurrencias
        self.etiqueta_total = tk.Label(self.root, text="", font=("Arial", 10, "bold"))
        self.etiqueta_total.pack(pady=5, anchor="w", padx=10)
        
        # Etiqueta para los resultados
        tk.Label(self.root, text="Resultados:", font=("Arial", 10)).pack(pady=(10, 5), anchor="w", padx=10)
        
        # Área de texto para los resultados con scroll
        self.area_resultados = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=100, height=10)
        self.area_resultados.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Botón para limpiar
        self.boton_limpiar = tk.Button(self.root, text="Limpiar Todo", command=self.limpiar_todo)
        self.boton_limpiar.pack(pady=10)
      
        # Función para contar ocurrencias de una palabra en el código fuente
        # Se considera que una palabra está delimitada por espacios o signos de puntuación
    def contar_ocurrencias_palabra(codigo_fuente, palabra_buscar):
        
        # Se divide al código por líneas
        lineas = codigo_fuente.split('\n')
        total_ocurrencias = 0
        resultados = []
        
        # Delimitadores estándar de palabras
        delimitadores = set("!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~ \t\n")
        
        # Se procesa cada línea
        for num_linea, linea in enumerate(lineas, 1):
            pos_inicial = 0
            linea_tiene_ocurrencia = False
            linea_resaltada = linea
            
            while True:
                # Se busca la próxima ocurrencia de la palabra
                pos_inicial = linea.find(palabra_buscar, pos_inicial)
                
                # Si no hay más ocurrencias, salir del bucle
                if pos_inicial == -1:
                    break
                    
                # Se verifica al es una palabra completa
                es_palabra_completa = True
                
                # Se verifica al caracter antes de la palabra
                if pos_inicial > 0:
                    char_antes = linea[pos_inicial - 1]
                    if char_antes not in delimitadores and not (char_antes.isspace() or char_antes in "([{,;:"):
                        es_palabra_completa = False
                        
                # Se verifica al caracter después de la palabra
                pos_final = pos_inicial + len(palabra_buscar)
                if pos_final < len(linea):
                    char_despues = linea[pos_final]
                    if char_despues not in delimitadores and not (char_despues.isspace() or char_despues in ")]},.;:"):
                        es_palabra_completa = False
                
                # Si es una palabra completa, contarla
                if es_palabra_completa:
                    total_ocurrencias += 1
                    linea_tiene_ocurrencia = True
                    
                    # Resaltar la palabra (para mostrar en la interfaz)
                    inicio = len(linea_resaltada)
                    # Localizar la posición correcta en la cadena posiblemente ya modificada
                    offset = linea_resaltada.find(linea[pos_inicial:pos_final], 
                                                max(0, pos_inicial - 10))
                    
                    if offset != -1:
                        linea_resaltada = (
                            linea_resaltada[:offset] + 
                            ">>>" + linea_resaltada[offset:offset+len(palabra_buscar)] + "<<<" + 
                            linea_resaltada[offset+len(palabra_buscar):]
                        )
                
                # Se avanza y se busca la siguiente ocurrencia
                pos_inicial += len(palabra_buscar)
            
            if linea_tiene_ocurrencia:
                resultados.append(f"Línea {num_linea}: {linea_resaltada}")
        
        return total_ocurrencias, resultados
        
    # Función para buscar la palabra en el código fuente
        
    def buscar_palabra(self):
        # Se obtiene el código y la palabra
        codigo_fuente = self.area_codigo.get("1.0", tk.END)
        palabra_buscar = self.entrada_palabra.get().strip()
        
        # Se valida la entrada
        if not palabra_buscar:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una palabra para buscar.")
            return
        
        if not codigo_fuente.strip():
            messagebox.showwarning("Advertencia", "Por favor, ingrese código fuente para analizar.")
            return
        
        # Se realiza la búsqueda
        total_ocurrencias, resultados = Aplicacion.contar_ocurrencias_palabra(codigo_fuente, palabra_buscar)
        
        # Se muestran resultados
        self.etiqueta_total.config(text=f"Total de ocurrencias de '{palabra_buscar}': {total_ocurrencias}")
        
        # Limpia el área de resultados anterior
        self.area_resultados.delete("1.0", tk.END)
        
        # Se muestra cada línea con ocurrencia
        if resultados:
            self.area_resultados.insert(tk.END, "\n".join(resultados))
        else:
            self.area_resultados.insert(tk.END, f"No se encontraron ocurrencias de '{palabra_buscar}'.")
    
    def limpiar_todo(self):
        self.area_codigo.delete("1.0", tk.END)
        self.area_resultados.delete("1.0", tk.END)
        self.entrada_palabra.delete(0, tk.END)
        self.etiqueta_total.config(text="")

def main():

    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()