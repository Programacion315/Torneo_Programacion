# El cifrado César es una técnica de cifrado muy básica y antigua que se atribuye al famoso líder militar romano Julio César. 
# Funciona desplazando cada letra en un texto un número fijo de posiciones hacia adelante en el alfabeto. 
# Por ejemplo, con un desplazamiento de 3, la letra "A" se convierte en "D", la letra "B" en "E", y así sucesivamente.

# Aquí hay un ejemplo simple con un desplazamiento de 3:

# Texto original: HELLO
# Texto cifrado: KHOOR

# Cada letra en "HELLO" ha sido reemplazada por la letra que se encuentra 3 posiciones hacia adelante en el alfabeto.

def traduccion_cesar(text):
    shift = -3  
    translated_text = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                translated = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                translated = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            translated_text += translated
        else:
            translated_text += char

    return translated_text


