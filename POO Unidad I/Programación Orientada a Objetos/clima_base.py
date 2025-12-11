# clima_base.py
class ClimaBase:
    """Clase base que representa un conjunto de temperaturas."""

    def __init__(self):
        # Inicializa una lista vacía para almacenar las temperaturas.
        # Este atributo está protegido (con convención de nombre con un guion bajo).

        self._temperaturas = []  # Atributo protegido

    def ingresar_temperaturas(self, temperaturas):
        """Método abstracto para ingresar las temperaturas."""
        # Este método se utiliza para ingresar las temperaturas en las subclases
        # Cada subclase debe implementarlo según sus necesidades específicas.

        raise NotImplementedError("Este método debe ser implementado en la subclase.")

    def calcular_promedio(self):
       # Método para calcular el promedio de las temperaturas almacenadas.

       # Si la lista de temperaturas está vacía, devuelve 0.
       # Si hay temperaturas, devuelve el promedio de la lista.

        if len(self._temperaturas) == 0:
            return 0  # Si no hay temperaturas, el promedio es 0
        return sum(self._temperaturas) / len(self._temperaturas)  # Promedio de las temperaturas

