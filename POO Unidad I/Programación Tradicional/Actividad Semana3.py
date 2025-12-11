
# Programa: Promedio semanal del clima
# Paradigma: Programación Tradicional
# Descripción: Este programa solicita al usuario
#              las temperaturas de los 7 días de
#              la semana y calcula el promedio.
#Elaborado por: Leiber Correa

# Función: ingresar_temperaturas
# Objetivo: Solicitar al usuario la temperatura de
#           cada uno de los 7 días y almacenarlas
#           en una lista.
# Retorna: Lista con 7 temperaturas ingresadas.
# -----------------------------------------------------
def ingresar_temperaturas():
    temperaturas = []  # Lista vacía donde se guardarán las temperaturas
    print("Ingrese la temperatura de cada día de la semana:\n")

    # Bucle para solicitar la temperatura de los 7 días
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))  # Convierte la entrada a número decimal
        temperaturas.append(temp)            # Agrega la temperatura a la lista

    return temperaturas  # Regresa la lista completa

# Función: calcular_promedio
# Objetivo: Calcular el promedio de un conjunto de
#           temperaturas.
# Parámetros: temps -> lista de temperaturas
# Retorna: Valor numérico del promedio.

def calcular_promedio(temps):
    return sum(temps) / len(temps)  # Suma todos los valores y divide para el total


# Función principal: main
# Objetivo: Coordinar el flujo del programa llamando
#           a las funciones de ingreso y cálculo.

def main():
    print("=== PROMEDIO SEMANAL DEL CLIMA ===")

    # Llamada para ingresar las temperaturas
    temps = ingresar_temperaturas()

    # Cálculo del promedio semanal
    promedio = calcular_promedio(temps)

    # Muestra el resultado con dos decimales
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")



# Punto de inicio del programa
main()
