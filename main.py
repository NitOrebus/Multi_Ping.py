import os
import time

def ping(): #Funcion princical del programa

    iplist = [] #Lista de direcciones ip raw
    iponline = [] #Lista de direcciones ip en linea
    ipoffline = []  #Lista de direcciones ip fuera de línea

    #Leer el archivo ip.txt para optener las direcciones ip
    try:
        iplist = open("ip.txt",'r').readlines() #Abre el archivo .txt, lo lee y guarda cada fila por separado en una lista

    except FileNotFoundError:
        print("No se ha encontrado el archivo 'ip.txt'")
        time.sleep(5)
        exit()

    #Si el archivo está vacio finaliza el programa
    if len(iplist) == 0:
            print("No hay direcciones ip en el archivo")
            time.sleep(5)
            exit()

    print(f"Haciendo ping a {len(iplist)} direcciones IP\nEste proceso puede tardar un rato...")
    print("==========================================================")

    #Proceso de hacer ping
    for ip in iplist:

        ip = ip.strip( )   #Quitar los espacios al principio y final de la cadena
        ip = ip.strip('\n') #Quitar el salto de línea al final de la cadena

        if ip in ("/", "", "-", "&", '"', "%", "{", "?"): #Si la cadena contiene alguno de los elementos indicados salta al siguiente elemento en la lista
            print(f"Direccion {ip} no valida\n")
            continue
        else:
            response = os.popen(f"ping -n 1 {ip}").read()

            if "bytes=32" in response:
                print(f'>>> Se ha establecido una conexión exitosa con la {ip}\n')
                iponline.append(ip)
                
            else:
                print(f'No se pudo conectar a la {ip}\n')
                ipoffline.append(ip)

    print("==========================================================")
    print(f"Proceso de ping a {len(iplist)} direcciones ip completado.\n\nDirecciones en linea: {len(iponline)}\nDirecciones fuera de linea: {len(ipoffline)}")
    print("==========================================================\n")

    #Crear el archivo de salida para guardar las direcciones ip con su respuesta
    archivo_salida = open("resultados.txt",'w')
    archivo_salida.write("-- Direcciones IP en linea --\n")

    for ip in iponline:
        archivo_salida.write(f"- {ip}\n")

    archivo_salida.write("\n-- Direcciones IP fuera de linea --\n")

    for ip in ipoffline:
        archivo_salida.write(f"- {ip}\n")

    archivo_salida.close()
    
    decision = input("Hacer otro intento? (S/N): ").lower()

    if decision == 's':
        pass
    else:
        exit()

#------------------------------------------------------------------------------

#Menu principal
print("==========================================================")
print("-- Multi-Ping 1.1 Beta --\n")
time.sleep(1)

while True:
    selector_menu = "0"

    while not selector_menu in ("1","2","3"):

        print("- Empezar (1)\n- Como usar (2)\n- Salir (3)\n")

        selector_menu = input("->> ")
        print("==========================================================")

        match selector_menu: #Se ejecuta la opcion elegida por el usuario
            case "1":
                ping()

            case "2":
                print("Como usar:\n")
                print("- Asegúrate de tener conexión a la red.\n- Crea un archivo de texto llamado 'ip.txt' y escribe las direcciones ip que quieres verificar, una por línea.")
                print("- Ejecuta el programa y espera a que termine. El programa leerá el archivo 'ip.txt' y hará ping a cada dirección ip. Si el archivo no existe o está vacío, el programa te mostrará un mensaje de error.")
                print("- Al finalizar, el programa generará un archivo de texto llamado 'resultados.txt' con el resultado de cada ping. Las direcciones ip que respondieron estarán arriba y las que no respondieron estarán abajo.\n")
                time.sleep(5)

            case "3":
                exit()
            
            case _: #Si se introduce algo que no es una de las opciones anteriores, da error y vuelve a preguntar que hacer
                print(f"\nError, opción incorrecta ({selector_menu})\n")
                time.sleep(1)