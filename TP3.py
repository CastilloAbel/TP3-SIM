import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Visita import Visita
from tkinter import Scrollbar

class MonteCarloSimulador:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Monte Carlo")
        
        # Crear un frame para los campos de entrada de datos y el widget Text
        input_frame = ttk.Frame(root)
        input_frame.grid(row=0, column=0, padx=5, pady=10)

        # Variables para almacenar los parámetros
        self.N = tk.IntVar()
        self.prob_hombre = tk.DoubleVar()
        self.prob_mujer = tk.DoubleVar()
        self.prob_venta_mujer = tk.DoubleVar()
        self.precios_productos_hombre = [tk.DoubleVar() for _ in range(4)]  # Lista para almacenar las probabilidades de vender 1, 2, 3 y 4 productos
        self.precios_productos_mujer = [tk.DoubleVar() for _ in range(3)]  # Lista para almacenar las probabilidades de vender 1, 2 y 3 productos
        self.precio_producto = tk.DoubleVar()
        self.I = tk.IntVar()
        self.J = tk.IntVar()
        
        # Crear los widgets para introducir los parámetros
        ttk.Label(root, text="Cantidad de visitas (N):", background=root.cget('background')).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(root, textvariable=self.N).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Probabilidad de que el que atienda sea hombre:", background=root.cget('background')).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(root, textvariable=self.prob_hombre).grid(row=1, column=1, padx=5, pady=5)
    
        ttk.Label(root, text="Probabilidad de que el que atienda sea mujer:", background=root.cget('background')).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(root, textvariable=self.prob_mujer).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Probabilidad de venta si es mujer:" ,background=root.cget('background')).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(root, textvariable=self.prob_venta_mujer).grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Probabilidad de venta de productos si es hombre:", background=root.cget('background')).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.hombre_entries = []
        
        for i in range(4):
            ttk.Label(root, text=f"Probabilidad de vender {i+1} producto(s):", background=root.cget('background')).grid(row=5+i, column=0, sticky="w", padx=5, pady=5)
            entry = ttk.Entry(root, textvariable=self.precios_productos_hombre[i])
            entry.grid(row=5+i, column=1, padx=5, pady=5)
            self.hombre_entries.append(entry)
        
        ttk.Label(root, text="Probabilidad de venta de productos si es mujer:", background=root.cget('background')).grid(row=9, column=0, sticky="w", padx=5, pady=5)
        self.mujer_entries = []
        
        for i in range(3):
            ttk.Label(root, text=f"Probabilidad de vender {i+1} producto(s):", background=root.cget('background')).grid(row=10+i, column=0, sticky="w", padx=10, pady=5)
            entry = ttk.Entry(root, textvariable=self.precios_productos_mujer[i])
            entry.grid(row=10+i, column=1, padx=10, pady=5)
            self.mujer_entries.append(entry)
        
        ttk.Label(root, text="Precio del producto si se realiza una venta:", background=root.cget('background')).grid(row=13, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(root, textvariable=self.precio_producto).grid(row=13, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Cantidad de visitas a mostrar (I):", background=root.cget('background')).grid(row=14, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(root, textvariable=self.I).grid(row=14, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Visita específica a mostrar (J):", background=root.cget('background')).grid(row=15, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(root, textvariable=self.J).grid(row=15, column=1, padx=5, pady=5)
        
        # Crear un estilo para el botón
        style = ttk.Style()
        style.configure("Custom.TButton", background="white")

        # Crear el botón y aplicar el estilo
        ttk.Button(root, text="Iniciar Simulación", command=self.iniciar_simulacion, style="Custom.TButton").grid(row=16, columnspan=2, pady=10)

        # Crear un widget Text para mostrar los resultados
        self.resultados_text = tk.Text(root, height=40, width=100)
        self.resultados_text.grid(row=0, column=2, padx=120, pady=20, rowspan=50)

    
    

    def iniciar_simulacion(self):

        prob_hombre = self.prob_hombre.get()
        prob_mujer = self.prob_mujer.get()
        precios_hombre = sum([i.get() for i in self.precios_productos_hombre])
        precios_mujer = sum([i.get() for i in self.precios_productos_mujer])
        
        
        if prob_hombre + prob_mujer != 1:
            messagebox.showerror("Error", "La suma de las probabilidades de que el que atienda sea hombre y mujer debe ser igual a 1.")
        
        elif precios_hombre != 1:
            messagebox.showerror("Error", "La suma de las probabilidades de venta de los hombres debe ser igual a 1.")

        elif precios_mujer != 1:
            messagebox.showerror("Error", "La suma de las probabilidades de venta de las mujeres debe ser igual a 1.")
        
        else:
            visitas = []
            ventas = []
            n = self.N.get()
            prob_venta_mujer = self.prob_venta_mujer.get()
            ventas_prob_hombre = [var.get() for var in self.precios_productos_hombre]
            ventas_prob_mujer = [var.get() for var in self.precios_productos_mujer]
            prob_mujer = self.prob_mujer.get()
            prob_hombre = self.prob_hombre.get()
            precio = self.precio_producto.get()
            i = self.I.get()
            j = self.J.get()
            
            datos = [n,prob_venta_mujer,ventas_prob_hombre, 
                    ventas_prob_mujer, prob_mujer, prob_hombre, precio]
            
            for x in range(n):
                if x == 0:
                    v = Visita(x+1, 0)
                    acum = v.simular(datos)
                    visitas.append(v)
                else:
                    v = Visita(x+1, acum)
                    acum = v.simular(datos)
                    visitas.append(v)
            
            # Guardar las n las visitas en un archivo
            # Acumular las visitas que vendieron revistas
            filename = "visitas.txt"
            with open(filename, "w") as file:
                for visita in visitas:
                    file.write(str(visita) + "\n")
                    if visita.vendio:
                        ventas.append(visita)
        
            print("Las visitas se han guardado en el archivo:", filename)

            # Probabilidad de que el vendedor venda revistas
            prob_vender = len(ventas) / n

            # Mostrar i visitas a partir de la visita J en la ventana
            resultados = ""
            for idx, visita in enumerate(visitas[j-1:j+i], start=j):
                resultados += f"Iteración {idx}: {visita}\n"
            
        # Mostrar la información de la última visita simulada con espacio antes y después
            resultados += f"\nInformación de la última visita simulada:\n{visitas[-1]}\n"
            resultados += f"\nProbabilidad de vender suscripciones: {prob_vender}\n"

            # Limpiar el widget Text antes de agregar los resultados
            self.resultados_text.delete("1.0", tk.END)
            # Agregar los resultados al widget Text
            self.resultados_text.insert(tk.END, resultados)

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.configure(bg="#B0E0E6")
app = MonteCarloSimulador(root)
# Centrar la ventana en la pantalla
root.eval('tk::PlaceWindow . center')
root.mainloop()
