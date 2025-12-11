# main.py

from clima_semanal import ClimaSemanal  # Importa la clase ClimaSemanal
from gestor_clima import GestorClima  # Importa la clase GestorClima

def main():
    """Función principal que coordina la ejecución del programa."""
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===\n")

    # Usamos GestorClima para obtener las temperaturas del usuario
    temperaturas = GestorClima.ingresar_temperaturas_usuario()

    # Creamos un objeto de la clase ClimaSemanal
    clima = ClimaSemanal()

    # Ingresamos las temperaturas en el objeto de ClimaSemanal
    clima.ingresar_temperaturas(temperaturas)

    # Calculamos y mostramos el promedio de las temperaturas
    promedio = clima.calcular_promedio()
    GestorClima.mostrar_promedio(promedio)

# Este bloque garantiza que la función main() solo se ejecutará cuando este archivo sea ejecutado directamente.
if __name__ == "__main__":
    main()  # Llama a la función principal para comenzar el programa
