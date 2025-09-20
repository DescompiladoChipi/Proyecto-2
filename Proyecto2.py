import random, os, textwrap, re

while True:
    try:
        menu_1 = int(input(textwrap.dedent("""
         ---------------------------------------------------                     
        |         Bienvenido, seleccione una opción!        |
        |                                                   |                    
        | Presiona 1 para efectuar operaciones con Matrices |
        | Presiona 2 para efectuar operaciones con cadenas  |
        |                                                   |                   
        | Presiona 0 para salir del programa                |
         --------------------------------------------------- 
        """)))
    except ValueError:
        os.system('cls')
        print(textwrap.dedent(""" 
               ---------------------------------------------------
              |  Seleccione una de las tres opciones unicamente   |
               ---------------------------------------------------"""))
        continue

    if menu_1 == 1:
        os.system('cls')
        salir_matrices = False
        while not salir_matrices:
            try:
                n1 = int(input(textwrap.dedent("""
                     ---------------------------------------------------
                    |              Calculadora de Matrices              |
                    |                                                   |                    
                    | Ingresa la cantidad de filas de la matriz 1       |
                     --------------------------------------------------- 
                    """)))
            except ValueError:
                print(textwrap.dedent(""" 
                     ---------------------------------------------------
                    |  Ingrese un numero valido de filas para la matriz |
                     ---------------------------------------------------"""))
                continue
            try:
                m1 = int(input(textwrap.dedent("""
                     ---------------------------------------------------
                    |              Calculadora de Matrices              |
                    |                                                   |                    
                    | Ingresa la cantidad de columnas de la matriz 1    |
                     --------------------------------------------------- 
                    """))) 
            except ValueError:
                print(textwrap.dedent(""" 
                     ---------------------------------------------------
                    | Ingrese un numero valido de columnas para la matriz|
                     ---------------------------------------------------"""))
                continue
            if n1<1 or n1>9 or m1<1 or m1>9:
                print(textwrap.dedent(""" 
                     ---------------------------------------------------
                    |La matriz solo puede tener de 1 a 9 filas/columnas |
                     ---------------------------------------------------"""))
            else:
                print(textwrap.dedent(f"""
                     ---------------------------------------------------
                    | La matriz 1 tendra {n1} filas y {m1} columnas         |
                     ---------------------------------------------------"""))
            print(" ---------------------------------------------------")    
            print("| Presiona Enter para continuar...                  |")
            print(" ---------------------------------------------------")
            input()
            os.system('cls')
            
            if n1<1 or n1>9 or m1<1 or m1>9:
                continue    
        
            while True:
                try:
                    n2 = int(input(textwrap.dedent("""
                         ---------------------------------------------------
                        |              Calculadora de Matrices              |
                        |                                                   |                    
                        | Ingresa la cantidad de filas de la matriz 2       |
                         --------------------------------------------------- 
                        """)))
                except ValueError:
                    print(textwrap.dedent(""" 
                         ---------------------------------------------------
                        |  Ingrese un numero valido de filas para la matriz |
                         ---------------------------------------------------"""))
                    continue

                try:
                    m2 = int(input(textwrap.dedent("""
                         ---------------------------------------------------
                        |              Calculadora de Matrices              |
                        |                                                   |                    
                        | Ingresa la cantidad de columnas de la matriz 2    |
                         --------------------------------------------------- 
                        """))) 
                except ValueError:
                    print(textwrap.dedent(""" 
                         ---------------------------------------------------
                        | Ingrese un numero valido de columnas para la matriz|
                         ---------------------------------------------------"""))
                    continue

                if n2<1 or n2>9 or m2<1 or m2>9:
                    print(textwrap.dedent(""" 
                         ---------------------------------------------------
                        |La matriz solo puede tener de 1 a 9 filas/columnas |
                         ---------------------------------------------------"""))
                else:
                    print(textwrap.dedent(f"""
                         ---------------------------------------------------
                        | La matriz 2 tendra {n2} filas y {m2} columnas          |
                         ---------------------------------------------------"""))
                print(" ---------------------------------------------------")    
                print("| Presiona Enter para continuar...                  |")
                print(" ---------------------------------------------------")
                input()
                os.system('cls')

                if n2<1 or n2>9 or m2<1 or m2>9:
                    continue 

                try:
                    menu_ran = int(input(textwrap.dedent("""
                     ---------------------------------------------------
                    |                       Matriz 1                    |
                    |                                                   |
                    | Presiona 1 para ingresar la matriz 1 manualmente  |  
                    | Presione 2 para ingresarla de forma random        |                                 
                     ---------------------------------------------------
                    """)))
                except ValueError:
                    os.system('cls')
                    print(textwrap.dedent(""" 
                         ---------------------------------------------------
                        |  Seleccione una de las dos opciones unicamente    |
                         ---------------------------------------------------"""))
                    continue
                
                if menu_ran == 1:
                    print(textwrap.dedent("""
                     ---------------------------------------------------
                    | Ingrese los datos para la Matriz 1:               |
                    |                                                   |
                    """),end="")
                    matriz1 = []
                    for i in range(n1): 
                        filas = []
                        for j in range(m1):
                            entrada = int(input(f"| Ingrese el numero: {i+1},{j+1} : "))
                            filas.append(entrada)
                        matriz1.append(filas)
                    print(" ---------------------------------------------------")
                    print(textwrap.dedent(""" 
                             ---------------------------------------------------
                            | Esta sera la Matriz 1:                            |
                             ---------------------------------------------------
                        """), end="")
                    for fila in matriz1:
                        for elemento in fila:
                            print(" [ ", end="")
                            print(f"{elemento}" " ]", end="")
                        print()
                    print(" ---------------------------------------------------")    
                    print("| Presiona Enter para continuar...                  |")
                    print(" ---------------------------------------------------")
                    input()

                if menu_ran == 2:
                    matriz1 = []
                    for i in range(n1):
                        filas = []
                        for j in range(m1):
                            filas.append(random.randint(0, 100))
                        matriz1.append(filas)

                    print(textwrap.dedent(""" 
                             ---------------------------------------------------
                            | Esta sera la Matriz 1 aleatoria:                  |
                             ---------------------------------------------------
                        """), end="")
                    for filas in matriz1:
                        for elemento in filas:
                            print(" [ ", end="")
                            print(f"{elemento}" " ]", end=" ") 
                        print()                
                    print(" ---------------------------------------------------")    
                    print("| Presiona Enter para continuar...                  |")
                    print(" ---------------------------------------------------")
                    input()
                try:
                    os.system('cls')
                    menu_ran = int(input(textwrap.dedent("""
                     ---------------------------------------------------
                    |                       Matriz 2                    |
                    |                                                   |
                    | Presiona 1 para ingresar la matriz 2 manualmente  |  
                    | Presione 2 para ingresarla de forma random        |                                 
                     ---------------------------------------------------
                    """)))
                except ValueError:
                    os.system('cls')
                    print(textwrap.dedent(""" 
                         ---------------------------------------------------
                        |  Seleccione una de las dos opciones unicamente    |
                         ---------------------------------------------------"""))
                    continue
                
                if menu_ran == 1:
                    print(textwrap.dedent("""
                     ---------------------------------------------------
                    | Ingrese los datos para la Matriz 2:               |
                    |                                                   |
                    """),end="")
                    matriz2 = []
                    for i in range(n2): 
                        filas = []
                        for j in range(m2):
                            entrada = int(input(f"| Ingrese el numero: {i+1},{j+1} : "))
                            filas.append(entrada)
                        matriz2.append(filas)
                    print(" ---------------------------------------------------")
                    print(textwrap.dedent(""" 
                             ---------------------------------------------------
                            | Esta sera la Matriz 2:                            |
                             ---------------------------------------------------
                        """), end="")
                    for fila in matriz2:
                        for elemento in fila:
                            print(" [ ", end="")
                            print(f"{elemento}" " ]", end="")
                        print()
                    print(" ---------------------------------------------------")    
                    print("| Presiona Enter para continuar...                  |")
                    print(" ---------------------------------------------------")
                    input()
                if menu_ran == 2:
                    matriz2 = []
                    for i in range(n2):
                        filas = []
                        for j in range(m2):
                            filas.append(random.randint(0, 100))
                        matriz2.append(filas)

                    print(textwrap.dedent(""" 
                             ---------------------------------------------------
                            | Esta sera la Matriz 2 aleatoria:                  |
                             ---------------------------------------------------
                        """), end="")
                    for filas in matriz2:
                        for elemento in filas:
                            print(" [ ", end="")
                            print(f"{elemento}" " ]", end=" ") 
                        print()
                    print(" ---------------------------------------------------")    
                    print("| Presiona Enter para continuar...                  |")
                    print(" ---------------------------------------------------")
                    input()

                while True:
                    try:
                        os.system('cls')
                        menu_2 = int(input(textwrap.dedent("""
                         ---------------------------------------------------
                        |                                                   |
                        | Presiona 1 para sumar las dos matrices            |  
                        | Presiona 2 para obtener la matriz transpuesta     |
                        | Presiona 3 para multiplicar las dos matrices      |
                        | Presiona 4 para encontrar un numero en una matriz |
                        |                                                   |
                        | Presiona 0 para regresar al menu principal        |
                        |                                                   |                                    
                         ---------------------------------------------------
                        """)))
                    except ValueError:
                        os.system('cls')
                        print(textwrap.dedent(""" 
                             ---------------------------------------------------
                            |  Seleccione una de las cuatro opciones unicamente |
                             ---------------------------------------------------"""))
                        continue
                    os.system('cls')

                    if menu_2 == 1:
                        
                        if n1 == n2 and m1 == m2:
                            print(textwrap.dedent(""" 
                                 ---------------------------------------------------
                                | Este es el resultado de sumar la Matriz 1 y 2:    |
                                 ---------------------------------------------------"""))
                            matriz_suma = []
                            for i in range(n1):
                                filas = []
                                for j in range(m1):
                                    suma = matriz1[i][j] + matriz2[i][j]
                                    filas.append(suma)
                                matriz_suma.append(filas)
                            for filas in matriz_suma:
                                for elemento in filas:
                                    print(" [ ", end="")
                                    print(f"{elemento}" " ]", end=" ") 
                                print()                
                            print(" ---------------------------------------------------")    
                            print("| Presiona Enter para continuar...                  |")
                            print(" ---------------------------------------------------")
                            input()
                        else:
                            if n1 != n2 or m1 != m2:
                                print(textwrap.dedent(""" 
                                     ---------------------------------------------------
                                    | Solo puedes sumar matrices con la misma cantidad  |
                                    | de filas y columnas.                              |
                                    |                                                   |
                                    |Presiona cualquier tecla para regresar al menu e   |
                                    |intentalo de nuevo.                                |
                                     ---------------------------------------------------"""))
                                input()
                                continue
                        
                    if menu_2 == 2:
                           
                        while True:
                            os.system('cls') 
                            try:
                                menu_t = int(input(textwrap.dedent("""
                                 ---------------------------------------------------
                                |                                                   |
                                | Presiona 1 para la transpuesta de la Matriz 1     |  
                                | Presiona 2 para la transpuesta de la Matriz 2     |
                                | Presiona 3 si quieres usar una nueva Matriz       |
                                |                                                   |
                                | Presiona 0 para volver al menu anterior           |
                                 ---------------------------------------------------
                                """)))
                            except ValueError:
                                print(textwrap.dedent(""" 
                                     ---------------------------------------------------
                                    |  Seleccione una de las dos opciones unicamente    |
                                     ---------------------------------------------------"""))
                                continue

                            if menu_t == 1:
                                os.system('cls')
                                print(textwrap.dedent(""" 
                                     ---------------------------------------------------
                                    | Esta es la Matriz 1 original:                     |
                                     ---------------------------------------------------"""))
                                for filas in matriz1:
                                    for elemento in filas:
                                        print(" [ ", end="")
                                        print(f"{elemento}" " ]", end=" ") 
                                    print()   
                                print(" ---------------------------------------------------")    
                                print("| Presiona Enter para calcular                       |")
                                print(" ---------------------------------------------------")
                                input()

                                print(textwrap.dedent(""" 
                                     ---------------------------------------------------
                                    | Esta es la Matriz 1 transpuesta:                  |
                                     ---------------------------------------------------"""))
                                matriz_transpuesta = []
                                for j in range(m1):
                                    filas = []
                                    for i in range(n1):
                                        filas.append(matriz1[i][j])
                                    matriz_transpuesta.append(filas)
                                for filas in matriz_transpuesta:
                                    for elemento in filas:
                                        print(" [ ", end="")
                                        print(f"{elemento}" " ]", end=" ") 
                                    print()                
                                print(" ---------------------------------------------------")    
                                print("| Presiona Enter para continuar...                  |")
                                print(" ---------------------------------------------------")
                                input()

                            if menu_t == 2:
                                os.system('cls')
                                print(textwrap.dedent(""" 
                                     ---------------------------------------------------
                                    | Esta es la Matriz 2 original:                     |
                                     ---------------------------------------------------"""))
                                for filas in matriz2:
                                    for elemento in filas:
                                        print(" [ ", end="")
                                        print(f"{elemento}" " ]", end=" ") 
                                    print()   
                                print(" ---------------------------------------------------")    
                                print("| Presiona Enter para calcular                      |")
                                print(" ---------------------------------------------------")
                                input()

                                print(textwrap.dedent(""" 
                                     ---------------------------------------------------
                                    | Esta es la transpuesta de la Matriz 2:            |
                                     ---------------------------------------------------"""))
                                matriz_transpuesta = []
                                for j in range(m2):
                                    filas = []
                                    for i in range(n2):
                                        filas.append(matriz2[i][j])
                                    matriz_transpuesta.append(filas)
                                for filas in matriz_transpuesta:
                                    for elemento in filas:
                                        print(" [ ", end="")
                                        print(f"{elemento}" " ]", end=" ") 
                                    print()                
                                print(" ---------------------------------------------------")    
                                print("| Presiona Enter para continuar...                  |")
                                print(" ---------------------------------------------------")
                                input()
                                os.system('cls')

                            if menu_t == 3:
                                os.system('cls')
                                while True:
                                    try:
                                        n3 = int(input(textwrap.dedent("""
                                             ---------------------------------------------------
                                            |              Calculadora de Matrices              |
                                            |                                                   |                    
                                            | Ingresa la cantidad de filas de la matriz nueva   |
                                             --------------------------------------------------- 
                                            """)))
                                    except ValueError:
                                        print(textwrap.dedent(""" 
                                             ---------------------------------------------------
                                            |  Ingrese un numero valido de filas para la matriz |
                                             ---------------------------------------------------"""))
                                        continue

                                    try:
                                        m3 = int(input(textwrap.dedent("""
                                             ---------------------------------------------------
                                            |              Calculadora de Matrices              |
                                            |                                                   |                    
                                            | Ingresa la cantidad de columnas de la matriz      |
                                             --------------------------------------------------- 
                                            """))) 
                                    except ValueError:
                                        print(textwrap.dedent(""" 
                                             ---------------------------------------------------
                                            | Ingrese un numero valido de columnas para la matriz|
                                             ---------------------------------------------------"""))
                                        continue

                                    if n3<1 or n3>9 or m3<1 or m3>9:
                                        print(textwrap.dedent(""" 
                                             ---------------------------------------------------
                                            |La matriz solo puede tener de 1 a 9 filas/columnas |
                                             ---------------------------------------------------"""))
                                    else:
                                        print(textwrap.dedent(f"""
                                             ---------------------------------------------------
                                            | La matriz tendra {n3} filas y {m3} columnas            |
                                             ---------------------------------------------------"""))
                                    print(" ---------------------------------------------------")    
                                    print("| Presiona Enter para continuar...                  |")
                                    print(" ---------------------------------------------------")
                                    input()
                                    os.system('cls')

                                    if n3<1 or n3>9 or m3<1 or m3>9:
                                        continue 


                                    try:
                                        os.system('cls')
                                        menu_ran = int(input(textwrap.dedent("""
                                         ---------------------------------------------------
                                        |                    Matriz nueva                   |
                                        |                                                   |
                                        | Presiona 1 para ingresar la matriz manualmente    |  
                                        | Presione 2 para ingresarla de forma random        |                                 
                                         ---------------------------------------------------
                                        """)))
                                    except ValueError:
                                        os.system('cls')
                                        print(textwrap.dedent(""" 
                                             ---------------------------------------------------
                                            |  Seleccione una de las dos opciones unicamente    |
                                             ---------------------------------------------------"""))
                                        continue
                                    
                                    if menu_ran == 1:

                                        print(textwrap.dedent("""
                                         ---------------------------------------------------
                                        | Ingrese los datos para la Matriz nueva:           |
                                        |                                                   |
                                        """),end="")
                                        matriz3 = []
                                        for i in range(n3): 
                                            filas = []
                                            for j in range(m3):
                                                entrada = int(input(f"| Ingrese el numero: {i+1},{j+1} : "))
                                                filas.append(entrada)
                                            matriz3.append(filas)
                                        input()
                                        print(" ---------------------------------------------------")
                                    if menu_ran == 2:
                                        matriz3 = []
                                        for i in range(n3):
                                            filas = []
                                            for j in range(m3):
                                                filas.append(random.randint(0, 100))
                                            matriz3.append(filas)

                                    os.system('cls')
                                    print(textwrap.dedent(""" 
                                         ---------------------------------------------------
                                        | Esta sera la Matriz nueva:                        |
                                         ---------------------------------------------------
                                        """), end="")
                                    for filas in matriz3:
                                        for elemento in filas:
                                            print(" [ ", end="")
                                            print(f"{elemento}" " ]", end="")
                                        print()

                                    print(" ---------------------------------------------------")    
                                    print("| Presiona Enter para calcular                      |")
                                    print(" ---------------------------------------------------")
                                    input()

                                    print(textwrap.dedent(""" 
                                         ---------------------------------------------------
                                        | Esta es la transpuesta de la Matriz nueva:        |
                                         ---------------------------------------------------"""))
                                    matriz_transpuesta = []
                                    for j in range(m3):
                                        filas = []
                                        for i in range(n3):
                                            filas.append(matriz3[i][j])
                                        matriz_transpuesta.append(filas)
                                    for filas in matriz_transpuesta:
                                        for elemento in filas:
                                            print(" [ ", end="")
                                            print(f"{elemento}" " ]", end=" ") 
                                        print()                
                                    print(" ---------------------------------------------------")    
                                    print("| Presiona Enter para continuar...                  |")
                                    print(" ---------------------------------------------------")
                                    input()
                                    break
                            if menu_t == 0:
                                break
                    if menu_2 == 3:
                        if m1 == n2:
                            print(textwrap.dedent(""" 
                                 ---------------------------------------------------
                                | Este es el total al multiplicar la Matriz 1 y 2   |
                                 ---------------------------------------------------"""))
                            matriz_multi = []
                            for i in range(n1):
                                filas = []
                                for j in range(m2):
                                    suma = 0
                                    for k in range(m1):
                                        suma += matriz1[i][k] * matriz2[k][j]
                                    filas.append(suma)
                                matriz_multi.append(filas)
                            for filas in matriz_multi:
                                for elemento in filas:
                                    print(" [ ", end="")
                                    print(f"{elemento}" " ]", end=" ") 
                                print()                
                            print(textwrap.dedent(""" 
                                 ---------------------------------------------------
                                | Este es el procedimiento para multiplicarlas      |
                                 ---------------------------------------------------"""))
                            for i in range(n1):
                                for j in range(m2):
                                    matriz_multi[i][j] = 0
                                    for k in range(m1):
                                        print(f" [ {matriz1[i][k]} ] * [ {matriz2[k][j]} ]", end="")
                                        matriz_multi[i][j] += matriz1[i][k] * matriz2[k][j]
                                        if k < m1 - 1:
                                            print(" + ", end="")
                                    print(f" = {matriz_multi[i][j]} ")    
                            print()                
                            print(" ---------------------------------------------------")    
                            print("| Presiona Enter para continuar...                  |")
                            print(" ---------------------------------------------------")
                            input()
                    
                        else:
                            if m1 != n2:
                                print(textwrap.dedent(""" 
                                     ---------------------------------------------------
                                    | La cantidad de columnas de la Matriz 1 tiene que  |
                                    | ser igual a la cantidad de filas de la Matriz 2   |
                                    | para poder multiplicarlas                         |             
                                    |                                                   |
                                    |Presiona cualquier tecla para regresar al menu e   |
                                    |intentalo de nuevo.                                |
                                     ---------------------------------------------------"""))
                                input()
                                
                    if menu_2 == 4:
                        while True:
                            try:
                                os.system('cls')
                                menu_num = int(input(textwrap.dedent("""
                                 ---------------------------------------------------
                                | En que matriz deseas buscar un numero?            |
                                |                                                   |
                                | Presiona 1 para buscar en la Matriz 1             |
                                | Presiona 2 para buscar en la Matriz 2             |
                                |                                                   |
                                | Presiona 0 para volver al menu anterior           |                                     
                                 ---------------------------------------------------
                                """)))

                            except ValueError:
                                print(textwrap.dedent(""" 
                                     ---------------------------------------------------
                                    |  Seleccione una de las dos opciones unicamente    |
                                     ---------------------------------------------------"""))
                                continue

                            if menu_num == 1:
                                while True:
                                    try:
                                        num = int(input(textwrap.dedent("""
                                             ---------------------------------------------------
                                            | Ingrese el numero que desea buscar en la Matriz 1 |
                                             ---------------------------------------------------
                                            """)))

                                    except ValueError:
                                        print(textwrap.dedent(""" 
                                             ---------------------------------------------------
                                            |  Ingrese unicamente numeros                       |
                                             ---------------------------------------------------"""))
                                        continue
                                    else:
                                        ubicado = False

                                        for i in range(n1):
                                            for j in range(m1):
                                                if matriz1[i][j] == num:
                                                    print(" ---------------------------------------------------")
                                                    print(f"| El numero {num} se encuentra en la Matriz 1 en la posicion ({i+1}, {j+1}) |")
                                                    print(" ---------------------------------------------------")
                                                    ubicado = True
                                                
                                        if not ubicado:
                                            print(" ---------------------------------------------------")
                                            print(f"| El numero {num} no se encuentra en la Matriz 1.  |")
                                            print(" ---------------------------------------------------")
                                        input()
                                        break
                            if menu_num == 2:
                                while True:
                                    try:
                                        num = int(input(textwrap.dedent("""
                                             ---------------------------------------------------
                                            | Ingrese el numero que desea buscar en la Matriz 2 |
                                             ---------------------------------------------------
                                            """)))

                                    except ValueError:
                                        print(textwrap.dedent(""" 
                                             ---------------------------------------------------
                                            |  Ingrese unicamente numeros                       |
                                             ---------------------------------------------------"""))
                                        continue
                                    else:
                                        ubicado = False

                                        for i in range(n2):
                                            for j in range(m2):
                                                if matriz2[i][j] == num:
                                                    print(" ---------------------------------------------------")
                                                    print(f"| El numero {num} se encuentra en la Matriz 2 en la posicion ({i+1}, {j+1}) |")
                                                    print(" ---------------------------------------------------")
                                                    ubicado = True

                                        if not ubicado:
                                            print(" ---------------------------------------------------")
                                            print(f"| El numero {num} no se encuentra en la Matriz 2.  |")
                                            print(" ---------------------------------------------------")
                                        input()
                                        break
                            if menu_num == 0:
                                break
                    if menu_2 == 0:
                        salir_matrices = True
                        break
                if salir_matrices:
                    break
            if salir_matrices:
                break
    if (menu_1 == 2):
        os.system('cls')
        while True:
            try:
                menu_cade = int(input(textwrap.dedent("""
                     ---------------------------------------------------
                    |                    Bienvenido!                    |
                    |                                                   |
                    | Presiona 1 para contar palabras en un texto       |
                    | Presiona 2 para ordenar alfabeticamente una cadena|
                    | Presiona 3 para detectar una subcadena de texto   |
                    | Presiona 4 para verificar un palindromo           |
                    |                                                   |
                    | Presiona 0 para regresar al menu principal        |
                     ---------------------------------------------------
                    """)))
            except ValueError:
                os.system('cls')
                print(textwrap.dedent(""" 
                     ---------------------------------------------------
                    |  Seleccione una de las opciones unicamente        |
                     ---------------------------------------------------"""))
                continue
            os.system('cls')

            if menu_cade == 1:
                print(textwrap.dedent("""
                     ---------------------------------------------------
                    | Porfavor ingresa el texto del que deseas contar   |
                    | cuantas palabras contiene                         |
                    |                                                   |
                    | Y presiona ENTER 2 veces para calcular            |                 
                     ---------------------------------------------------"""))
                lineas = []
              
                while True:
                    linea = input()
                    if linea == "":  
                        break
                    lineas.append(linea)  
                texto = " ".join(lineas) 

                palabras = texto.split()
                contador = len(palabras)
                print(" ---------------------------------------------------")
                print(f"| El texto ingresado tiene {contador} palabras.          |")
                print(" ---------------------------------------------------")
                print(" ---------------------------------------------------")
                print("| Presiona Enter para continuar...                  |")
                print(" ---------------------------------------------------")
                input()
                os.system('cls')

            if menu_cade == 2:
                print(textwrap.dedent("""
                     ---------------------------------------------------
                    | Porfavor ingresa la cadena que deseas ordenar     |
                    |                                                   |
                    | Y presiona ENTER 2 veces para calcular            |                 
                     ---------------------------------------------------"""))
                lineas = [] 
                enter_vacios = 1
                
                while True:
                    linea = input()
                    if linea == "":
                        enter_vacios += 1
                        if enter_vacios == 2:
                            break
                    else:
                        enter_vacios = 1
                        lineas.append(linea)

                texto_completo = " ".join(lineas)
                texto2 = list(texto_completo)
                texto2.sort()
                cadena_ordenada = ''.join(texto2)

                print(" ---------------------------------------------------")
                print(f"| La cadena ordenada es:                             |")
                print(f"| {cadena_ordenada} |")
                print(" ---------------------------------------------------")
                print(" ---------------------------------------------------")
                print("| Presiona Enter para continuar...                  |")
                print(" ---------------------------------------------------")
                input()
                os.system('cls')

            if menu_cade == 3:
                print(textwrap.dedent("""
                     ---------------------------------------------------
                    | Porfavor ingresa el texto en el que deseas        |
                    | encontrar una subcadena:                          |
                    |                                                   | 
                    | Y presiona ENTER 2 veces para confirmar           | 
                     ---------------------------------------------------"""))
                lineas = [] 
                enter_vacios = 1
                
                while True:
                    linea = input()
                    if linea == "":
                        enter_vacios += 1
                        if enter_vacios == 2:
                            break
                    else:
                        enter_vacios = 1
                        lineas.append(linea)

                texto_principal = " ".join(lineas)

                print(textwrap.dedent("""
                     ---------------------------------------------------
                    | Ahora ingresa la subcadena que deseas buscar      |
                    |                                                   |
                    | Y presiona ENTER 2 veces para calcular            |                 
                     ---------------------------------------------------"""))
                lineas_sub = [] 
                enter_vacios = 1
                
                while True:
                    linea_sub = input()
                    if linea_sub == "":
                        enter_vacios += 1
                        if enter_vacios == 2:
                            break
                    else:
                        enter_vacios = 1
                        lineas_sub.append(linea_sub)

                subcadena = " ".join(lineas_sub)

                if subcadena in texto_principal:
                    posiciones = [m.start() for m in re.finditer(re.escape(subcadena), texto_principal)]
                    print(" ---------------------------------------------------")
                    print(f"| La subcadena esta en la posicion: {posiciones}     |")
                    print(" ---------------------------------------------------")
                else:
                    print(" ---------------------------------------------------")
                    print(f"| Esta subcadena no es parte del texto original     |")
                    print(" ---------------------------------------------------")
                
                print(" ---------------------------------------------------")
                print("| Presiona Enter para continuar...                  |")
                print(" ---------------------------------------------------")
                input()
                os.system('cls')

            if menu_cade == 4:
                os.system('cls')
                print(textwrap.dedent("""
                     ---------------------------------------------------
                    | Porfavor ingresa una palabra para verificar si    |
                    | es palindromo o no:                               | 
                     ---------------------------------------------------"""))
                palabra = input()
                if palabra == palabra[::-1]:
                    print(" ---------------------------------------------------")
                    print(f"| La palabra '{palabra}' si es un palindromo       |")
                    print(" ---------------------------------------------------")
                else:
                    print(" ---------------------------------------------------")
                    print(f"| La palabra '{palabra}' no es un palindromo      |")
                    print(" ---------------------------------------------------")
                input()
                os.system('cls')
            if menu_cade == 0:
                break

    if menu_1>2 or menu_1<0:
        os.system('cls')
        print(textwrap.dedent(""" 
             ---------------------------------------------------
            |  Seleccione una de las tres opciones unicamente   |
             ---------------------------------------------------"""))
    if menu_1 == 0:
        break
