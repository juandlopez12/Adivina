# Adivina
Adivina el # secreto
El juego trata de que los participantes deberán intentar adivinar un número secreto en un número determinado de intentos 
se decide implementar ciertas reglas para hacer más interesante el juego.

El juego debe cumplir las siguientes reglas


1.El organizador es quien debe ingresar el número secreto, un número máximo de intentos y el valor mínimo y máximo donde 
se puede encontrar el número secreto
2.El juego debe darle la bienvenida al jugador con el siguiente texto
¡Bienvenido! Por favor ingrese números entre <mínimo> y <máximo> para ganar.
3.En cada ronda se debe indicar al jugador el número de intentos restantes con el que cuenta de la siguiente forma:
Intentos restantes: <intentos>.
4.Si el número ingresado no está dentro del intervalo, se debe imprimir el siguiente mensaje. No se resta ningún intento
El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente
5.Si el valor ingresado por el jugador es correcto se debe imprimir el siguiente mensaje
¡Felicidades! El número ingresado es correcto.
6.En caso de que el valor ingresado sea incorrecto, pero el jugador aún tenga intentos, se debe indicar al jugador si 
el número ingresado es mayor o menor al número secreto con uno de los siguientes dos mensajes, según corresponda
Respuesta incorrecta. El número que ingresó es mayor que el número secreto.
Respuesta incorrecta. El número que ingresó es menor que el número secreto.
7.Si el jugador se queda sin intentos se debe imprimir el siguiente mensaje. No se indica si el número es mayor o menor 
que el número secreto
Se acabaron los intentos. El número correcto era <valor>.
8.Al finalizar el juego, sin importar el resultado, se debe imprimir el siguiente mensaje
 Fin del juego. ¡Gracias por participar!
