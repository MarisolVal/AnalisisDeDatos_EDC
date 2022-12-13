import os
from dibujo import dibujo
from palabras import palabras

#La función "mostrar_palabra" recibe la palabra a adivinar y la lista de letras correctas hasta el momento e imprime las letras correctas en su posición correspondiente o '_' en la posición de las letras faltantes
def mostrar_palabra(palabra, correctas):
    mostrar = 'Palabra :'               #Cadena de caracteres que se mostrará en pantalla
    for i in palabra:                   #ciclo que intera sobre todas las letras de la palabra a adivinar.
        if i in correctas:              #Verifica si la letra se encuentra en la lista de correctas
            mostrar += ' '+i+' '        #Si la letra está dentro de la lista de letras adivinadas, la agrega a "mostrar"
        else:
            mostrar += ' _ '            #Si la letra no se encuentra en la lista "correctas", agrega '_' a "mostrar"
    print(mostrar+'\n')

#La función "mostrar_incorrectas" recibe la lista de letras incorrectas y las imprime en pantalla
def mostrar_incorrectas(incorrectas):
    mostrar = 'Letras incorrectas: '    #Cadena de caracteres que se mostrará en pantalla
    for i in incorrectas:               #Ciclo que itera sobre todas las letras incorrectas
        if(i==incorrectas[0]):          #Verificca si la letra incorrecta es la primera de la lista o no
            mostrar += i                #En caso de ser la primer letra incorrecta, simplementa la agrega a "mostrar"
        else:
            mostrar += ', '+i           #En caso de no ser la primera, también agrega una coma
    print(mostrar+'\n')

palabra = palabras()        #Palabra a adivinar
#"palabra_aux" es la misma palabra pero quitándole los acentos a las vocales
palabra_aux = palabra.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ü','u')
correctas = []              #Lista de letras adivinadas correctamente
incorrectas = []            #Lista de intentos que no forman parte de la palabra
errores = 0                 #Cantidad de intentos fallidos
#"abcd" contiene todos los caracteres válidos.
abcd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

#Este ciclo se detiene solo hasta que se adivinen todas las letras o se terminen los intentos
while(errores<6 and len(palabra)>len(correctas)):
    os.system('cls')                        #Limpia la pantalla
    dibujo(errores)                         #Llama a la función "dibujo" para que dibuje al ahorcado en función de la cantidad de errores cometidos
    mostrar_palabra(palabra_aux, correctas) #Imprime las letras de la palabra que ya fueron adivinadas
    mostrar_incorrectas(incorrectas)        #Imprime las letras incorrectas
    valido = False                          #Variable usada para verificar que se ingrese una sola letra
    while(valido==False):                   #Ciclo para verificar que se ingrese una letra válida
        letra = str(input('Escriba una letra: '))   #caracter(es) ingresado(s)
        #"letra_aux" es la misma que "letra" pero con minúsculas y sin acentos para poder ser comparada con "palabra_aux"
        letra_aux = letra.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ü','u')
        if(len(letra_aux)!=1):                                          #Para verificar si "letra" tiene 1 o más caracteres
            print('Debes ingrasar exactamente un caracter.')                #En caso no tener 1 solo caracter, imprime esto y vuelve a pedir otra
        else:                                                               #En caso de tener exactamente 1 caracter hace lo siguiente
            if(letra_aux in abcd):                                                  #Verifica si es un caracter es una letra de "abcd"
                if(letra_aux in correctas or letra in incorrectas):                         #Si es una letra de "abcd", verifica si la letra no se ha utilizado antes
                    print(f'La letra {letra_aux} ya fue usada. Intenta con otra letra.')            #Indica si la letra ya ha sido utilizado antes y pide que ingrese otra
                else:
                    valido = True                                                                   #Si la letra no ha sido utilizada antes, indica que es una letra válido
            else:
                print(f'{letra_aux} no es una letra. Intenta otra vez.')                    #Si no es una letra de "abcd", entonces indica que no es válido y pide que ingrese una válida
    
    if(letra_aux in palabra_aux):               #Para comprobar si la letra forma parte de la palabra
        aux = palabra_aux.split(letra_aux)      #divide "palabra_aux" utilizando como separador "letra_aux" y los ordena en una lista. (Si la palabra tiene la misma letra repetida n veces, entonces la lista tendrá n+1 elementos)
        for i in aux[:-1]:                      #Ciclo que itera sobre todos los elementos de la lista "aux", salvo el último elemento
            correctas.append(letra_aux)         #Agrega "letra_aux" a la lista de letras correctas tantas veces como aparesca repetida en "palabra_aux"
    else:                                       
        errores += 1                            #Si "letra_aux" no se encuentra en "palabra_aux", se contabiliza un error más
        incorrectas.append(letra_aux)           #Y se agrega "letra_aux" a la lista de letras incorrectas

os.system('cls')                            #Limpia la pantalla
dibujo(errores)                             #Imprime el dibujo del ahorcado en función de los errores cometidos
mostrar_palabra(palabra_aux, correctas)     #Muestra las letras adivinadas de la palabra y los espacios de las letras aún desconocidas
mostrar_incorrectas(incorrectas)            #Muestra las letras que se han intentado pero que no forman parte de la palabra
if(errores==6):                             #Para indicar si se ganó o se perdió
    print('Jajajajajaja ¡PERDISTE!\n')      #Indica que se ha perdiddo en caso de haber alcanzado el máximo número de errores
else:
    print('¡FELICIDADES! ¡GANASTE!\n')      #Indica que se ganó en caso de haber adivinado todas las palabras.