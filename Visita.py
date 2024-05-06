import random
class Visita():
    def __init__(self, nro:int, acum_venta:int):
        self.nro = nro
        self.abrio = False
        self.es_mujer = False
        self.vendio = False
        self.cantidad = 0
        self.precio_venta = 0
        self.venta = 0
        self.acum_venta = acum_venta

    def simular(self, datos):
        self.precio_venta = datos[6]
        rnd_abrio = random.random()
        if rnd_abrio >= 0.30:
            self.abrio = True
            rnd_sexo = random.random()
            if rnd_sexo < datos[4]:
                self.es_mujer = True
                rnd_venta = random.random()
                if rnd_venta < datos[1]:
                    self.vendio = True
                    rnd_ventas = random.random()
                    if rnd_ventas < datos[3][0]:
                        self.cantidad = 1
                    elif datos[3][0] <= rnd_ventas < (datos[3][1] + datos[3][0]):
                        self.cantidad = 2
                    elif (datos[3][1] + datos[3][0]) <= rnd_venta < 1:
                        self.cantidad = 3
                    self.venta = self.cantidad * self.precio_venta
                    self.acum_venta = self.acum_venta + self.venta
                    return self.acum_venta
                else:
                    self.vendio = False
                    return self.acum_venta
            else: ##es hombre
                self.es_mujer = False
                rnd_venta = random.random()
                if rnd_venta < 0.25:
                    self.vendio = True
                    rnd_ventas = random.random()
                    if rnd_ventas < datos[2][0]:
                        self.cantidad = 1
                    elif datos[2][0] <= rnd_ventas < (datos[2][0] + datos[2][1]):
                        self.cantidad = 2
                    elif (datos[2][0] + datos[2][1]) <= rnd_venta < (datos[2][0]+datos[2][1]+datos[2][2]):
                        self.cantidad = 3
                    elif (datos[2][0]+datos[2][1]+datos[2][2]) <= rnd_venta < 1:
                        self.cantidad = 4
                    self.venta = self.cantidad * self.precio_venta
                    self.acum_venta = self.acum_venta + self.venta
                    return self.acum_venta
                else:
                    self.vendio = False
                    return self.acum_venta
        else:
            self.abrio = False
            return self.acum_venta
        
    def __str__(self):
        # Definir el estado de si es mujer o hombre
        genero = "Mujer" if self.es_mujer else "Hombre"
        # Definir si abrió o no
        abrio_str = "Abrió" if self.abrio else "No abrió"
        # Definir si vendió o no
        vendio_str = "Vendió" if self.vendio else "No vendió"

        # Formatear la información en una cadena
        return f"Nro de visita: {self.nro:,} - {abrio_str} - Género: {genero} - {vendio_str} - Cantidad: {self.cantidad:,} - Acumulado: {self.acum_venta:,.2f}"