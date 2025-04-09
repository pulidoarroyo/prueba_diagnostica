# Dado un número entero no negativo n
# a) Genere los coeficientes del polinomio (x+1)n, muestre el resultado de polinomio
# b) Muestre por pasos el cálculo para x dado, f(x) = (x+1)n, según el polinomio generado
# Para generar los polinomios de (x+1)n utilice el triangulo de pascal.

def generar_triangulo_pascal(n):
    
   # Genera las primeras n+1 filas del triángulo de Pascal.
   # Cada fila representa los coeficientes de (x+1)^n para n = 0, 1, 2, ..., n

    triangulo = []
    for i in range(n + 1):
        # Iniciar una nueva fila
        fila = [1]  # El primer elemento siempre es 1
        
        # Calcular los elementos intermedios basados en la fila anterior
        if i > 0:
            fila_anterior = triangulo[i - 1]
            for j in range(len(fila_anterior) - 1):
                fila.append(fila_anterior[j] + fila_anterior[j + 1])
            
            # El último elemento siempre es 1
            fila.append(1)
        
        triangulo.append(fila)
    
    return triangulo

    # Imprime el triángulo de Pascal de manera formateada
def mostrar_triangulo_pascal(triangulo):
    
    print("Triángulo de Pascal:")
    for i, fila in enumerate(triangulo):
        # Ajustar el formato para centrar cada fila
        print(f"n={i}: {fila}")

def obtener_polinomio(coeficientes):
   
    # Genera una representación en string del polinomio (x+1)^n basado en sus coeficientes
    
    n = len(coeficientes) - 1
    terminos = []
    
    for i, coef in enumerate(coeficientes):
        # Calcular el exponente de x para este término
        exp = n - i
        
        # Generar el término
        if coef == 0:
            continue  # Omitir términos con coeficiente 0
        
        # Formatear el coeficiente
        if coef == 1 and exp > 0:
            coef_str = ""
        else:
            coef_str = str(coef)
        
        # Formatear la variable x con su exponente
        if exp == 0:
            x_str = ""
        elif exp == 1:
            x_str = "x"
        else:
            x_str = f"x^{exp}"
        
        # Combinar coeficiente y variable
        termino = coef_str + x_str
        if termino:
            terminos.append(termino)
    
    # Unir todos los términos con signos
    if not terminos:
        return "0"
    
    resultado = terminos[0]
    for t in terminos[1:]:
        if t[0] == "-":
            resultado += " " + t
        else:
            resultado += " + " + t
    
    return resultado

def evaluar_polinomio(coeficientes, x, detallado=False):
   
    # Evalúa el polinomio para un valor dado de x Si detallado = True, muestra los pasos intermedios
    
    n = len(coeficientes) - 1
    resultado = 0
    pasos = []
    
    for i, coef in enumerate(coeficientes):
        # Calcular el exponente de x para este término
        exp = n - i
        
        # Calcular el valor de este término
        termino = coef * (x ** exp)
        resultado += termino
        
        # Almacenar paso si es detallado
        if detallado:
            # Formatear el término para mostrar
            if coef == 1 and exp > 0:
                coef_str = ""
            else:
                coef_str = str(coef)
            
            if exp == 0:
                x_str = ""
            elif exp == 1:
                x_str = "x"
            else:
                x_str = f"x^{exp}"
            
            # Mostrar el término en el polinomio
            termino_str = coef_str + x_str
            
            # Calcular y mostrar la sustitución
            if exp == 0:
                valor_str = f"{coef}"
            elif exp == 1:
                valor_str = f"{coef}*{x}"
            else:
                valor_str = f"{coef}*{x}^{exp}"
            
            # Mostrar el valor calculado
            pasos.append(f"{termino_str} = {valor_str} = {termino}")
    
    return resultado, pasos

    # Función principal que ejecuta el programa
def polinomio_binomial():
    while True:
        try:
            n = int(input("\nIngrese '0' o un número entero no negativo n (o -1 para salir): "))
            if n == -1:
                print("Ejecución finalizada")
                break
            if n < 0:
                print("Por favor, ingrese un número no negativo.")
                continue
            
            # Generar los coeficientes usando el triángulo de Pascal
            triangulo = generar_triangulo_pascal(n)
            coeficientes = triangulo[n]
            
            # Mostrar el triángulo de Pascal para referencia
            mostrar_triangulo_pascal(triangulo)
            
            # Imprime el polinomio resultante
            polinomio = obtener_polinomio(coeficientes)
            print(f"\na) El polinomio (x+1)^{n} expandido es:")
            print(f"   {polinomio}")
            
            # Se evalua al polinomio para un valor dado utilizando la función de evaluación
            try:
                x = float(input("\nIngrese un valor para x: "))
                resultado, pasos = evaluar_polinomio(coeficientes, x, detallado=True)
                
                # Mostrar los pasos de cálculo
                print(f"\nb) Cálculo de f({x}) = (x+1)^{n} paso a paso:")
                for paso in pasos:
                    print(f"   {paso}")
                print(f"\n   Resultado final: f({x}) = {resultado}")
                
                # Verificar el resultado usando la fórmula directa
                resultado_directo = (x + 1) ** n
                print(f"\n   Verificación: ({x}+1)^{n} = {resultado_directo}")
                
            except ValueError:
                print("Error: Ingrese un número válido para x.") # Permite un número entero o decimal
            
        except ValueError:
            print("Error: Ingrese un número entero válido para n.") # Solo permite un número entero

if __name__ == "__main__":
    polinomio_binomial()