# Introducción
Existen diferentes paradigmas de programación, y entre ellos se encuentran la Programación Tradicional y la Programación Orientada a Objetos (POO). En este informe se comparan ambos enfoques mediante la explicación de dos programas que resuelven el mismo problema: calcular el promedio de las temperaturas de la semana. A continuación, se describen ambos métodos, sus ventajas, características y diferencias.
# Programación Tradicional
La Programación Tradicional se basa en el uso de funciones y secuencias de instrucciones que se ejecutan de manera lineal y secuencial. Este enfoque es más simple y adecuado para programas pequeños y de corto alcance.
En el primer programa, se utiliza una estructura secuencial en la que se definen tres funciones clave: ingresar_temperaturas(), calcular_promedio() y main().
Función ingresar_temperaturas():
Esta función solicita al usuario las temperaturas de los 7 días de la semana y las almacena en una lista.
Utiliza un bucle for para iterar a través de los 7 días, recibiendo la entrada del usuario y agregándola a la lista.
Función calcular_promedio():
Esta función recibe la lista de temperaturas y calcula el promedio sumando todas las temperaturas y dividiéndolas por el número de elementos (en este caso, 7).
Función main():
La función principal orquesta el flujo del programa, llamando a las funciones anteriores, calculando el promedio y mostrando el resultado.
Este enfoque es simple, directo y fácil de entender. Sin embargo, presenta algunas limitaciones a medida que el programa crece. La lógica y los datos se encuentran mezclados, lo que puede dificultar el mantenimiento y la expansión del código. Además, la falta de estructuras organizadas como las clases puede hacer que el código se vuelva desordenado en programas más grandes, lo que se conoce como código espagueti.
# Programación Orientada a Objetos (POO)
La Programación Orientada a Objetos (POO) es un enfoque que organiza el código en clases y objetos. Cada clase es responsable de manejar un conjunto de datos y comportamientos relacionados, lo que permite estructurar el código de manera más modular y reutilizable. Este enfoque es más adecuado para proyectos grandes, donde la reutilización, la escalabilidad y el mantenimiento del código son esenciales.
En el segundo programa, se implementa la POO utilizando clases para organizar el código. El programa está compuesto por varias clases:
Clase ClimaBase:
Esta es la clase base que define las características comunes de cualquier tipo de clima, como el atributo _temperaturas y los métodos para ingresar temperaturas y calcular el promedio. El método ingresar_temperaturas() está diseñado como un método abstracto que debe ser implementado en las subclases.
Clase ClimaSemanal:
Hereda de ClimaBase y se especializa en gestionar las temperaturas de la semana. Sobrescribe el método ingresar_temperaturas() para recibir las temperaturas desde el exterior y almacenarlas en _temperaturas.
También sobrescribe el método calcular_promedio(), aunque en este caso simplemente imprime un mensaje antes de llamar a la implementación de la clase base.
Clase GestorClima:
Esta clase se encarga de gestionar la interacción con el usuario. Tiene métodos estáticos para solicitar las temperaturas y mostrar el promedio calculado.
Función main():
Al igual que en la programación tradicional, la función principal coordina el flujo del programa, pero en este caso interactúa con las clases creadas, utilizando objetos para gestionar las temperaturas y calcular el promedio.
El uso de clases y objetos permite una mayor organización del código y facilita la expansión. Si en el futuro se quisiera agregar nuevas funcionalidades, como gestionar las temperaturas mensuales o recibir datos de un archivo, este enfoque modular haría que los cambios sean más fáciles de implementar. Además, la herencia y el polimorfismo permiten la reutilización de código, lo que reduce la redundancia y mejora la mantenibilidad.


