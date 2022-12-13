import random

#Función que devuelve una palabra al azar elegida entre todas las disponibles en la lista
def palabras():
    palabras = ['ahorcado', 'esternocleidomastoideo', 'otorrinolaringólogo', 'idiosincrasia', 'desoxirribonucleico', 'paralelepípedo', 'ovovivíparo', 'caleidoscopio',
    'elecrtroencefalografista', 'humanidad', 'adolescente', 'anciano', 'caballero', 'individuo', 'espinilla', 'estómago', 'resfriado', 'enfermedad', 'matrimonio', 'bisabuelo', 'nacimiento',
    'reproducción', 'naturaleza', 'laguna', 'montaña', 'energía', 'elefante', 'gorrión', 'camarón', 'langosta', 'sardina', 'calamar', 'mariposa', 'insecto', 'saltamontes', 'mosquito',
    'cucaracha', 'caracol', 'babosa', 'lombrices', 'marisco', 'molusco', 'lagarto', 'serpiente', 'cocodrilo', 'almendra', 'zanahoria', 'guisantes', 'plátano', 'gaseosa', 'anochecer', 'mediodía',
    'miércoles', 'calendario', 'pingüino']                      #Lista de posibles palabras
    palabra = palabras[random.randint(0, len(palabras)-1)]      #Para elegir una palabra al azar de la lista "palabras"
    return palabra                                              #Devuelve la palabra elegida al azar