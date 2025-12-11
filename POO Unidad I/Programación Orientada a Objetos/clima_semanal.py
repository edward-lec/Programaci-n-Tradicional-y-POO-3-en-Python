# clima_semanal.py

from clima_base import ClimaBase  # Importa la clase base para heredar sus métodos

class ClimaSemanal(ClimaBase):
    # Clase derivada de ClimaBase que gestiona las temperaturas de una semana.

    def ingresar_temperaturas(self, temperaturas):
        # Recibe una lista de temperaturas y las almacena en el atributo _temperaturas.

        # Este método reemplaza el de la clase base, almacenando las temperaturas
        # pasadas como parámetro en la lista _temperaturas.

        self._temperaturas = temperaturas

    def calcular_promedio(self):
        # Calcula el promedio semanal de las temperaturas.

        # Este método sobrescribe el método `calcular_promedio` de la clase base.
        # Aquí se podría agregar lógica adicional si fuera necesario, pero en este
        # caso solo llama al método de la clase base para calcular el promedio.

        print("\nCalculando promedio semanal...")
        return super().calcular_promedio()  # Llama al método de la clase base para calcular el promedio
