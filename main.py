from te import Te_negro, Te_verde, Infusion
from formato_precio import Formato_precio

sabor = input('Ingrese que infusion desea (Te Negro, Te verde o Infusion): ')
peso = input('Ingrese formato que desea (300gr / 500gr): ')


if peso == Formato_precio.formato1:
    print(f'Usted selecciono el formato de {peso}.')
    print(f'El precio es de ${Formato_precio.precio1}')
elif peso == Formato_precio.formato2:
    print(f'Usted selecciono el formato de {peso}.')
    print(f'El precio es de ${Formato_precio.precio2}')
else:
    print('Ingrese un formato valido')
    
    
if sabor.lower() == "te negro":  
    te_negro = Te_negro() 
    print('Recomendacion')
    print(f'El te verde tiene un tiempo de preparacion de {Te_negro.tiempo_preparacion} minutos y {Te_negro.horario}')
elif sabor.lower() == "te verde":
    te_verde = Te_verde()
    print('Recomendacion')
    print(f'El te verde tiene un tiempo de preparacion de {Te_verde.tiempo_preparacion} minutos y {Te_verde.horario}')
elif sabor.lower() == "infusion":
    infusion = Infusion()
    print('Recomendacion')
    print(f'La infusion tiene un tiempo de preparacion de {Infusion.tiempo_preparacion} minutos y {Infusion.horario}')
else:
    "Sabor de té no válido"