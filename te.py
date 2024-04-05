class Te():
    precio_300 = 3000
    precio_500 = 5000
    
    @staticmethod
    def tiempo_recomendacion(sabor):
        if sabor == 1:
            return 3, 'Tomar al desayuno'
        elif sabor == 2:  
            return 5, 'Tomar al mediodia'
        else:
            return 6, 'Tomar al atardecer'
    
    @staticmethod
    def saber_precio(formato):
        if formato == 300:
            return Te.precio_300
        else:
            return Te.precio_500
