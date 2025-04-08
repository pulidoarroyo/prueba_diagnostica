# Dado una cadena C, valide si C se encuentra en notación FEN (Forsyth-Edwards Notation)

def validar_fen(cadena):
    # Comprobar si la cadena es una cadena válida
    if not isinstance(cadena, str):
        return False
    
    # Comprobar si la cadena está vacía
    if not cadena:
        return False
    
    # Se divide a la cadena en sus seis campos
    campos = cadena.split()
    
    # Una cadena válida se compone de exactamente 6 campos
    if len(campos) != 6:
        return False
    
    # Desempaquetar los campos
    posicion, turno, enroque, al_paso, medio_movimiento, movimiento_completo = campos
    
    # A continuación se realizan las verificaciones de cada uno de los campos de una cadena FEN válida
    
    # 1) Validar el campo de posición (tiene 8 filas separadas por '/')
    filas = posicion.split('/')
    if len(filas) != 8:
        return False
    
    for fila in filas:
        # Una fila del tablero contiene 8 espacios o casillas, se utiliza un contador para asegurar que cada fila representa exactamente 8 casillas
        casillas_contadas = 0
        
        for caracter in fila:
            if caracter.isdigit():
                casillas_contadas += int(caracter)
                # Verificar que el número está entre 1 y 8
                if int(caracter) < 1 or int(caracter) > 8:
                    return False
            elif caracter in 'rnbqkpRNBQKP':
                casillas_contadas += 1
            else:
                # El caracter introducido es distinto a los permitidos por lo tanto es inválido
                return False
        
        # Cada fila debe tener exactamente 8 casillas
        if casillas_contadas != 8:
            return False
    
    # 2) Validar el turno o el próximo a mover una pieza (debe ser 'w' que representa al blanco o 'b' que representa al negro)
    if turno not in ['w', 'b']:
        return False
    
    # 3) Validar enroque, tambien llamado 'castling', (combinación de 'KQkq' o '-')
    if enroque != '-':
        for c in enroque:
            if c not in 'KQkq':
                return False
        # Verificar si hay caracteres duplicados
        if len(enroque) != len(set(enroque)):
            return False
    
    # 4) Validar casilla al paso, tambien llamado 'en passant' (e3, a6, etc. o '-')
    if al_paso != '-':
        if len(al_paso) != 2:
            return False
        if al_paso[0] not in 'abcdefgh' or al_paso[1] not in '36':  # Solo puede ser fila 3 o 6
            return False
        
        # Verificación adicional: si el turno es 'w', la casilla debe estar en la fila 6
        # si el turno es 'b', la casilla debe estar en la fila 3
        if (turno == 'w' and al_paso[1] != '6') or (turno == 'b' and al_paso[1] != '3'):
            return False
    
    # 5) Validar contador de medio movimiento (un entero no negativo)
    try:
        if int(medio_movimiento) < 0:
            return False
    except ValueError:
        return False
    
    # 6) Validar contador de movimientos completos (un entero positivo)
    try:
        if int(movimiento_completo) < 1:
            return False
    except ValueError:
        return False
    
    # Verificación adicional: comprobar que hay exactamente un rey de cada color
    reyes_blancos = posicion.count('K')
    reyes_negros = posicion.count('k')
    
    if reyes_blancos != 1 or reyes_negros != 1:
        return False
    
    # Si pasa todas las verificaciones, Se devuelve TRUE y la cadena FEN es válida, de lo contrario se devuelve FALSE
    return True


# Ejemplo de uso
if __name__ == "__main__":
    ejemplo_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
    print(f"¿Es válido '{ejemplo_fen}'? {validar_fen(ejemplo_fen)}")