#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>
#include <sstream>
#include <cctype>
#include <algorithm>

using namespace std;

int main(){
	
	int i, j, k, numero, menu_1, menu_2, menu_3, menu_ran, menu_t, menu_num, n1, m1, n2, m2, n3, m3, num;
	int menu_cade;
	string texto, palabras, lineas_orden, texto2, texto3, texto_total, subcadena, palindromo;

	int suma[9][9];
	int matriz1[9][9];
	int matriz2[9][9];
	int matriz3[9][9];
	int multi[9][9];
	
	do 
	{
		cout << " ---------------------------------------------------\n";
		cout << "|                     Bienvenido!                   |\n";
		cout << "|                                                   |\n";
		cout << "| Presiona 1 para efectuar operaciones con matrices |\n";
		cout << "| Presiona 2 para efectuar operaciones con cadenas  |\n";
		cout << "|                                                   |\n";
		cout << "| Presiona 0 para salir del programa                |\n";
		cout << " --------------------------------------------------- \n";	
		while (!(cin >> menu_1) || menu_1<0 || menu_1>2) { 
				  	cin.clear(); 
			       	cin.ignore(1000, '\n'); 
			        cout << " ---------------------------------------------------\n";
			        cout << "|  Seleccione una de las tres opciones unicamente   |\n";
			        cout << " ---------------------------------------------------\n";
			    }
						
		switch(menu_1)
		{
			case 1:		
				system("cls");
				do {
					cout << " ---------------------------------------------------\n";
					cout << "|               Calculadora de Matrices             |\n";
					cout << "|                                                   |\n";
					cout << "|   Ingresa la cantidad de filas de la matriz 1     |\n";
					cout << " ---------------------------------------------------\n";
					while (!(cin >> n1)) { 
				       	cin.clear(); 
				        cin.ignore(1000, '\n'); 
				        cout << " ---------------------------------------------------\n";
				        cout << "| Ingrese un numero valido de filas para la matriz  |\n";
				        cout << " ---------------------------------------------------\n";
				    }
				    
					cout << " ---------------------------------------------------\n";
					cout << "|  Ingresa la cantidad de columnas de la matriz 1   |\n";
					cout << " ---------------------------------------------------\n";
					while (!(cin >> m1)) { 
				       	cin.clear(); 
				        cin.ignore(1000, '\n'); 
				        cout << " ---------------------------------------------------\n";
				        cout << "|Ingrese un numero valido de columnas para la matriz|\n";
				        cout << " ---------------------------------------------------\n";
				    }
				    
				    if (n1>9 || m1>9 || n1<1 || m1<1)
				    {
				    	cout << " ---------------------------------------------------\n";
				        cout << "|La matriz solo puede tener de 1 a 9 filas/columnas |\n";
				        cout << " ---------------------------------------------------\n";
				        _getch();
				       	system("cls");	
					} else {
						cout << " ---------------------------------------------------\n";
						cout << "|     La Matriz 1 tendra: " << n1 << " filas y " << m1 << " columnas      |\n";
						cout << " ---------------------------------------------------\n";
						_getch();
					}
				}	while (n1>9 || m1>9 || n1<1 || m1<1);
				
			    
				do 
				{
					system("cls");
					cout << " ---------------------------------------------------\n";
					cout << "|               Calculadora de Matrices             |\n";
					cout << "|                                                   |\n";
					cout << "|   Ingresa la cantidad de filas de la matriz 2     |\n";
					cout << " ---------------------------------------------------\n";
					while (!(cin >> n2)) { 
				       	cin.clear(); 
				        cin.ignore(1000, '\n'); 
				        cout << " ---------------------------------------------------\n";
				        cout << "| Ingrese un numero valido de filas para la matriz  |\n";
				        cout << " ---------------------------------------------------\n";
				    }	
				    
					cout << " ---------------------------------------------------\n";
					cout << "|  Ingresa la cantidad de columnas de la matriz 2   |\n";
					cout << " ---------------------------------------------------\n";
					while (!(cin >> m2)) { 
				       	cin.clear(); 
				       	cin.ignore(1000, '\n'); 
				        cout << " ---------------------------------------------------\n";
				        cout << "| Ingrese un numero valido de filas para la matriz  |\n";
				        cout << " ---------------------------------------------------\n";
				    }
				    
				    if (n2>9 || m2>9 || n2<1 || m2<1)
				    {
				    	cout << " ---------------------------------------------------\n";
				        cout << "|La matriz solo puede tener de 1 a 9 filas/columnas |\n";
				        cout << " ---------------------------------------------------\n";
				        _getch();
				       	system("cls");
					} else {
						cout << " ---------------------------------------------------\n";
						cout << "|     La Matriz 2 tendra: " << n1 << " filas y " << m1 << " columnas      |\n";
						cout << " ---------------------------------------------------\n";
						_getch();
					}
				} while (n2>9 || m2>9 || n2<1 || m2<1);
				
				system("cls");
				cout << " ---------------------------------------------------\n";
				cout << "|                     Matriz 1                      |\n";
				cout << "|                                                   |\n";
				cout << "| Presiona 1 para ingresar la matriz 1 manualmente  |\n";
				cout << "| Presione 2 para ingresarla de forma random        |\n";
				cout << " ---------------------------------------------------\n";
				while (!(cin >> menu_ran) || menu_ran<1 || menu_ran>2) { 
				  	cin.clear(); 
			       	cin.ignore(1000, '\n'); 
			        cout << " ---------------------------------------------------\n";
			        cout << "|   Seleccione una de las dos opciones unicamente   |\n";
			        cout << " ---------------------------------------------------\n";
			    }
				
				if (menu_ran==1)
				{	cout << " ---------------------------------------------------\n";
					cout << "| Ingrese los datos para la Matriz 1:               |\n";
					for (int i = 0; i < n1; i++){
						for (int j = 0; j < m1; j++){
							cout << "| Ingrese el numero: " << i+1 << "," << j+1 
							<< "                            |" << endl;
							cin >> matriz1[i][j];
						}
					} cout << " ---------------------------------------------------\n";
					
					cout << endl << " ---------------------------------------------------\n";
					cout << "| Esta sera la Matriz 1:                            |\n";
					cout << " ---------------------------------------------------\n";
					for (int i = 0; i < n1; i++){
						for (int j = 0; j < m1; j++){
							cout << "[ " << matriz1[i][j] << " ] ";
						}
						cout << endl;
					}
					_getch();
				} else {
					srand(time(NULL));
					for (i=0; i<n1; i++){
						for (j=0; j<m1; j++){
						matriz1[i][j] = rand()%100;
						}
					} 
					cout << " ---------------------------------------------------\n";
					cout << "| Esta sera la Matriz 1 random:                     |\n";
					cout << " ---------------------------------------------------\n";
					for (int i = 0; i < n1; i++){
						for (int j = 0; j < m1; j++){
							cout << "[ " << matriz1[i][j] << " ] ";
						}
						cout << endl;	
					}
					_getch();
				} 
				system("cls");
				cout << " ---------------------------------------------------\n";
				cout << "|                     Matriz 2                      |\n";
				cout << "|                                                   |\n";
				cout << "|Presiona 1 para ingresar la matriz 2 manualmente   |\n";
				cout << "|Presione 2 para ingresarla de forma random         |\n";
				cout << " ---------------------------------------------------\n";
				while (!(cin >> menu_ran) || menu_ran<1 || menu_ran>2) { 
				  	cin.clear(); 
			       	cin.ignore(1000, '\n'); 
			        cout << " ---------------------------------------------------\n";
			        cout << "|   Seleccione una de las dos opciones unicamente   |\n";
			        cout << " ---------------------------------------------------\n";
			    }
				
				cout << " ";
				if (menu_ran==1)
				{
					cout << " ---------------------------------------------------\n";
					cout << "| Para la Matriz 2:                                 |\n";
					for (int i = 0; i < n2; i++){
						for (int j = 0; j < m2; j++){
							cout << "| Ingrese el numero: " << i+1 << "," << j+1 
							<< "                            |" << endl;
							cin >> matriz2[i][j];
						}
					} cout << " ---------------------------------------------------\n";
					
					cout << endl << " ---------------------------------------------------\n";
					cout << "| Esta sera la Matriz 2:                            |\n";
					cout << " ---------------------------------------------------\n";
					for (int i = 0; i < n2; i++){
						for (int j = 0; j < m2; j++){
							cout << "[ " << matriz2[i][j] << " ] ";
						}
						cout << endl;
					}
					_getch();
				} else {
					srand(time(NULL));
					for (int i=0; i<n2; i++){
						for (int j=0; j<m2; j++){
						matriz2[i][j] = rand()%100;
						}
					} 
					cout << " ---------------------------------------------------\n";
					cout << "| Esta sera la Matriz 2 random:                     |\n";
					cout << " ---------------------------------------------------\n";
					for (int i = 0; i < n2; i++){
						for (int j = 0; j < m2; j++){
							cout << "[ " << matriz2[i][j] << " ] ";
						}
						cout << endl;	
					}
					_getch();
				} 
								
				do 
				{
					system("cls");
					cout << " ---------------------------------------------------\n";
					cout << "|                                                   |\n";
					cout << "| Presiona 1 para sumar las dos matrices            |\n";
					cout << "| Presiona 2 para obtener la matriz transpuesta     |\n";
					cout << "| Presiona 3 para multiplicar las dos matrices      |\n";
					cout << "| Presiona 4 para encontrar un numero en una matriz |\n";
					cout << "|                                                   |\n";
					cout << "| Presiona 0 para regresar al menu principal        |\n";
					cout << "|                                                   |\n";
					cout << " --------------------------------------------------- \n";
					while (!(cin >> menu_2) || menu_2<0 || menu_2 > 4) { 
				       	cin.clear(); 
				       	cin.ignore(1000, '\n'); 
				        cout << " ---------------------------------------------------\n";
				        cout << "| Ingrese el numero de una de las opciones          |\n";
				        cout << " ---------------------------------------------------\n";
				    }
					
					switch(menu_2)
					{
						case 1:
							// Suma de matrices
							if (m1==m2 && n1==n2)
							{
								system("cls");
								
								for (int i=0;i<n1;i++){
									for(int j=0;j<m1;j++){
										suma[i][j] = matriz1[i][j] + matriz2[i][j];
									}
								}
								system("cls");
								cout << " ---------------------------------------------------\n";
								cout << "| Este es el resultado de sumar la Matriz 1 y 2:    |\n";
								cout << " ---------------------------------------------------\n";
							    for (int i=0; i<n1; i++){
							        for (int j=0; j<m1; j++){
							        	cout << "[ " << suma[i][j] << " ] ";
							        }
							        cout << endl;
							    } _getch();
								
							}else {
								system("cls");
								cout << " ---------------------------------------------------\n";
								cout << "| Solo puedes sumar matrices con la misma cantidad  |\n";
								cout << "| de filas y columnas.                              |\n";
								cout << "|                                                   |\n";
								cout << "| Presiona cualquier tecla para volver al menu e    |\n";
								cout << "| intentalo de nuevo.                               |\n";
								cout << " ---------------------------------------------------\n";
								_getch();
								break;
								system("cls");
								}
						break;	
								
						case 2:	
							// Matriz transpuesta	
							system("cls");
							cout << " ---------------------------------------------------\n";
							cout << "| Deseas obtener la Matriz Transpuesta de           |\n";
							cout << "| la Matriz 1 o 2?                                  |\n";
							cout << "|                                                   |\n";
							cout << "| Presiona 1 si quieres la de la Matriz 1           |\n";
							cout << "| Presiona 2 si quieres la de la Matriz 2           |\n";
							cout << "|                                                   |\n";
							cout << "| Presiona 3 si quieres usar una nueva Matriz       |\n";
							cout << " ---------------------------------------------------\n";
				
							while (!(cin >> menu_t) || menu_t<1 || menu_t> 3) { 
						       	cin.clear(); 
						       	cin.ignore(1000, '\n'); 
						        cout << " ---------------------------------------------------\n";
						        cout << "| Ingrese el numero de una de las opciones          |\n";
						        cout << " ---------------------------------------------------\n";
						    }
						    
						    system("cls");
						    
						    if (menu_t==1){
						    	cout << " ---------------------------------------------------\n";
								cout << "| La Matriz 1 original es                           |\n";
								cout << " ---------------------------------------------------\n";
						    	for (int i=0;i<n1;i++){
									for (int j=0; j<m1; j++){
										cout << "[ " << matriz1[i][j] << " ] ";
									}
									cout << endl;
								}
								cout << endl << " ---------------------------------------------------\n";
								cout << "| El resultado de la Matriz 1 Transpuesta es:       |\n";
						        cout << " ---------------------------------------------------\n";
						    	for (int i=0;i<n1;i++){
									for (int j=0; j<m1; j++){
										cout << "[ " << matriz1[j][i] << " ] ";
									}
									cout << endl;
								}
								_getch();
							} 
							
							if (menu_t==2){
								cout << " ---------------------------------------------------\n";
								cout << "| La Matriz 2 original es:                          |\n";
								cout << " ---------------------------------------------------\n";
						    	for (int i=0;i<n2;i++){
									for (int j=0; j<m2; j++){
										cout << "[ " << matriz2[i][j] << " ] ";
									}
									cout << endl;
								}
								cout << " ---------------------------------------------------\n";
						        cout << "| El resultado de la Matriz 2 Transpuesta es:       |\n";
						        cout << " ---------------------------------------------------\n";
						    	for (int j=0;j<m2;j++){
									for (int i=0; i<n2; i++){
										cout << "[ " << matriz2[i][j] << " ] ";
									}
									cout << endl;
								}
								_getch();
							} 
							
							if (menu_t==3) {
								do {
									cout << " ---------------------------------------------------\n";
									cout << "|    Ingresa la cantidad de filas de la Matriz      |\n";
									cout << " ---------------------------------------------------\n";
									while (!(cin >> n3)) { 
								       	cin.clear(); 
								        cin.ignore(1000, '\n'); 
								        cout << " ---------------------------------------------------\n";
								        cout << "| Ingrese un numero valido de filas para la matriz  |\n";
								        cout << " ---------------------------------------------------\n";
								    }
								    
									cout << " ---------------------------------------------------\n";
									cout << "|   Ingresa la cantidad de columnas de la Matriz    |\n";
									cout << " ---------------------------------------------------\n";
									while (!(cin >> m3)) { 
								       	cin.clear(); 
								        cin.ignore(1000, '\n'); 
								        cout << " ---------------------------------------------------\n";
								        cout << "| Ingrese un numero valido de filas para la Matriz  |\n";
								        cout << " ---------------------------------------------------\n";
								    }
								    
								    if (n3>9 || m3>9 || n3<1 || m3<1)
								    {
								    	cout << " ---------------------------------------------------\n";
								        cout << "|La matriz solo puede tener de 1 a 9 filas/columnas |\n";
								        cout << " ---------------------------------------------------\n";
								        _getch();
								       	system("cls");	
									} else {
										cout << " ---------------------------------------------------\n";
										cout << "|     La Matriz tendra: " << n3 << " filas y " << m3 
										<< " columnas        |\n";
										cout << " ---------------------------------------------------\n";
										_getch();
									}
									
								}while (n3>9 || m3>9 || n3<1 || m3<1);
								
								system("cls");
								cout << " ---------------------------------------------------\n";
								cout << "|                   Matriz nueva                    |\n";
								cout << "|                                                   |\n";
								cout << "|Presiona 1 para ingresar la matriz manualmente     |\n";
								cout << "|Presione 2 para ingresarla de forma random         |\n";
								cout << " ---------------------------------------------------\n";
								while (!(cin >> menu_ran) || menu_ran<1 || menu_ran>2) { 
								  	cin.clear(); 
							       	cin.ignore(1000, '\n'); 
							        cout << " ---------------------------------------------------\n";
							        cout << "|   Seleccione una de las dos opciones unicamente   |\n";
							        cout << " ---------------------------------------------------\n";
							    }
								
								if (menu_ran==1)
								{
									cout << " ---------------------------------------------------\n";
									cout << "| Para la nueva Matriz:                             |\n";
									for (int i = 0; i < n3; i++){
										for (int j = 0; j < m3; j++){
											cout << "| Ingrese el numero: " << i+1 << "," << j+1 
											<< "                            |" << endl;
											cin >> matriz3[i][j];
										}
									} cout << " ---------------------------------------------------\n";
									
									system("cls");
									cout << endl << " ---------------------------------------------------\n";
									cout << "| Esta sera la nueva Matriz:                        |\n";
									cout << " ---------------------------------------------------\n";
									for (int i = 0; i < n3; i++){
										for (int j = 0; j < m3; j++){
											cout << "[ " << matriz3[i][j] << " ] ";
										}
										cout << endl;
									}
									
								} else {
									srand(time(NULL));
									for (int i=0; i<n3; i++){
										for (int j=0; j<m3; j++){
										matriz3[i][j] = rand()%100;
										}
									} 
									cout << " ---------------------------------------------------\n";
									cout << "| Esta sera la nueva Matriz random:                 |\n";
									cout << " ---------------------------------------------------\n";
									for (int i = 0; i < n3; i++){
										for (int j = 0; j < m3; j++){
											cout << "[ " << matriz3[i][j] << " ] ";
										}
										cout << endl;	
									}
								}
								
								cout << endl << " ---------------------------------------------------\n";
								cout << "| El resultado de la nueva Matriz Transpuesta es:   |\n";
						        cout << " ---------------------------------------------------\n";
						    	for (int i=0;i<n3;i++){
									for (int j=0; j<m3; j++){
										cout << "[ " << matriz3[j][i] << " ] ";
									}
									cout << endl;
								}
								_getch();
							}
						break;	
							
						case 3:
							// Multiplicaci�n de matrices
							if (m1==n2)
							{
								system("cls");
								for (int i=0;i<n1;i++){
									for(int j=0;j<m2;j++){
										multi[i][j]=0;
										for(int k=0;k<m1;k++){
											multi[i][j] += (matriz1[i][k]*matriz2[k][j]);
										}
									} 
								}
								cout << " ---------------------------------------------------\n";
								cout << "| Este es el total al multiplicar la Matriz 1 y 2:  |\n";
								cout << " ---------------------------------------------------\n";
							    for (int i=0; i<n1; i++){
							        for (int j=0; j<m2; j++){
							        	cout << "[ " << multi[i][j] << " ] ";
							        }
							        cout << endl;
							    } 
							    cout << endl << " ---------------------------------------------------\n";
								cout << "| Este es el procedimiento para multiplicarlas:     |\n";
								cout << " ---------------------------------------------------\n";
								for (int i = 0; i < n1; i++) {              
								    for (int j = 0; j < m2; j++) {          
								        multi[i][j] = 0;
								
								        for (int k = 0; k < m1; k++) {    
								            cout << " [ " <<  matriz1[i][k] << " ] " << "* [ " 
											<< matriz2[k][j] << " ] ";
								            if (k < m1 - 1) cout << " + "; 
								            multi[i][j] += matriz1[i][k] * matriz2[k][j];
								        }
								        cout << " = " << multi[i][j] << endl;
								    }
								}
								_getch();
								
							}else {
								system("cls");
								cout << " ---------------------------------------------------\n";
								cout << "| La cantidad de columnas de la Matriz 1 tiene que  |\n";
								cout << "| ser igual a la cantidad de filas de la Matriz 2   |\n";
								cout << "| para poder multiplicarlas                         |\n";
								cout << "|                                                   |\n";
								cout << "| Presiona cualquier tecla para volver al menu e    |\n";
								cout << "| intentalo de nuevo.                               |\n";
								cout << " ---------------------------------------------------\n";
								_getch();
								system("cls");
								}
						break;
						
						case 4:
							// Buscar un n�mero en una matriz
							system("cls");
								cout << " ---------------------------------------------------\n";
								cout << "| En que matriz deseas buscar un numero?            |\n";
								cout << "|                                                   |\n";
								cout << "| Presiona 1 para buscar en la Matriz 1             |\n";
								cout << "| Presiona 2 para buscar en la Matriz 2             |\n";
								cout << " ---------------------------------------------------\n";
								while (!(cin >> menu_num) || menu_num<1 || menu_num>2) { 
								  	cin.clear(); 
							       	cin.ignore(1000, '\n'); 
							        cout << " ---------------------------------------------------\n";
							        cout << "|   Seleccione una de las dos opciones unicamente   |\n";
							        cout << " ---------------------------------------------------\n";
								}
								bool ubicado = false;
								
								if (menu_num==1){
									cout << " ---------------------------------------------------\n";
							        cout << "| Ingrese el numero que desea buscar en la Matriz 1 |\n";
							        cout << " ---------------------------------------------------\n";
							    	while (!(cin >> num)){ 
								  	cin.clear(); 
							       	cin.ignore(1000, '\n'); 
							        cout << " ---------------------------------------------------\n";
							        cout << "| Porfavor ingrese unicamente numeros               |\n";
							        cout << " ---------------------------------------------------\n";
									}
									
									for (int i = 0; i < n1; i++){
										for (int j = 0; j < m1; j++){
											if(num==matriz1[i][j]){
												cout << " ---------------------------------------------------\n";
												cout << "| El numero se encuentra en la posicion: " << i +1 << "," 
												<< j +1 << "        | \n";
												cout << " ---------------------------------------------------\n";
												ubicado = true;
												_getch();
											}
										}
										cout << endl;	
									}
									
									if (!ubicado){
										cout << " ---------------------------------------------------\n";
										cout << "| Ese numero no se encuentra en la matriz           |\n";
										cout << " ---------------------------------------------------\n";
										_getch();
									}    
								}
								if (menu_num==2){
									cout << " ---------------------------------------------------\n";
							        cout << "| Ingrese el numero que desea buscar en la Matriz 2 |\n";
							        cout << " ---------------------------------------------------\n";
							    	while (!(cin >> num)){ 
								  	cin.clear(); 
							       	cin.ignore(1000, '\n'); 
							        cout << " ---------------------------------------------------\n";
							        cout << "| Porfavor ingrese unicamente numeros               |\n";
							        cout << " ---------------------------------------------------\n";
									}
									
									for (int i = 0; i < n2; i++){
										for (int j = 0; j < m2; j++){
											if(num==matriz2[i][j]){
												cout << " ---------------------------------------------------\n";
												cout << "| El numero se encuentra en la posicion: " << i +1 << "," 
												<< j +1 << "        | \n";
												cout << " ---------------------------------------------------\n";
												ubicado = true;
												_getch();
											}
										}
										cout << endl;	
									}
									
									if (!ubicado){
										cout << " ---------------------------------------------------\n";
										cout << "| Ese numero no se encuentra en la matriz           |\n";
										cout << " ---------------------------------------------------\n";
										_getch();
									}    
								}
						break;
					}		
					
				} while (menu_2!=0);
				system("cls");
				
			break;
			
			case 2:
				system("cls");
				do{	
					cout << " ---------------------------------------------------\n";
					cout << "|                     Bienvenido!                   |\n";
					cout << "|                                                   |\n";
					cout << "| Presiona 1 para contar palabras en un texto       |\n";
					cout << "| Presiona 2 para ordenar alfabeticamente una cadena|\n";
					cout << "| Presiona 3 para detectar una subcadena de texto   |\n";
					cout << "| Presiona 4 para verificar un palindromo           |\n";
					cout << "|                                                   |\n";			
					cout << "| Presiona 0 para salir                             |\n";
					cout << " --------------------------------------------------- \n";	
					while (!(cin >> menu_cade) || menu_cade<0 || menu_cade>4) { 
					  	cin.clear(); 
				       	cin.ignore(1000, '\n'); 
				        cout << " ---------------------------------------------------\n";
				        cout << "|  Seleccione una de las opciones unicamente        |\n";
				        cout << " ---------------------------------------------------\n";
				    }
				    
				    cin.ignore(1000, '\n');
				    if (menu_cade==1){
				    	system("cls");
				    	cout << " ---------------------------------------------------\n";
						cout << "| Porfavor ingresa el texto del que deseas contar   |\n";
						cout << "| cuantas palabras contiene                         |\n";
						cout << "|                                                   |\n";
						cout << "| Y presiona ENTER 2 veces para calcular            |\n";
						cout << " ---------------------------------------------------\n";
						
						int contador=0;
						
						do {
						    getline(cin, texto);
						
						    if (texto.empty()) {
						        break;
						    }
						
						    stringstream tx(texto);
						    while (tx >> palabras) {
						        contador++;
						    }
						
						} while (true);
						cout << " ---------------------------------------------------\n";
						cout << "| Esta es la cantidad total de palabras:            |\n" << contador << endl;
						_getch();
						system("cls");
					}
				    
				    if (menu_cade==2){
				    	system("cls");
				    	cout << " ---------------------------------------------------\n";
						cout << "| Porfavor ingresa el texto que deseas ordenar:     |\n";
						cout << "|                                                   |\n";
						cout << "| Y presiona ENTER 2 veces para calcular            |\n";
						cout << " ---------------------------------------------------\n";
						
					    while (true) {
					        getline(cin, lineas_orden);
					        if (lineas_orden.empty()) break;
					        texto2 += lineas_orden;
					    }
					
						sort(texto2.begin(), texto2.end());
				
				    	cout << " ---------------------------------------------------\n";
						cout << "| Este es el texto ordenado en orden alfabetico:    |\n" << texto2 << endl;
						_getch();
						system("cls");
					}
					
				    if (menu_cade==3){
				    	system("cls");
				    	cout << " ---------------------------------------------------\n";
						cout << "| Porfavor ingresa el texto en el que deseas        |\n";
						cout << "| encontrar una subcadena:                          |\n";
						cout << " ---------------------------------------------------\n";
						
						do {
						    getline(cin, texto3);
						
						    if (texto3.empty()) break;
						    texto_total += texto3 + " ";
						} while (true);
						
						cout << " ---------------------------------------------------\n";
						cout << "| Porfavor ingresa la subcadena que deseas buscar   |\n";
						cout << " ---------------------------------------------------\n";
						
						
						    getline(cin, subcadena);
				
						size_t pos = texto_total.find(subcadena);

					    if (pos != string::npos) {
						cout << " ---------------------------------------------------\n";
						cout << "| La subcadena esta en la posicion:                 |\n" <<  pos << endl;
					    } else {
						cout << " ---------------------------------------------------\n";
						cout << "| Esta subcadena no es parte del texto original     |\n";
						cout << " ---------------------------------------------------\n";
					    }
						_getch();
						system("cls");
					}
				
				    if (menu_cade==4){
				    	system("cls");
				    	cout << " ---------------------------------------------------\n";
						cout << "| Porfavor ingresa una palabra para verificar si    |\n";
						cout << "| es palindromo o no:                               |\n";
						cout << " ---------------------------------------------------\n";
						cin >> palindromo;
						
				    	transform(palindromo.begin(), palindromo.end(), palindromo.begin(), ::tolower);

					    bool palindromo_si = true;
					    int n = palindromo.size();
					
					    for (int i = 0; i < n / 2; i++) {
					        if (palindromo[i] != palindromo[n - 1 - i]) {
					            palindromo_si = false;
					            break;
					        }
					    }
					
					    if (palindromo_si) {
					        cout << " ---------------------------------------------------\n";
					        cout << "| La palabra \"" << palindromo << "\" si es palindromo \n";
					        cout << " ---------------------------------------------------\n";
					    } else {
					        cout << " ---------------------------------------------------\n";
					        cout << "| La palabra \"" << palindromo << "\" no es palindromo \n";
					        cout << " ---------------------------------------------------\n";
					    }
						_getch();
						system("cls");
					}
				
				} while (menu_cade!=0);
				system("cls");
		}
	
	} while (menu_1 != 0);
	
	return 0;
}
