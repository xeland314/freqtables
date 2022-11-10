from lib import FreqTable, crear_intervalos

# Se crean 8 intervalos desde 0 con ancho de 4:
intervalos = crear_intervalos(8, 0, 4)
frecuencias = [47, 32, 25, 20, 12, 5, 4, 5]
# Se inicializa la tabla con los intervalos y frecuencias:
tabla_con_intervalos = FreqTable(intervalos, frecuencias)
print("Tabla #01".center(62, "~"))
print(tabla_con_intervalos)