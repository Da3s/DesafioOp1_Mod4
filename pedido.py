from te import Te

precio_300 = 3000
precio_500 = 5000

# Ingreso de datos de parte del usuario

print('Ingrese numero segun sabor de te que desea')
print('1.- Te Negro')
print('2.- Te Verde')
print('3.- Infusion')
sabor = int(input())

print('Ingrese formato que desea (Solo numeros)')
print('300 gramos')
print('500 gramos')
formato = int(input())

# Precio
precio = Te.saber_precio(formato)

# Tiempo y recomendacion de consumo
tiempo, recomendacion = Te.tiempo_recomendacion(sabor)

# Generar el detalle del pedido

print('Detalle de su pedido:')
print('Sabor del te:')
if sabor == 1:
    print('Te Negro')
elif sabor == 2:
    print('Te Verde')
elif sabor == 3:
    print('Infusion de Hierbas')
print('Formato:', formato, 'gramos')
print('Precio: $', precio)
print('Recomendaciones:', recomendacion,'. El tiempo de preparacion son:', tiempo, 'minutos')