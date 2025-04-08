import problema1  

# Ejemplos predefinidos para mostrar al usuario
ejemplos = [
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",  # Posición inicial
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",  # Después de 1.e4
    "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3"  # Apertura Ruy López
]

if __name__ == "__main__":
    print("VALIDADOR DE NOTACIÓN FEN (Forsyth-Edwards Notation)")
    print("-" * 50)
    print("Ejemplos de notación FEN válida:")
    for i, ejemplo in enumerate(ejemplos):
        print(f"{i+1}. {ejemplo}")
    print("-" * 50)
    
    # Input para que el usuario ingrese una cadena FEN
    print("Ingrese una cadena FEN para validar (o presione Enter para salir):")
    
    while True:
        entrada_usuario = input("> ").strip()
        
        if not entrada_usuario:
            print("¡Adiós!")
            break
        
        if problema1.validar_fen(entrada_usuario):
            print("✓ La cadena FEN es VÁLIDA")
        else:
            print("✗ La cadena FEN es INVÁLIDA")
        
        print("\nIngrese otra cadena FEN para validar (o presione Enter para salir):")


