try:
    archivo = open ("myFile.txt", "r")
    
    for lines in archivo:
        print(lines)
except FileNotFoundError:
    print ("No se encontró el archivo")
except:
    print("Error con el archivo")
finally:
    try:
        archivo.close()
        print("Se cerró el archivo con éxito")
    except:
        print("Error inesperado, el programa terminara")
