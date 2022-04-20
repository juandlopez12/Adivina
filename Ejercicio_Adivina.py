

num_secreto= int(input("Escriba el numero secreto: "))
num_intentos= int(input("Escriba el numero de intentos: "))
rango_min= int(input("Escriba el rango minio: "))
rango_max= int(input("Escriba el rango maximo: "))


print("¡Bienvenido! Por favor ingrese números entre " + str(rango_min) + " y " + str(rango_max) + " para ganar.")

while num_intentos > 0:
  
  print("Intentos restantes: " + str(num_intentos) + ".")
  num=int(input("Escriba el numero: "))
  
  if num_secreto==num:
    print("¡Felicidades! El número ingresado es correcto.")
    break
  else: 
    
    if num > rango_max or num < rango_min:
      print("El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente")

    elif  num > num_secreto:
      print("Respuesta incorrecta. El número que ingresó es mayor que el número secreto.")
      num_intentos = num_intentos - 1

    elif num < num_secreto:
      print("Respuesta incorrecta. El número que ingresó es menor que el número secreto.")
      num_intentos = num_intentos - 1

    else:
      if num_intentos == 0:
        print ("Se acabaron los intentos. El número correcto era " +  str(num_secreto) + ".")
      


print(" Fin del juego. ¡Gracias por participar!")    