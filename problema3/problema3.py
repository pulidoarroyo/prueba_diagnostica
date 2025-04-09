# implemente la evaluación de expresiones aritméticas considerando los operadores +,-,*,/ y los operandos pueden ser ingresados en notación científica
# la entrada al programa será una cadena de caracteres con la expresión
# ejemplo de expresión a evaluar: (125E10 – 1e15)/5E-85*15.


import re # Importar la librería re para expresiones regulares

def tokenizar(expresion):
    # Se convierte la cadena en una lista de tokens para separar a los números de los operadores
    # Patrón para capturar números en notación científica o regular y operadores
    patron = r'(\d+\.\d+[eE][+-]?\d+|\d+[eE][+-]?\d+|\d+\.\d+|\d+|[+\-*/()])'
    
    # Encontrar todos los tokens
    tokens = re.findall(patron, expresion)
    
    # Convertir números a float y dejar operadores como string
    resultado = []
    for token in tokens:
        if token in '+-*/()':
            resultado.append(token)
        else:
            resultado.append(float(token))
    
    return resultado


    # Se convierte una expresión en notación infija (o común, Ej: 2+3) a postfija  (Ej: 2 3 +) usando el algoritmo shunting-yard
def convertir_a_postfijo(tokens):
    
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    salida = []
    operadores = []
    
    for token in tokens:
        # Si es un número, añadirlo a la salida
        if isinstance(token, float):
            salida.append(token)
        # Si es un operador
        elif token in '+-*/':
            while (operadores and operadores[-1] != '(' and 
                   precedencia.get(operadores[-1], 0) >= precedencia.get(token, 0)):
                salida.append(operadores.pop())
            operadores.append(token)
        # Si es un paréntesis izquierdo
        elif token == '(':
            operadores.append(token)
        # Si es un paréntesis derecho
        elif token == ')':
            while operadores and operadores[-1] != '(':
                salida.append(operadores.pop())
            if operadores and operadores[-1] == '(':
                operadores.pop()  # Eliminar el paréntesis izquierdo
    
    # Añadir los operadores restantes a la salida
    while operadores:
        salida.append(operadores.pop())
    
    return salida

    # Luego de convertir la expresión a postfijo, se evalúa la expresión con una pila
def evaluar_postfijo(expresion_postfija):

    pila = []
    
    for token in expresion_postfija:
        if isinstance(token, float):
            pila.append(token)
        else:
            # Es un operador, sacar dos operandos de la pila
            b = pila.pop()
            a = pila.pop()
            
            # Realizar la operación
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("División por cero")
                pila.append(a / b)
    
    # El resultado final debe estar al tope de la pila
    return pila[0]

    #Función principal para evaluar la expresión aritmética
def evaluar_expresion(expresion):
   
    # Eliminar espacios y preparar la expresión
    expresion = expresion.replace(" ", "")
    
    try:
        # Convertir la expresión a tokens
        tokens = tokenizar(expresion)
        
        # Convertir la expresión infija a postfija
        postfijo = convertir_a_postfijo(tokens)
        
        # Evaluar la expresión postfija
        resultado = evaluar_postfijo(postfijo)
        
        return resultado
    except Exception as e:
        return f"Error: {str(e)}"

# Ejemplo de uso
if __name__ == "__main__":
    # Pruebas con diferentes expresiones
    expresiones = [
        "3+4*2", # 11
        "3.5+4.2", # 7.7
        "2E3+4",  # 2000 + 4
        "5E-8*2",  # 5x10^-8 * 2
        "125E25/5",  # 125x10^25 / 5
        "(2+3)*4", #20
        "2.5E3 - 1.2E2",# 2500 - 120
        "(125E10 - 1e15)/5E-85*15" # -2.99625e+100
    ]
    
    for expr in expresiones:
        resultado = evaluar_expresion(expr)
        print(f"Expresión: {expr} = {resultado}")
    
    # Solicitar input de expresión al usuario
    print("Ingrese expresiones aritméticas para evaluar (presione Enter para salir):")
    
    while True:
        expresion_usuario = input("\nExpresión: ")
        if expresion_usuario == "":
            print("Ejecución finalizada.")
            break
            
        resultado = evaluar_expresion(expresion_usuario)
        print(f"Resultado: {resultado}")