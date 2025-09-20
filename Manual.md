# Proyecto 2 Algortimos
En este proyecto podemos encontrar dos utilidades, una calculadora de
matrices y un operador de cadenas de texto.

## Matrices

### Menu Principal
Al iniciar el programa nos encontramos un menú principal que nos da 2 opciones, trabajar con matrices o con cadenas al igual que una opción para cerrar el programa, en caso de que desees operar matrices presiona 1 y Enter, en caso de querer operar cadenas presiona 2 y Enter. 
En caso de que ingreses un número que no sea alguno de esos 3 o una letra el programa le dará un error.

### Operacion de Matrices
Si presionamos 1 para utilizar matrices el programa nos pedira que ingresemos los datos de la primera matriz, empezando por las filas y despues las columnas.
Al final nos mostrara las dimensiones que tendra nuestra matriz.

En caso de que el usuario ingrese un numero menor a 1 o mayor a 9 el programa dara un error, en caso de que se ingrese una letra tambien y se repetira el programa hasta que ingrese informacion valida en la matriz.

En este caso el programa se repetira para poder ingresar una segunda matriz para poder operarlas, si el usuario ingresa un dato que no es valido el programa mostrara los mismos error que la primera matriz.

### Datos de las Matrices 
Una vez ingresadas las dimensiones de las matrices a utilizar, el programa nos dará la opción de ingresar los datos manualmente o generar los datos aleatoriamente, para las dos matrices. 

Si presionas 1 para ingresar los datos manualmente, el programa nos pedirá dato por dato detallando en que posición ira cada uno y nos mostrará como quedará la matriz elegida.

En caso de que el presiones 2 el programa generara los datos aleatoriamente y mostrara el resultado de la matriz aleatoria, esto se repetirá para la matriz 2 igualmente.

## Operaciones 
Una vez ingresemos los datos de las dos matrices el programa nos dará un nuevo menú con las opciones para operar estas matrices. En caso de que el usuario ingrese un numero no establecido en las opciones o una letra el programa se repetirá hasta que elija una de esas opciones.

### Suma
Al presionar 1 en el menu de operaciones el programa realizara la suma de las dos matrices ingresadas anteriormente y mostrara el resultado.

### Matriz Transpuesta
Si presionas 2 se le presentará un nuevo menú en el cual podrá elegir si obtener la matriz transpuesta de la primera o de la segunda matriz ingresada. También mostrara una tercera opción para ingresar una nueva matriz y obtener la transpuesta de esa nueva matriz y la opción de salir de ese menú y regresar al menú de operaciones.

En caso de que presiones 1 o dos el programa nos mostrara la matriz original y al presionar Enter nos mostrara como se la transpuesta de esta. Esto aplica para la matriz 1 y 2.

Si presionas la opción 3 el programa te pedirá que ingrese las dimensiones de la matriz, nos pedirá ingresarla manualmente o ingresarla aleatoriamente y mostrara como se ve y su matriz transpuesta.

### Multiplicacion
Si seleccionas la opcion 3 en el menu de operaciones el programa multiplicara las 2 matrices, mostrara el resultado y mostrara el procedimiento de como llego hasta ahí.

### Buscar un Numero
Si presionas 4 para buscar un numero en una matriz, el programa le mostrará un nuevo menú y preguntará si quiere buscar el numero en la matriz 1 o 2 y dará la opción para regresar al menú de opciones manualmente.

Si ingresas un numero que si es parte de la matriz seleccionada el programa le mostrara en que posición se encuentra, sino el programa mostrara un mensaje diciendo que el número ingresado no está en esa matriz. Esto aplica para las dos matrices.

## Cadenas 
Si presionas la opción 2 desde el menú esto nos dará un nuevo menú con las opciones para operar cadenas. En caso de que ingreses un numero mayor que no se muestra en el menu dara un error, en caso de que se ingrese una letra tambien y se repetira el programa hasta que ingrese informacion valida en la matriz.

### Contar Palabras
Al presionar 1 para contar palabras el programa nos pedirá ingresar el texto del cual deseamos contar las palabras, al darle click al Enter 2 veces el programa contará el total de palabras y nos mostrará el resultado.

### Orden Alfabetico
Al presionar 2 el programa nos pedirá que ingresemos el texto que deseamos ordenar, al presionar Enter dos veces nos mostrara el orden de todas las palabras juntas.

### Subcadena
Si deseas encontrar una subcadena, al presiona 3 el programa nos pedirá el texto y la subcadena que deseamos buscar, si lo que buscamos es una subcadena el programa nos mostrara en que posición empieza del texto empieza, en caso de que no, nos mostrara un error.

### Palindromo
Si deseas confirmar si una cadena es palíndroma o no al presionar 4 el programa nos pedirá que ingresemos una cadena, si es palíndromo o no nos mostrara un mensaje confirmando.