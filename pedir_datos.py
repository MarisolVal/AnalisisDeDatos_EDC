#Declaración de variables

int_Edad = 0
float_Estatura = 0.0
str_Nombre = ""
str_Apellido = ""

#Inicio del programa

int_Edad = int(input('Introduce tu edad: '))
float_Estatura = float(input('Introduce Tu estatura: '))
str_Nombre = input('Introduce tu nombre: ')
str_Apellido = input('Introduce Tu apellido: ')

print ("")
print ("TUS DATOS SON:")
print ("")
print ("Tu Edad es:        %d" %(int_Edad ))
print ("Tu Estatura :      %1.2f" %(float_Estatura))
print ("Tu Inicial:        %s" %(str_Nombre))
print ("Tu Apellido:       %s" %(str_Apellido))
