import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Visita import Visita
class MonteCarloSimulador:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Monte Carlo")
        
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
        ttk.Label(root, text="Cantidad de visitas (N):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(root, textvariable=self.N).grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Probabilidad de que el que atienda sea hombre:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(root, textvariable=self.prob_hombre).grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Probabilidad de que el que atienda sea mujer:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(root, textvariable=self.prob_mujer).grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Probabilidad de venta si es mujer:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(root, textvariable=self.prob_venta_mujer).grid(row=3, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Probabilidad de venta de productos si es hombre:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.hombre_entries = []
        for i in range(4):
            ttk.Label(root, text=f"Probabilidad de vender {i+1} producto(s):").grid(row=5+i, column=0, sticky="w", padx=10, pady=5)
            entry = ttk.Entry(root, textvariable=self.precios_productos_hombre[i])
            entry.grid(row=5+i, column=1, padx=10, pady=5)
            self.hombre_entries.append(entry)
        
        ttk.Label(root, text="Probabilidad de venta de productos si es mujer:").grid(row=9, column=0, sticky="w", padx=10, pady=5)
        self.mujer_entries = []
        for i in range(3):
            ttk.Label(root, text=f"Probabilidad de vender {i+1} producto(s):").grid(row=10+i, column=0, sticky="w", padx=10, pady=5)
            entry = ttk.Entry(root, textvariable=self.precios_productos_mujer[i])
            entry.grid(row=10+i, column=1, padx=10, pady=5)
            self.mujer_entries.append(entry)
        
        ttk.Label(root, text="Precio del producto si se realiza una venta:").grid(row=13, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(root, textvariable=self.precio_producto).grid(row=13, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Cantidad de visitas a mostrar (I):").grid(row=14, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(root, textvariable=self.I).grid(row=14, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Visita específica a mostrar (J):").grid(row=15, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(root, textvariable=self.J).grid(row=15, column=1, padx=10, pady=5)
        
        # Botón para iniciar la simulación
        ttk.Button(root, text="Iniciar Simulación", command=self.iniciar_simulacion).grid(row=16, columnspan=2, pady=10)

    def iniciar_simulacion(self):
        visitas = []
        n = self.N.get()
        prob_venta_mujer = self.prob_venta_mujer.get()
        total_prob_hombre = sum(var.get() for var in self.precios_productos_hombre)
        total_prob_mujer = sum(var.get() for var in self.precios_productos_mujer)
        ventas_prob_hombre = [var.get() for var in self.precios_productos_hombre]
        ventas_prob_mujer = [var.get() for var in self.precios_productos_mujer]
        prob_mujer = self.prob_mujer.get()
        prob_hombre = self.prob_hombre.get()
        precio = self.precio_producto.get()
        i = self.I.get()
        j = self.J = tk.IntVar()
        datos = [n,prob_venta_mujer,ventas_prob_hombre, 
                 ventas_prob_mujer, prob_mujer, prob_hombre, precio]
        # Validar que la suma de las probabilidades de venta de productos sea 1
        #if total_prob_hombre != 1 or total_prob_mujer != 1 or prob_mujer + prob_hombre != 1:
        #    messagebox.showerror("Error", "La suma de las probabilidades de venta de productos debe ser igual a 1.")
        #    return
        
        for i in range(n):
            if i == 0:
                v = Visita(i+1, 0)
                acum = v.simular(datos)
                visitas.append(v)
            else:
                v = Visita(i+1, acum)
                acum = v.simular(datos)
                visitas.append(v)
        
        for i in visitas:
            print(i)
        messagebox.showinfo("Simulación terminada", "La simulación ha sido completada.")

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = MonteCarloSimulador(root)
# Centrar la ventana en la pantalla
root.eval('tk::PlaceWindow . center')
root.mainloop()
