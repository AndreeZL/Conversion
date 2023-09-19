from logica.Conversion import Conversion

print("¿Qué desea convertir?")
print("1. Grados a Radianes")
print("2. Radianes a Grados")

opcion = input("Seleccione 1 o 2: ")

if opcion == '1':
    grados = float(input("Ingrese los grados: "))
    radianes = Conversion.grados_a_radianes(grados)
    print(f"{grados} grados son aproximadamente {radianes} radianes.")
elif opcion == '2':
    radianes = float(input("Ingrese los radianes: "))
    grados = Conversion.radianes_a_grados(radianes)
    print(f"{radianes} radianes son aproximadamente {grados} grados.")
else:
    print("Opción no válida. Seleccione 1 o 2.")