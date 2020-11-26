# Rabin-Karp algorithm en python


numero_caracteres_d = 36 # d es el número de caracteres en el alfabeto de entrada

def search(patron, texto):
    primo = 13 # Numero Primo
    patron_m = len(patron) # longitud del patron
    texto_n = len(texto) # longitud del texto
    hash_p = 0 # valor hash para el patrón
    hash_t = 0 # valor hash para el texto
    ventana_h = 1 # el valor hash de la primera ventana

    for i in range(0,patron_m-1):
        ventana_h = (ventana_h*numero_caracteres_d) % primo # calculamos el hast del patron en la ventana

    # Calcule el valor hash para el usuario y el texto
    for i in range(0,patron_m):
        hash_p = (numero_caracteres_d*hash_p + ord(patron[i])) % primo # calculamos el hast del patron 
        hash_t = (numero_caracteres_d*hash_t + ord(texto[i])) % primo # calculamos el hast del texto 

    # Encuentra el partido
    for i in range(0,texto_n-patron_m+1): 
    # Verifique los valores hash de la ventana actual de texto y
    # el patrón si los valores hash coinciden, solo verifique
    # para personajes uno por uno
        if hash_p == hash_t:      
        # Compruebe los personajes uno por uno
            for j in range(0,patron_m):
                if texto[i+j] != patron[j]:
                    break

            j += 1           
            # si p == t y pat [0 ... M-1] = txt [i, i + 1, ... i + M-1]
            if j == patron_m:
                print("El patrón se encuentra en la posición: " + str(i+1))
        # Calcular el valor hash para la siguiente ventana de texto: Eliminar
        # dígito inicial, agregar dígito final
        if i < texto_n-patron_m:
            hash_t = (numero_caracteres_d*(hash_t-ord(texto[i])*ventana_h) + ord(texto[i+patron_m])) % primo   
            # Podríamos obtener valores negativos de t, convirtiéndolo en
            # positivo
            if hash_t < 0:
                hash_t = hash_t+primo

texto = input('Escriba el texto: ')
patron = input('Escriba la palabra que desea buscar: ')
search(patron, texto)