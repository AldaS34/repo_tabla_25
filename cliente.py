#probar la clase y sus metodos
import tabla as tbl


mi_tabla = int(input("Ingresa un numero: "))

mi_objeto = tbl.tabla(mi_tabla)

print("Tabla normal:")
mi_objeto.mostrarNormal()

print("Tabla Invertida:")
mi_objeto.mostrarInvertido()