


def contar_palabras(texto):
    """
    Cuenta el número de palabras en el texto dado.

    Args:
        texto (str): El texto a analizar.

    Returns:
        int: El número de palabras en el texto.
    """
    palabras = texto.split()
    return len(palabras)
    
