from ejercicios_matrices.funciones_matriz import imprimir_matriz,  ingresar_elemento
def validar_repetido(matriz: list, lista_valores: list, fila: int, columna: int, total_elementos: int):

    repetido = False
    bandera = True
    while bandera == True: #ASEGURAMOS INGRESAR EL VALOR VALIDADO
        imprimir_matriz(matriz)
        print(lista_valores)
        print()
        el_elemento = ingresar_elemento(f'Ingresar el valor para fila {fila} - columna {columna}')
                            #VERIFICA ESTE DENTRO DEL RANGO
        print(f'Verificando Rango...')
        if el_elemento >= 1 and el_elemento <= total_elementos:
            print(f'rango correcto...')
            #VERIFICA QUE NO ESTE REPETIDO
            print(f'Verificando Repetidos...')
                                

            for i in range(len(lista_valores)):
                                    
                #EL ERROR ERA EN ESTA COMPARACIÓN.
                if el_elemento == lista_valores[i]:
                    print(f'EL NUMERO ESTÁ REPETIDO, INGRESA DE NUEVO')
                                        
                    repetido = True
                    break #FALTABA UN BREAK, SI ESTABA REPETIDO, ROMPE Y REPITE CICLO WHILE.
                                        
                else: 
                                        
                    print(f'Almacenando nuevo valor...')
                    repetido = False #ACÁ ALMACENA EL VALOR Y COMPARA PARA TERMINAR CICLO.
                                        
            if repetido == False:
                lista_valores[valor] = el_elemento
                matriz[fila][columna] = el_elemento  
                #ALMACENA UNA VEZ.
                #LUEGO EL OTRO ERROR ESTABA AQUI. NO AUMENTABA EL VALOR EN EL LUGAR CORRECTO.    
                valor +=1
                print('Almacenado nuevo valor en la lista...')
                bandera = False


        else: 
            print(f'Valor fuera de rango, ingrese otro')