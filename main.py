# import csear

# Bienvenido

# Crea una rama la cual tendra como nombre: [Tu nombre completo]

# para esto ejecuta el comando 

# git branch nombre-de-la-nueva-rama

# Luego ejecuta el comando para cambiarte de rama

# git checkout nombre-de-la-nueva-rama

# para despues ejecutar

# git branch

# Te debe aparecer 

# *nombre-de-la-nueva-rama

# Ya con esto estaras en la nueva rama, en esta sera en la que vas a desarrollar el ejercicio

# Recuerda que el nombre de la rama deber ser [Tu nombre completo]


# INSTRUCCIONES

# Debes resolver 3 retos, luego de realizarlos los vas a guardar en la variable
# codigo_ganador = str(resultado_reto3) + str(resultado_reto1) + str(resultado_reto2)
# convirtiéndolos en cadenas y luego concatenándolos juntos en la variable codigo_ganador. 


# Cuando lo imprimas, te daras cuenta que en la variable codigo_ganador guarda un codigo, pasa este codigo como 
# parametro en la funcion traduccion_cesar que se encueentra en el modulo cesar.py 
# Esta sera el codigo con el que ganaras el reto!

# Deja la respuesta en la parte final del codigo de esta manera

# Respuesta = [Codigo que te genero el archivo el metodo del archvivo cesar.py]




# RETO NUMERO 1


# En este ejercicio, debes implementar una función llamada clasificacion_de_Numeros que tome un número como argumento y
# lo clasifique en diferentes categorías según ciertos rangos. Los rangos y sus categorías son los siguientes categorias 
# y le pases por parametro el numero 40 cuando llames el metodo en la seccion LLAMANDO METODOS

# Si el número está entre 1 y 10 (incluyendo ambos), la categoría es "nqja".
# Si el número está entre 11 y 20 (incluyendo ambos), la categoría es "lqj".
# Si el número está entre 21 y 30 (incluyendo ambos), la categoría es "awqas".
# Si el número está entre 31 y 40 (incluyendo ambos), la categoría es "b Kdn".
# Si el número está entre 41 y 50 (incluyendo ambos), la categoría es "la d".
# Si el número está entre 51 y 60 (incluyendo ambos), la categoría es "Kdss".
# Si el número está entre 61 y 70 (incluyendo ambos), la categoría es "drh sf".
# Si el número está entre 71 y 80 (incluyendo ambos), la categoría es "qfdgwf".
# Si el número está entre 81 y 90 (incluyendo ambos), la categoría es "jgho".
# Si el número está entre 91 y 100 (incluyendo ambos), la categoría es "dvnx".
# Si el número no está en ninguno de estos rangos, la categoría es "Número fuera de rango".


def clasificacion_de_Numeros(numero):
    if 1 <= numero <= 10:
        return "nqja"
    # elif 11 <= numero <= 20:
    #     return ...

    # ...

    else:
        return "Número fuera de rango"


# RETO NUMERO 2

# Toma una lista de lenguajes de programacion, analiza los nombres en la lista y cuenta la cantidad total de letras en los 
# nombres que tienen más de 3 caracteres y cuyo cuarto carácter es "a". 

# Los lenguaJes son estos  Python C, Java, PHP, Rubi, JavaScript

# Por ejemplo si las letras que cumplieran estas caracteristicas fueran Helado, y Vino, entonces 
# las letras totales serian Helado = 6 + Vino = 4 entonces el total seria 10

# Por ultimo, debe devolver el metodo clasificacion_de_numeros pero pasandole por parametro las letras_totales


lenguajes = ["Vainilla", "Chocolate", "Fresa", "Mango", "Menta", "Café"]

def analizar_nombres(lista):
    letras_totales = 0
    for nombre in lista:
        if len(nombre) > 4 and nombre[4] == "j":
            letras_totales += len(nombre)
    #  clasificacion_de_Numeros(letras_totales)


# RETO NUMERO 3
# Me suma los multiplos de 3 del 1 al 20 menos los que termninan en 6 
# o sea 3, 9, 12...
# Para luego retornar el metodo clasificacion_de_Numeros pasandole por parametro la suma

# La expresión num % 10 se utiliza para obtener el último dígito de un número en base 10. 
# El operador % en programación se llama operador módulo, y lo que hace es calcular el residuo de la división entre dos números.
# Cuando divides un número por 10, el residuo de esa división será el último dígito del número original. 
# Esto es útil en situaciones donde necesitas trabajar con dígitos individuales de un número.
# Por ejemplo, si tienes el número 753, y haces 753 % 10, obtendrás 3, que es el último dígito de ese número. 
# Si luego divides 753 por 10 (es decir, 753 // 10), obtendrás 75, que es el número sin el último dígito.


def imprimir_multiplos_de_tres(inicio, fin, paso):
     suma = 0
     for num in range(inicio, fin, paso):
        ultimo_digito = 0 #...  
        if ultimo_digito != 5:
            suma -= num
     return clasificacion_de_Numeros(int(suma))

# LLAMANDO METODOS

def main():
    resultado_reto1 = clasificacion_de_Numeros(?)
    # resultado_reto3 = imprimir_multiplos_de_tres(3, 21, 3)
    # resultado_reto2 = analizar_nombres(lenguajes)
    # codigo_ganador = str(resultado_reto?) + str(resultado...
    # print(cesar.traduccion_cesar(codigo_ganador))


if __name__ == "__main__":
    main()

