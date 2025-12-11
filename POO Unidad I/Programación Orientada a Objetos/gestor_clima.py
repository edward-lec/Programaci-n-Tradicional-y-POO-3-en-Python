# gestor_clima.py

class GestorClima:
    """Clase encargada de gestionar la interacción con el usuario."""

    @staticmethod
    def ingresar_temperaturas_usuario():
        """Solicita al usuario ingresar las temperaturas de cada día de la semana.

        Este método es estático, lo que significa que no necesita ser llamado
        desde una instancia de la clase. Se encarga de pedir las temperaturas
        de la semana y las devuelve como una lista.
        """
        temperaturas = []  # Lista vacía para almacenar las temperaturas
        print("Ingrese la temperatura de cada día de la semana:\n")
        for i in range(7):
            while True:
                try:
                    # Solicita la temperatura del día i+1
                    temp = float(input(f"Día {i + 1}: "))
                    temperaturas.append(temp)  # Añade la temperatura a la lista
                    break  # Sale del bucle si la entrada es válida
                except ValueError:
                    # Si el valor ingresado no es válido (no es un número), muestra un mensaje de error
                    print("Por favor ingrese un número válido.")
        return temperaturas  # Devuelve la lista con las temperaturas ingresadas

    @staticmethod
    def mostrar_promedio(promedio):
        """Muestra el promedio calculado de las temperaturas.

        Este método muestra el promedio de las temperaturas en un formato legible.
        """
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")
