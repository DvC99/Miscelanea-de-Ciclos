import funciones_ciclos as fn


sw = "si"
while(sw == "si"):
  print("Digite la opcion que desea usar:")
  op = input("""   1 -> Si desea usar el simulador_caida_libre
   2 -> Si desea usar el generador_generaciones
   3 -> Si desea usar el constructor_triangulos
   4 -> Si desea usar el constructor_tableros\n""")
  
  if(op == "1"):
    dis = input("Digite la distancia a la que esta ubicada el objeto:\n")
    fn.simulador_caida_libre(int(dis))
  elif(op == "2"):
    gen = input("Digite el numero de generaciones que desea calcular:\n")
    print("El numero de personas que hay todas las generaciones es: "+str(fn.generador_generaciones(int(gen))) )
  elif(op == "3"):
    niv = input("Digite el numero de niveles que desea calcular:\n")
    fn.constructor_triangulos(int(niv))
  elif(op == "4"):
    tam = input("Digite el tamaño del tablero que desea calcular:\n")
    fn.constructor_tableros(int(tam))

  sw = input("Desea seguir con el programa: si/no\n")