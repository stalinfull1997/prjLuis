# Funciones de módulos nativos de python y de librerías
import prettytable
import numpy as np
import matplotlib.pyplot as plt 

# Funciones de módulos propios
from liberias.materiales import calcular_losa

def calcular_materiales(largo, ancho, espesor):
    tabla = prettytable.PrettyTable()
    tabla.field_names = ["Variable", "Valor"]

    espesor_metros = espesor / 100
    volumen = largo * ancho * espesor_metros
    cemento = volumen * 7

    cantidad_arena = 0
    cantidad_grava = 0
    parihuela_metros = 0.027

    saco_de_cemento = 0
    while saco_de_cemento < cemento:
        cantidad_arena += 2 * parihuela_metros
        cantidad_grava += 3 * parihuela_metros
        saco_de_cemento += 1

    tabla.add_row(["Largo de la Losa (m)", largo])
    tabla.add_row(["Ancho de la Losa (m)", ancho])
    tabla.add_row(["Espesor de la Losa (cm)", espesor])
    tabla.add_row(["Volumen de la losa (m^3)", volumen])
    tabla.add_row(["Cantidad de cemento necesaria (sacos)", cemento])
    tabla.add_row(["Cantidad de arena necesaria (m^3)", cantidad_arena])
    tabla.add_row(["Cantidad de grava necesaria (m^3)", cantidad_grava])

    print ("Tabla de dosificación de materiales: ")
    return tabla, volumen, cemento, cantidad_arena, cantidad_grava


def graficar_distribucion_materiales(volumen, cemento, arena, grava):
    materiales = ['Cemento', 'Arena', 'Grava']
    cantidades = [cemento, arena, grava]

    plt.bar(materiales, cantidades)
    plt.xlabel('Materiales')
    plt.ylabel('Cantidad (m^3)')
    plt.title('Distribución de materiales en la losa')
    plt.show()


def main():
    largo = float(input("Ingrese el largo de la losa en metros: "))
    ancho = float(input("Ingrese el ancho de la losa en metros: "))
    espesor = float(input("Ingrese el espesor de la losa en centímetros: "))

    # tabla, volumen, cemento, arena, grava = calcular_materiales(largo, ancho, espesor)
    tabla, volumen, cemento, arena, grava = calcular_losa(largo, ancho, espesor)
    #print(matematicas.restar(3,6))
    print(tabla)
    graficar_distribucion_materiales(volumen, cemento, arena, grava)

if __name__ == '__main__':
    main()